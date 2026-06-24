"""
Centralised error response helpers for the Flask app.
"""
from flask import jsonify


def bad_request(message: str):
    return jsonify({"error": message}), 400


def not_implemented_error(feature: str):
    return jsonify({"error": f"{feature} is not implemented yet"}), 501


def internal_error(message: str = "Internal server error"):
    return jsonify({"error": message}), 500
