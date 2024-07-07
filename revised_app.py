from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL', 'sqlite:///default.db')  # Default DB for local testing
db = SQLAlchemy(app)

# Model definition
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def json(self):
        return {'id': self.id, 'username': self.username, 'email': self.email}

db.create_all()

# Test route
@app.route('/test', methods=['GET'])
def test():
    return make_response(jsonify({'message': 'test route'}), 200)

# Create a user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        if not data or not 'username' in data or not 'email' in data:
            return make_response(jsonify({'message': 'Invalid input'}), 400)

        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return make_response(jsonify({'message': 'user created'}), 201)
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({'message': f'error creating user: {str(e)}'}), 500)

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return make_response(jsonify([user.json() for user in users]), 200)
    except Exception as e:
        return make_response(jsonify({'message': f'error getting users: {str(e)}'}), 500)

# Get a user by ID
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = User.query.get(id)
        if user:
            return make_response(jsonify({'user': user.json()}), 200)
        return make_response(jsonify({'message': 'user not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': f'error getting user: {str(e)}'}), 500)

# Update a user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.get(id)
        if user:
            data = request.get_json()
            if not data or not 'username' in data or not 'email' in data:
                return make_response(jsonify({'message': 'Invalid input'}), 400)

            user.username = data['username']
            user.email = data['email']
            db.session.commit()
            return make_response(jsonify({'message': 'user updated'}), 200)
        return make_response(jsonify({'message': 'user not found'}), 404)
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({'message': f'error updating user: {str(e)}'}), 500)

# Delete a user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({'message': 'user deleted'}), 200)
        return make_response(jsonify({'message': 'user not found'}), 404)
    except Exception as e:
        db.session.rollback()
        return make_response(jsonify({'message': f'error deleting user: {str(e)}'}), 500)

if __name__ == '__main__':
    app.run(debug=True)
