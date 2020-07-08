from typing import Dict, List

from dynaconf import settings

from models import Face
from vocaface.utils.cognition_client import CognitionClient

import logging

log = logging.getLogger(__name__)


class FaceApiLogic:
    def __init__(self) -> None:
        self.cog_client = CognitionClient(settings.COGNITION_ENDPOINT, settings.COGNITION_KEY)

    def detect_all_faces(self, request_obj) -> List[Face]:
        faces = []
        for u in request_obj:
            image_url = u["url"]
            res = self.cog_client.detect(image_url)
            res_js = res.json()
            for face in res_js:

                faces.append(
                    Face(
                        image_url=image_url,
                        face_id=face["faceId"],
                        face_rectangle=face["faceRectangle"],
                        size=face["faceRectangle"]["width"] * face["faceRectangle"]["height"],
                        face_attr=face["faceAttributes"]

                    )
                )
        return faces

    def group_faces(self, faces):
        face_ids = [face.face_id for face in faces]
        res = self.cog_client.group_face(face_ids=face_ids)
        res_js = res.json()
        return res_js

    @staticmethod
    def get_best_face(faces: List[Face], groups: Dict) -> Face:
        sorted_faces = sorted(faces, key=lambda i: i.size, reverse=True)
        if groups['groups']:
            for face in sorted_faces:
                for group_face_id in groups['groups'][0]:
                    if group_face_id == face.face_id:
                        return face


        else:
            return sorted_faces[0]