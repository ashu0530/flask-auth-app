# Flask User Authentication App

This is a simple Flask web application for user registration, login, and a basic dashboard.

## Features

- **User Registration**: Allows new users to create an account by providing a name, email, and password.
- **User Login**: Existing users can log in using their email and password.
- **Session Management**: Uses Flask session to keep users logged in across multiple requests.
- **Password Hashing**: User passwords are securely hashed using bcrypt before storing them in the database.
- **Dashboard**: Once logged in, users can access a simple dashboard displaying their account details.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ashu0530/flask-auth-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd flask-auth-app
    ```
    
## Usage

1. Set up the Flask application:

    ```bash
    export FLASK_APP=app.py
    export FLASK_ENV=development
    ```

2. Initialize the SQLite database:

    ```bash
    flask init-db
    ```

3. Run the Flask application:

    ```bash
    flask run
    ```

4. Or you can run directly:

    ```bash
    python3 app.py
    ```

5. Access the application in your web browser at `http://localhost:5000`.

## Configuration

- **Database URI**: The application uses SQLite by default.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request.
