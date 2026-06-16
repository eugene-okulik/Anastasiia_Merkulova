import pytest

import requests

from endpoints.create_object import CreateObject
from endpoints.get_objects import GetObjects
from endpoints.get_one_object import GetOneObject
from endpoints.patch_object import PatchObject
from endpoints.put_object import PutObject
from endpoints.delete_object import DeleteObject


@pytest.fixture
def create_object_endpoint():
    return CreateObject()


def clear(post_id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')


@pytest.fixture
def created_object(create_object_endpoint):
    body = {
        "name": "test_one",
        "data": {
            "data": {
                "test_one": "test_one"
            }
        }
    }
    create_object_endpoint.new_object(body=body)
    post_id = create_object_endpoint.json['id']
    yield post_id
    clear(post_id)


@pytest.fixture
def get_objects_endpoint():
    return GetObjects()


@pytest.fixture
def get_one_object_endpoint():
    return GetOneObject()


@pytest.fixture
def put_object_endpoint():
    return PutObject()


@pytest.fixture
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture
def delete_object_endpoint():
    return DeleteObject()
