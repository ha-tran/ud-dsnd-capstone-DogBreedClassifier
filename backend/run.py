"""
    Run Flask application
"""
from app import app


if __name__ == '__main__':
    # load_model()
    app.run(host='0.0.0.0', port=app.config['PORT'])
