# CRUD-flask-postgres-docker
A CRUD application using Flask, PostgreSQL, and Docker
![arc](https://github.com/hhuseyincosgun/CRUD-flask-postgres-docker/assets/21257660/030f6560-a45a-44fe-90a3-d1922543c9f0)

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

![crudd](https://github.com/hhuseyincosgun/CRUD-flask-postgres-docker/assets/21257660/68cb8db3-77b6-4583-8a1c-a64c9b29f139)

- **Test Route**: A simple GET route (`/test`) that returns a JSON message to verify that the API is working.
![image](https://github.com/hhuseyincosgun/CRUD-flask-postgres-docker/assets/21257660/490913d2-9046-4520-b96d-21d8af64adfc)


- **Create User**: A POST route (`/users`) that accepts JSON data to create a new user. It adds the user to the database and returns a success message.
![image](https://github.com/hhuseyincosgun/CRUD-flask-postgres-docker/assets/21257660/1c57ef1a-ac16-47d2-b945-cb561046edac)

- **Get All Users**: A GET route (`/users`) that retrieves all users from the database and returns them as a JSON array.
![image](https://github.com/hhuseyincosgun/CRUD-flask-postgres-docker/assets/21257660/a6ea0004-5fee-4f1a-99c1-949bd19d8bf8)

- **DBeaver**

![image](https://github.com/hhuseyincosgun/CRUD-flask-postgres-docker/assets/21257660/67d61e07-fdd5-46d5-a017-8a33fb4646ca)


- **Get User by ID**: A GET route (`/users/<int:id>`) that retrieves a user by their ID and returns the user data as JSON. If the user is not found, it returns a 404 error.
![image](https://github.com/hhuseyincosgun/CRUD-flask-postgres-docker/assets/21257660/80470f1b-725b-4de0-8714-83e1e7c0c0b9)

- **Update User**: A PUT route (`/users/<int:id>`) that updates the username and email of a user identified by their ID. It returns a success message if the update is successful or a 404 error if the user is not found.
![image](https://github.com/hhuseyincosgun/CRUD-flask-postgres-docker/assets/21257660/f77c7e6c-2897-4862-a9b1-001cf764d306)

![image](https://github.com/hhuseyincosgun/CRUD-flask-postgres-docker/assets/21257660/3e586b47-dd78-4b89-9f1d-ab8921a3c2f6)

- **Delete User**: A DELETE route (`/users/<int:id>`) that deletes a user by their ID. It returns a success message if the deletion is successful or a 404 error if the user is not found.
![image](https://github.com/hhuseyincosgun/CRUD-flask-postgres-docker/assets/21257660/79f92ade-1b2d-4433-93c4-2e1ec6195bcc)

![image](https://github.com/hhuseyincosgun/CRUD-flask-postgres-docker/assets/21257660/02b0cbf1-6531-47b4-95e5-90985ef6b52d)

![image](https://github.com/hhuseyincosgun/CRUD-flask-postgres-docker/assets/21257660/c3a18d3f-2b43-4f6e-9419-99f4872a3cdc)

----------


#### References
- https://www.edureka.co/blog/what-is-rest-api/
- https://www.youtube.com/watch?v=fHQWTsWqBdE&t=103s
- https://app.diagrams.net/
