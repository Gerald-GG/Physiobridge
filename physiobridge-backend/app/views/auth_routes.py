# app/views/auth_routes.py

from flask import Blueprint, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET'])
def login():
    return jsonify({'message': 'Login route is working!'})
