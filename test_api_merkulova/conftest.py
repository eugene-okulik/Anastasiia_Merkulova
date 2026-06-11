import pytest

import requests

from endpoints.create_post import CreatePost, GetPost


@pytest.fixture
def create_post_endpoint():
    return CreatePost()


def clear(post_id):
    requests.delete(f'https://api.course.qa-practice.com/v1/posts/{post_id}')


@pytest.fixture
def created_post(create_post_endpoint):
    body = {
        "name" : "test_one",
        "data" : {
            "data" : {
                "test_one" : "test_one"
            }
        }
    }
    create_post_endpoint.new_post(body=body)
    post_id = create_post_endpoint.json['id']
    yield post_id
    clear(post_id)


@pytest.fixture
def get_post_endpoint():
    return GetPost()



