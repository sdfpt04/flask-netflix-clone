import React from 'react';

const MovieDetails = ({ movie }) => {
    return (
        <div className="movie-details">
            <h2>{movie.title}</h2>
            <p>{movie.description}</p>
            {}
        </div>
    );
}

export default MovieDetails;
