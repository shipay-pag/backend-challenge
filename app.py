from flask import Flask, request, jsonify
from models import Session, Role ,User,Base
from werkzeug.security import generate_password_hash
import random
import string
from datetime import datetime


app = Flask(__name__)
def generate_random_password():
    password_length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(password_length))



@app.route('/api/role', methods=['POST'])
def create_role():
    data = request.get_json()
    description = data.get('description')
    
    if not description:
        return jsonify({"message": "description is required"}), 400

    # Using a context manager to automatically commit and close the session
    with Session() as session:
        role = Role(description=description)
        session.add(role)
        session.commit()  # Commit the transaction to the database

        # Accessing the role.id after the commit to ensure it's associated with the session
        role_id = role.id

        return jsonify({"message": "Role created successfully", "role_id": role_id}), 201



@app.route('/api/user/<int:role_id>/role', methods=['GET'])
def get_role(role_id):
    session = Session()
    users = session.query(User).filter_by(role_id=role_id).all()

    if not users:
        session.close()
        return jsonify(message="No users found with this role ID"), 404
    
    user_roles = [user.role.description for user in users]
    
    session.close()  # Closing the session after accessing related attributes

    return jsonify(user_roles=user_roles)



@app.route('/api/user', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    role_id = data.get('role_id')
    password = data.get('password') or generate_random_password()


    if not (name and email and role_id):
        return jsonify({"message": "Name, email, and role_id are required"}), 400

    session = Session()
    created_at = datetime.now()


    role = session.query(Role).filter(Role.id == role_id).first()
    if not role:
        return jsonify({"error": "Role not found"}), 404

    user = User(name=name, email=email, role_id=role_id, password=password, created_at=created_at)
    session.add(user)
    session.commit()
    user_id = user.id

    session.close()
    # if user:
    #     return jsonify({'message': 'User created successfully',"user_id":user.id}), 201
    # else:
    #     return jsonify({'error': 'Failed to create user'}), 500

    return jsonify({"message": "User created successfully" ,"user_id": user_id}), 201

if __name__ == '__main__':
    app.run(debug=True)
