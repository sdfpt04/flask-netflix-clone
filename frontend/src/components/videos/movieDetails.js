import React from 'react';

const MovieDetails = ({ movie }) => {
    return (
        <div className="movie-details">
            <h2>{movie.title}</h2>
            <p>{movie.description}</p>
            {/* Add more details like genre, release date, etc. */}
        </div>
    );
}

export default MovieDetails;
