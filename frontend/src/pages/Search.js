import React, { useState } from 'react';
import axios from 'axios';
import MovieCard from '../components/videos/movieCard';

const Search = () => {
    const [searchTerm, setSearchTerm] = useState('');
    const [searchResults, setSearchResults] = useState([]);

    const handleSearch = async () => {
        try {
            const response = await axios.get(`/api/search?q=${searchTerm}`);
            setSearchResults(response.data.movies);
        } catch (error) {
            console.error('Error searching movies:', error);
        }
    };

    return (
        <div>
            <h2>Search</h2>
            <input type="text" value={searchTerm} onChange={e => setSearchTerm(e.target.value)} />
            <button onClick={handleSearch}>Search</button>
            <div className="search-results">
                {searchResults.map(movie => (
                    <MovieCard key={movie.id} movie={movie} />
                ))}
            </div>
        </div>
    );
}

export default Search;
