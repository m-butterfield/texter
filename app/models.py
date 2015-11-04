"""
Texter Models

"""
from app import db


class Text(db.Model):
    """
    Text model

    """
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.Integer, nullable=False)
    carrier_name = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String, nullable=False)
    send_time = db.Column(db.DateTime, nullable=False)
    sent = db.Column(db.Boolean)
