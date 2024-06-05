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

class Organisers(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role = db.Column(db.Integer)
    dep = db.Column(db.Integer)

class Payments(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    autopay_val = db.Column(db.String(150))
    state = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)

class Workshops(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    workshop_1 = db.Column(db.Integer)
    workshop_2 = db.Column(db.Integer)
    workshop_3 = db.Column(db.Integer)
    workshop_4 = db.Column(db.Integer)
    ergo_workshop = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)

class Participations(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    file_status = db.Column(db.Integer)
    block = db.Column(db.Integer)
    link_to_file = db.Column(db.String(150))

class Tickets(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.ticket'), primary_key = True)
    type_of = db.Column(db.String(150))
    price = db.Column(db.Float(2))
    currency = db.Column(db.String(150))
