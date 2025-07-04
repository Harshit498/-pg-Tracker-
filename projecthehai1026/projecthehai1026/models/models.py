from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class PG(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    sharing_type = db.Column(db.String(50), nullable=False)
    amenities = db.Column(db.String(200), nullable=False)  # Comma-separated
    image_url = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)

class Roommate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    about = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

class TiffinService(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    menu = db.Column(db.Text, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    area_covered = db.Column(db.String(200), nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password) 