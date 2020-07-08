from flask.testing import FlaskClient

from tests.conftest import create_valid_create_list_request


def test_face_api_return_best_image(client: FlaskClient):
    res = client.post('/api/face', json=create_valid_create_list_request()).json
    expected_image_url = "https://cms.qz.com/wp-content/uploads/2018/12/earring2.png"
    assert expected_image_url == res["image_url"]