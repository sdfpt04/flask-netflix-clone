# routes/auth.py
from flask import Blueprint, request, jsonify, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Please provide username, email, and password'}), 400

    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({'error': 'Username or email already exists'}), 400

    new_user = User(username=username, email=email, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Please provide username and password'}), 400

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid username or password'}), 401

    login_user(user)
    return jsonify({'message': 'Logged in successfully'}), 200

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'}), 200

