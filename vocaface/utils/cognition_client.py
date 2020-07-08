import json
import logging
from typing import List
from urllib.parse import urljoin

import requests
from requests import HTTPError

log = logging.getLogger(__name__)


def clean_empty(d):
    if not isinstance(d, (dict, list)):
        return d
    if isinstance(d, list):
        return [v for v in (clean_empty(v) for v in d) if v]
    return {k: v for k, v in ((k, clean_empty(v)) for k, v in d.items()) if v}


class CognitionClient:
    def __init__(self, endpoint, subscription_key):
        self.endpoint = urljoin(endpoint, "/face/v1.0/")
        self.subscription_key = subscription_key
        self.r = requests.Session()
        self.r.headers.update(self._get_headers())

    def _get_headers(self):
        return {
            # Request headers
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': self.subscription_key,
        }

    def detect(self, image_url):
        url = urljoin(self.endpoint, "detect")
        params = {"returnFaceAttributes": "age,gender"}
        data = {"url": image_url}
        return self._make_call("POST", url, params=params, data=data)

    def create_face_list(self, list_id, name, user_data=None, recognition_model="recognition_02"):
        url = urljoin(self.endpoint, f"facelists/{list_id}")
        data = {"name": name,
                "userData": user_data,
                "recognitionModel": recognition_model
                }

        return self._make_call("PUT", url, data=data)

    def add_to_face_list(self, list_id, image_url):
        url = urljoin(self.endpoint, f"facelists/{list_id}/persistedFaces")
        data = {"url": image_url}
        return self._make_call("POST", url, data=data)

    def find_similar(self, list_id):
        url = urljoin(self.endpoint, "findsimilars")
        data = {"faceListId": list_id}
        return self._make_call("POST", url, data=data)

    def get_list_faces(self, list_id):
        url = urljoin(self.endpoint, f"facelists/{list_id}")
        return self._make_call("GET", url)

    def group_face(self, face_ids: List[str]):
        url = urljoin(self.endpoint, "group")
        data = {
            "faceIds": face_ids
        }
        return self._make_call("POST", url, data=data)

    def _make_call(self, method, url, params=None, data=None):
        try:
            if data:
                data = json.dumps(clean_empty(data))
            response = self.r.request(method, url, params, data=data)
            response.raise_for_status()
        except HTTPError as e:
            log.exception(e)
            raise e
        return response
