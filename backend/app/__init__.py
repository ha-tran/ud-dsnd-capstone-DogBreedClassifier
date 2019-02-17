from flask import Flask
from flask_cors import CORS


# init machine learning model
model = None
# init Flask app
app = Flask(__name__)
app.config.from_object('config')
CORS(app)

@app.route("/")
def hello():
    return "Hello World!"

from app.modules.classifier import mod_classifier

# Register blueprints
app.register_blueprint(mod_classifier)