# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Import and register routes
from routes import auth, videos

app.register_blueprint(auth.bp)
app.register_blueprint(videos.bp)

if __name__ == '__main__':
    app.run(debug=True)
