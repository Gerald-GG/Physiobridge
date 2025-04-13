# app/views/booking_routes.py

from flask import Blueprint, jsonify

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/test', methods=['GET'])
def test_booking():
    return jsonify({'message': 'Booking route is working!'})
