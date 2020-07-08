from typing import List

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

    @staticmethod
    def get_biggest_face(faces: List[Face]) -> Face:
        return sorted(faces, key=lambda i: i.size, reverse=True)[0]
