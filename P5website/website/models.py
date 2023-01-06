from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    activities = db.relationship('Activities')
    current_stats = db.relationship('current_stats')

class Activities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String(200))
    guts_effect = db.Column(db.Integer)
    kindness_effect = db.Column(db.Integer)
    knowledge_effect = db.Column(db.Integer)
    charisma_effect = db.Column(db.Integer)
    proficency_effect = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class current_stats(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    prestige = db.Column(db.Integer)
    guts_level = db.Column(db.Integer)
    charisma_level = db.Column(db.Integer)
    proficency_level = db.Column(db.Integer)
    kindness_level = db.Column(db.Integer)
    knowledge_level = db.Column(db.Integer)


