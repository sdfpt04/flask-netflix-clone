# models.py
from app import db
import uuid

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    movie_lists = db.relationship('MovieList', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uu_id = db.Column(db.String(36), default=str(uuid.uuid4()))
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    genre = db.Column(db.String(100), nullable=False)
    length = db.Column(db.Integer, nullable=False)
    image_card = db.Column(db.String(255), nullable=False)
    image_cover = db.Column(db.String(255), nullable=False) 
    video = db.Column(db.String(255), nullable=False)  
    movie_views = db.Column(db.Integer, default=0)

    def __repr__(self):
        return self.title

class MovieList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    
    owner_user = db.relationship('User', back_populates='movie_lists')
    movie = db.relationship('Movie', back_populates='lists')
