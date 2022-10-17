from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
#DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdfsdlkgjelriteojskledfjsekl asdkljasdkl'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    

    from .views import views
    from .auth import auth
    from .projects import projects
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(projects, url_prefix='/')

    from .models import User # !! remember to import class before creating database to create proper table

    with app.app_context():
        db.create_all()
    #create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #if not logged in -> directed to auth.login()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app