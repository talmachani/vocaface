from dataclasses import asdict

from flask import Blueprint, make_response, request

from logic.face_api_logic import FaceApiLogic

face_api = Blueprint('api', __name__, url_prefix='faces/')

face_logic = FaceApiLogic()


@face_api.route('/face', methods=['POST'])
def face_analyze():
    request_data = request.get_json()
    faces = face_logic.detect_all_faces(request_data)
    best_face = FaceApiLogic.get_biggest_face(faces)
    return make_response(asdict(best_face), 200)