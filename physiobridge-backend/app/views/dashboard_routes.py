# app/views/dashboard_routes.py

from flask import Blueprint, jsonify

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/status', methods=['GET'])
def dashboard_status():
    return jsonify({'message': 'Dashboard route is working!'})
