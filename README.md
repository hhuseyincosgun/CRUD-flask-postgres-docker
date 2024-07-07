# CRUD-flask-postgres-docker
A CRUD application using Flask, PostgreSQL, and Docker
![arc](https://github.com/hhuseyincosgun/CRUD-flask-postgres-docker/assets/21257660/030f6560-a45a-44fe-90a3-d1922543c9f0)

## Summary

This is a Flask web application that provides a RESTful API for performing CRUD (Create, Read, Update, Delete) operations on a PostgreSQL database using SQLAlchemy as the ORM (Object Relational Mapper). Here is a detailed breakdown of its functionality:

### Setup and Configuration
- The Flask application is created and configured to connect to a PostgreSQL database using a database URL obtained from environment variables.
- SQLAlchemy is initialized with the Flask application to handle database interactions.

### Database Model
- A `User` model is defined, representing the structure of the `users` table in the database. This model includes fields for `id`, `username`, and `email`.
- The model also includes a `json` method to serialize the model instance into a JSON-compatible dictionary.

### Database Initialization
- `db.create_all()` is called to create the `users` table in the database if it does not already exist.

### API Endpoints
- **Test Route**: A simple GET route (`/test`) that returns a JSON message to verify that the API is working.
- **Create User**: A POST route (`/users`) that accepts JSON data to create a new user. It adds the user to the database and returns a success message.
- **Get All Users**: A GET route (`/users`) that retrieves all users from the database and returns them as a JSON array.
- **Get User by ID**: A GET route (`/users/<int:id>`) that retrieves a user by their ID and returns the user data as JSON. If the user is not found, it returns a 404 error.
- **Update User**: A PUT route (`/users/<int:id>`) that updates the username and email of a user identified by their ID. It returns a success message if the update is successful or a 404 error if the user is not found.
- **Delete User**: A DELETE route (`/users/<int:id>`) that deletes a user by their ID. It returns a success message if the deletion is successful or a 404 error if the user is not found.

![crudd](https://github.com/hhuseyincosgun/CRUD-flask-postgres-docker/assets/21257660/68cb8db3-77b6-4583-8a1c-a64c9b29f139)

### Error Handling
- Each route is wrapped in a try-except block to handle any exceptions that occur during database operations. If an exception is caught, a 500 error with an appropriate error message is returned.

----------

## Architecture and Tools

This architecture illustrates a CRUD application built using Flask, PostgreSQL, and Docker.

### Architecture Overview

1. **Docker and Docker Compose**:
   - **Docker**: Containerizes the application for consistency across environments.
   - **Docker Compose**: Manages and orchestrates the Flask application and PostgreSQL database.

2. **Flask Application**:
   - Containerized using Docker, defines dependencies and runs the app.
   - Provides a RESTful API for CRUD operations on user data.
   - Communicates with PostgreSQL for data storage and retrieval.

3. **PostgreSQL Database**:
   - Containerized using Docker for easy setup.
   - Stores user information with schema managed by SQLAlchemy ORM.

4. **Postman**:
   - Used for API development and testing.
   - Sends HTTP requests to API endpoints and verifies responses.

5. **DBeaver**:
   - Database management tool for interacting with PostgreSQL.
   - Provides a GUI for running SQL queries and managing tables.

### Tools Used

- **Docker**: Ensures consistency, simplifies deployment, isolates dependencies.
- **Docker Compose**: Manages multiple containers, easy setup and teardown.
- **Flask**: Lightweight web framework for building APIs.
- **PostgreSQL**: Robust, scalable relational database.
- **SQLAlchemy**: ORM for simplifying database operations.
- **Postman**: User-friendly tool for testing API endpoints.
- **DBeaver**: GUI for managing and querying databases.

### Summary

The setup leverages Docker for containerization, Flask for the API, PostgreSQL for the database, and SQLAlchemy for ORM. Postman and DBeaver are used for API testing and database management, ensuring a consistent development environment and simplifying deployment.


#### References
- https://www.edureka.co/blog/what-is-rest-api/
- https://www.youtube.com/watch?v=fHQWTsWqBdE&t=103s
- https://app.diagrams.net/
- 

