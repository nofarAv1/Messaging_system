from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(120), nullable=False)

    def __init__(self, user):
        self.user = user


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    message_subject = db.Column(db.String(100), nullable=True)
    message = db.Column(db.String, nullable=False)
    message_read = db.Column(db.Boolean, nullable=False, default=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # define relationships
    sender = db.relationship('User', backref='sender', foreign_keys=[sender_id])
    receiver = db.relationship('User', backref='receiver', foreign_keys=[receiver_id])

    # def __init__(self, sender_id, receiver_id, message_subject, message):
    #     self.sender_id = sender_id,
    #     self.receiver_id = receiver_id,
    #     self.message_subject = message_subject
    #     self.message = message



