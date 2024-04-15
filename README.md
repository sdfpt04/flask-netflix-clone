# Flask-React Netflix Clone

This is a Netflix clone built using Flask for the backend and React for the frontend.

## Features

- User authentication: Users can sign up, log in, and log out.
- Video streaming: Users can watch movies and TV shows.
- Dynamic and responsive user interface: Inspired by Netflix's UI design.
- Genre browsing: Users can browse movies and TV shows by genre.
- My List: Users can add movies and TV shows to their watchlist.
- Search: Users can search for movies and TV shows.

## Setup

### Backend

1. Install Python 3 and Pipenv.
2. Navigate to the `backend` directory.
3. Run `pipenv install` to install dependencies.
4. Set up the database by running `flask db init`, `flask db migrate`, and `flask db upgrade`.
5. Start the Flask server by running `flask run`.

### Frontend

1. Install Node.js and npm.
2. Navigate to the `frontend` directory.
3. Run `npm install` to install dependencies.
4. Start the React development server by running `npm start`.

## Technologies Used

- Flask: Python web framework for the backend.
- Flask-SQLAlchemy: Database ORM for Flask.
- React: JavaScript library for building user interfaces.
- React Router: Routing library for React.
- Flask-Login: User session management for Flask.
- Axios: Promise-based HTTP client for making API requests.
- Bootstrap: Frontend framework for responsive design.


## License

This project is licensed under the [MIT License](LICENSE).
