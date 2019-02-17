"""
  API Endpoint for classifying dog breeds
"""

import json
import requests

from flask import Blueprint
from flask import request
from flask_restful import Api

from app.modules.classifier.api import ClassifierAPI


mod_classifier = Blueprint('classifier', __name__,
                           url_prefix='/api/classifier')
api_classifier = Api(mod_classifier)

# Register Restul API resources
api_classifier.add_resource(ClassifierAPI, '/')
