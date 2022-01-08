import os
import requests

import pytest


def get_test_cases():
    return [x for x in os.walk('lfw') if len(x[2]) > 1][:10]


def upload_test_cases():
    dataset = [(os.path.basename(x[0]), x[2][0], open(os.path.join(x[0], x[2][0]), 'rb')) for x in get_test_cases()]
    return dataset


@pytest.mark.parametrize("name,file_name,photo", upload_test_cases())
def test_upload(name, file_name,photo):
    r = requests.post('http://127.0.0.1:8000/uploadphoto/', params={'name': name}, files={'photo': photo})
    ar = r.json()['upload_result']
    assert f"person {name} with photo {file_name} uploaded" == ar

