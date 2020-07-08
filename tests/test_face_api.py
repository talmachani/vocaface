from flask.testing import FlaskClient

from tests.conftest import create_valid_create_list_request_common, create_valid_create_list_request_messy


def test_face_api_return_best_image_messy_group(client: FlaskClient):
    res = client.post('/api/face', json=create_valid_create_list_request_messy()).json
    expected_image_url = "https://cms.qz.com/wp-content/uploads/2018/12/earring2.png"
    assert res["image_url"] == expected_image_url


def test_face_api_return_best_image_common_group(client: FlaskClient):
    res = client.post('/api/face', json=create_valid_create_list_request_common()).json
    expected_image_url = "https://i.pinimg.com/originals/81/02/cf/8102cfd1dfc816529efad3a8455b9c17.jpg"
    assert  res["image_url"] == expected_image_url
