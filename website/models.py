from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(150))
    surname = db.Column(db.String(150))
    password = db.Column(db.String(150))
    title = db.Column(db.String(150))
    student_index = db.Column(db.String(150), unique = True)
    email = db.Column(db.String(150), unique = True)
    institution = db.Column(db.String(150))
    telephone = db.Column(db.String(150), unique = True)
    ticket = db.Column(db.Integer)
    participation = db.Column(db.Integer)
    active_participation = db.Column(db.Integer)
    from_where = db.Column(db.Integer)
    interests = db.Column(db.String(150))
    

class Temperature(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    temperature = db.Column(db.String(150))

