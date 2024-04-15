# routes/videos.py
from flask import Blueprint, request, jsonify, flash
from models import Movie, MovieList, db

videos_bp = Blueprint('videos', __name__)

@videos_bp.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify({'movies': [movie.to_dict() for movie in movies]}), 200

@videos_bp.route('/movie/<uuid:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = Movie.query.filter_by(uuid=movie_id).first_or_404()
    return jsonify({'movie': movie.to_dict()}), 200

@videos_bp.route('/genres/<genre>', methods=['GET'])
def get_movies_by_genre(genre):
    movies = Movie.query.filter_by(genre=genre).all()
    return jsonify({'movies': [movie.to_dict() for movie in movies]}), 200

@videos_bp.route('/search', methods=['GET'])
def search_movies():
    search_term = request.args.get('q')
    movies = Movie.query.filter(Movie.title.ilike(f'%{search_term}%')).all()
    return jsonify({'movies': [movie.to_dict() for movie in movies]}), 200

@videos_bp.route('/my-list', methods=['GET'])
def get_my_list():
    # Implement logic to get the current user's list
    return jsonify({'message': 'List retrieved successfully'}), 200

@videos_bp.route('/my-list', methods=['POST'])
def add_to_my_list():
    data = request.get_json()
    movie_id = data.get('movie_id')

    # Implement logic to add movie to user's list
    flash('Movie added to your list', 'success')
    return jsonify({'message': 'Movie added to your list'}), 201



