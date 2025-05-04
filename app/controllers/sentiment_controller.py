from flask import Blueprint, jsonify, request
from app.services.textBlob_service import TextBlobService

sentiment_bp = Blueprint('sentiment', __name__)

@sentiment_bp.route('/sentiment', methods=['POST'])
def sentiment():
    body = request.get_json()
    message = body['message']
    
    if not message:
        return jsonify({'message': 'Message is required'}), 404
    
    return TextBlobService().get_sentiment(message)
