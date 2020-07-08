import pytest
from flask.testing import FlaskClient

from vocaface import app


@pytest.fixture
def client() -> FlaskClient:
    app.app.config['TESTING'] = True
    client = app.app.test_client()
    yield client


def create_valid_create_list_request_messy():
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


def create_valid_create_list_request_common():
    return [
        {
            "url": "https://i.pinimg.com/originals/d2/cf/77/d2cf77af37ad9690c60d80b76a8c7a1f.jpg"
        },
        {
            "url": "https://i.pinimg.com/564x/a2/70/e7/a270e76afbc8a703bb6e2a5273fc2cc7.jpg"
        },
        {
            "url": "https://awoiaf.westeros.org/images/a/a0/Cristi_Balanescu_Jon_SnowGhost.png"
        },
        {
            "url": "https://i.pinimg.com/originals/81/02/cf/8102cfd1dfc816529efad3a8455b9c17.jpg"
        },

    ]
