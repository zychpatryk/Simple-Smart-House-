from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique = True)
    login = db.Column(db.String(150))
    password = db.Column(db.String(150))

class Temperature(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    temperature = db.Column(db.String(150))

