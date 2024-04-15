// services/Movie.js
import axios from 'axios';

const getMovies = async () => {
    try {
        const response = await axios.get('/api/movies');
        return response.data.movies;
    } catch (error) {
        console.error('Error fetching movies:', error);
        throw error;
    }
};

const getMovie = async (movieId) => {
    try {
        const response = await axios.get(`/api/movie/${movieId}`);
        return response.data.movie;
    } catch (error) {
        console.error(`Error fetching movie with ID ${movieId}:`, error);
        throw error;
    }
};

const getMoviesByGenre = async (genre) => {
    try {
        const response = await axios.get(`/api/genres/${genre}`);
        return response.data.movies;
    } catch (error) {
        console.error(`Error fetching ${genre} movies:`, error);
        throw error;
    }
};

const searchMovies = async (searchTerm) => {
    try {
        const response = await axios.get(`/api/search?q=${searchTerm}`);
        return response.data.movies;
    } catch (error) {
        console.error('Error searching movies:', error);
        throw error;
    }
};

const addToMyList = async (movieId) => {
    try {
        const response = await axios.post('/api/my-list', { movie_id: movieId });
        return response.data;
    } catch (error) {
        console.error('Error adding to my list:', error);
        throw error;
    }
};

export default { getMovies, getMovie, getMoviesByGenre, searchMovies, addToMyList };
