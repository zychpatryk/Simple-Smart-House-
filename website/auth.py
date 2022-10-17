from tabnanny import check
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')

        if '@' in login:
            user = User.query.filter_by(email=login).first()
        else:
            user = User.query.filter_by(login=login).first()
        
        if user:
            if check_password_hash(user.password, password):
                flash('Zalogowano pomyślnie', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Niepoprawne hasło, spróbuj ponownie', category='error')
        else:
            if '@' in login:
                flash('Użytkownik o podanym adresie e-mail nie istnieje', category='error')
            else:
                flash('Użytkownik o podanym loginie nie istnieje', category='error')
    return render_template('login.html', user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Wylogowano', category='secondary')
    return redirect(url_for('views.home'))

@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        login = request.form.get("login")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        userL = User.query.filter_by(login=login).first()
        userE = User.query.filter_by(email=email).first()

        if userL:
            flash('Podany login jest już zajęty', category='error')
        elif userE:
            flash('Podany adres e-mail jest już zajęty', category='error')    
        elif len(email) < 4:
            flash('Adres e-mail musi być dłuższy niż 3 znaki oraz musi zawierać "@".', category='error')
        elif len(login) < 3:
            flash('Login musi być dłuższy niż 3 znaki.', category='error')
        elif len(firstName) < 2:
            flash('Długość imienia nie może być krótsze niż 2 znaki.', category = 'error')
        elif password1.islower() or not has_number(password1) or len(password1) < 7:
            flash('Hasło musi zawierać co najmniej jedną wielką literę oraz przynajmniej jedną cyfrę, a także być niekrótsze niż 7 znaków.', category='error')
        elif password1 != password2:
            flash('Podane hasła muszą być identyczne', category='error')
        else:
            new_user = User(first_name = firstName, email=email, login = login, password = generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Konto zostało utworzone.', category='success')
            return redirect(url_for('views.home'))
        
    return render_template('sign_up.html', user = current_user)

def has_number(input):
    return any(n.isdigit() for n in input)