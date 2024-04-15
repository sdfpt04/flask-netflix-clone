// services/Auth.js
import axios from 'axios';

const login = async (username, password) => {
    try {
        const response = await axios.post('/api/login', { username, password });
        return response.data;
    } catch (error) {
        console.error('Error logging in:', error);
        throw error;
    }
};

const signup = async (username, email, password) => {
    try {
        const response = await axios.post('/api/signup', { username, email, password });
        return response.data;
    } catch (error) {
        console.error('Error signing up:', error);
        throw error;
    }
};

const logout = async () => {
    try {
        const response = await axios.post('/api/logout');
        return response.data;
    } catch (error) {
        console.error('Error logging out:', error);
        throw error;
    }
};

export default { login, signup, logout };
