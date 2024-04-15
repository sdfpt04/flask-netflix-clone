# routes/videos.py
from flask import Blueprint, render_template, request, redirect, jsonify, flash
from flask_login import login_required, current_user
from .models import Movie, MovieList
import re

bp = Blueprint('videos', __name__)

@bp.route('/')
@login_required
def index():
    movies = Movie.query.all()
    featured_movie = movies[-1] if movies else None
    return render_template('index.html', movies=movies, featured_movie=featured_movie)

@bp.route('/movie/<string:pk>/')
@login_required
def movie(pk):
    movie_details = Movie.query.filter_by(uu_id=pk).first_or_404()
    return render_template('movie.html', movie_details=movie_details)

@bp.route('/genre/<string:pk>/')
@login_required
def genre(pk):
    movies = Movie.query.filter_by(genre=pk).all()
    return render_template('genre.html', movies=movies, movie_genre=pk)

@bp.route('/search', methods=['POST'])
@login_required
def search():
    search_term = request.form['search_term']
    movies = Movie.query.filter(Movie.title.ilike(f'%{search_term}%')).all()
    return render_template('search.html', movies=movies, search_term=search_term)

@bp.route('/my-list')
@login_required
def my_list():
    movie_list = current_user.movie_lists
    user_movie_list = [movie.movie for movie in movie_list]
    return render_template('my_list.html', movies=user_movie_list)

@bp.route('/add-to-list', methods=['POST'])
@login_required
def add_to_list():
    movie_url_id = request.form.get('movie_id')
    uuid_pattern = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
    match = re.search(uuid_pattern, movie_url_id)
    movie_id = match.group() if match else None

    if movie_id:
        movie = Movie.query.filter_by(uu_id=movie_id).first_or_404()
        if current_user.add_to_list(movie):
            flash('Added to your list', 'success')
        else:
            flash('Movie already in your list', 'info')
    else:
        flash('Invalid movie ID', 'error')

    return redirect(url_for('videos.index'))


