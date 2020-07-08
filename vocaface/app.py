from flask import Flask
from flask_cors import CORS

from vocaface.api.face_api import face_api

# flask application initialization
app = Flask(__name__)

# cross origin resource sharing
CORS(app)

app.register_blueprint(face_api, url_prefix='/api')
