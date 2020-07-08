import pytest
from flask.testing import FlaskClient

from vocaface import app


@pytest.fixture
def client() -> FlaskClient:
    app.app.config['TESTING'] = True
    client = app.app.test_client()
    yield client


def create_valid_create_list_request():
    return [
            {
                "url": "https://res.cloudinary.com/demo/image/upload/butterfly.jpg"
            },
            {
                "url": "https://res.cloudinary.com/demo/image/upload/docs/plain_face.jpg"
            },
            {
                "url": "https://i2-prod.mirror.co.uk/incoming/article14334083.ece/ALTERNATES/s615/3_Beautiful-girl-with-a-gentle-smile.jpg"
            },
            {
                "url": "https://cms.qz.com/wp-content/uploads/2018/12/earring2.png"
            },
            {
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Lion_waiting_in_Namibia.jpg/440px-Lion_waiting_in_Namibia.jpg"
            }

        ]
