from flask import Blueprint, jsonify


health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "message": "Health check successful",
        'status': 'success',
        "code": 200
        }), 200
    
