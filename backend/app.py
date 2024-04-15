# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a long random string
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

# Import your models
from models import User, Movie, MovieList

# Import your routes
from routes.auth import auth_bp
from routes.videos import videos_bp

# Register your blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(videos_bp)

if __name__ == '__main__':
    app.run(debug=True)
