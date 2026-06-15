import pytest

import requests

from endpoints.create_post import CreatePost, GetPosts, GetOnePost, PutPost, PatchPost, DeletePost


@pytest.fixture
def create_post_endpoint():
    return CreatePost()


def clear(post_id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')


@pytest.fixture
def created_post(create_post_endpoint):
    body = {
        "name": "test_one",
        "data": {
            "data": {
                "test_one": "test_one"
            }
        }
    }
    create_post_endpoint.new_post(body=body)
    post_id = create_post_endpoint.json['id']
    yield post_id
    clear(post_id)


@pytest.fixture
def get_post_endpoint():
    return GetPosts()


@pytest.fixture
def get_one_post_endpoint():
    return GetOnePost()


@pytest.fixture
def put_post_endpoint():
    return PutPost()


@pytest.fixture
def patch_post_endpoint():
    return PatchPost()


@pytest.fixture
def delete_post_endpoint():
    return DeletePost()
