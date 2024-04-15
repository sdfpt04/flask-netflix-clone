# routes/auth.py
from flask import Blueprint, render_template, request, redirect, jsonify, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Movie, MovieList

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('videos.index'))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('auth.login'))

    return render_template('login.html')

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']

        if password == password2:
            if User.query.filter_by(email=email).first():
                flash('Email already taken', 'error')
                return redirect(url_for('auth.signup'))
            elif User.query.filter_by(username=username).first():
                flash('Username already taken', 'error')
                return redirect(url_for('auth.signup'))
            else:
                user = User(email=email, username=username)
                user.set_password(password)
                user.save()
                login_user(user)
                return redirect(url_for('videos.index'))
        else:
            flash('Passwords do not match', 'error')
            return redirect(url_for('auth.signup'))

    return render_template('signup.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
