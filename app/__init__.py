from flask import Flask
from app.controllers.sentiment_controller import health_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(health_bp)
    return app

app = create_app()
app.run(debug=True, port=5000)