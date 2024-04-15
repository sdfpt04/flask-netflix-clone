import React, { useEffect, useState } from 'react';
import axios from 'axios';
import MovieCard from '../components/videos/movieCard';

const Genre = ({ match }) => {
    const genre = match.params.genre;
    const [movies, setMovies] = useState([]);

    useEffect(() => {
        fetchMoviesByGenre();
    }, [genre]);

    const fetchMoviesByGenre = async () => {
        try {
            const response = await axios.get(`/api/genres/${genre}`);
            setMovies(response.data.movies);
        } catch (error) {
            console.error(`Error fetching ${genre} movies:`, error);
        }
    };

    return (
        <div>
            <h2>{genre}</h2>
            <div className="movie-list">
                {movies.map(movie => (
                    <MovieCard key={movie.id} movie={movie} />
                ))}
            </div>
        </div>
    );
}

export default Genre;
