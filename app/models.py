# project/app/models.py
from datetime import datetime
from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    sex = db.Column(db.String(1), nullable=True)
    date_of_birth = db.Column(db.Date, nullable=True)
    weight = db.Column(db.Numeric(5, 2), nullable=True)

    __table_args__ = (
        db.CheckConstraint('sex IN (\'M\', \'F\')', name='sex_check'),
        db.CheckConstraint('weight >= 0', name='weight_check'),
    )

    def is_following(self, user):
        return Followers.query.filter(
            Followers.follower == self.id, 
            Followers.followee == user.id
        ).count() > 0


class Shit(db.Model):
    __tablename__ = 'shit'

    id = db.Column(db.Integer, primary_key=True)
    shape = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    colorID = db.Column(db.Integer, db.ForeignKey('shit_color.id'))
    dimension = db.Column(db.Integer)
    level_of_satisfaction = db.Column(db.Integer, nullable=False)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)

    user = db.relationship('User', backref=db.backref('shits', cascade='all, delete-orphan'))
    color = db.relationship('ShitColor', backref='shits')

    __table_args__ = (
        db.CheckConstraint('shape >= 1 AND shape <= 7', name='shape_check'),
        db.CheckConstraint('quantity >= 0 AND quantity <= 10', name='quantity_check'),
        db.CheckConstraint('dimension >= 1 AND dimension <= 10', name='dimension_check'),
        db.CheckConstraint('level_of_satisfaction >= 1 AND level_of_satisfaction <= 10', name='level_of_satisfaction_check'),
    )


class ShitColor(db.Model):
    __tablename__ = 'shit_color'

    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(50), nullable=False)


class Team(db.Model):
    __tablename__ = 'team'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)


class UserTeam(db.Model):
    __tablename__ = 'user_team'

    userID = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True)
    teamID = db.Column(db.Integer, db.ForeignKey('team.id', ondelete='CASCADE'), primary_key=True)

    user = db.relationship('User', backref=db.backref('user_teams', cascade='all, delete-orphan'))
    team = db.relationship('Team', backref=db.backref('user_teams', cascade='all, delete-orphan'))


class Followers(db.Model):
    follower = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    followee = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
