import requests


def all_posts():
    response = requests.get('http://objapi.course.qa-practice.com/object').json()
    assert len(response) == 1, 'Not all posts returned'
    print(response)


def one_post():
    post_id = new_post()
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{post_id}').json()
    assert response['id'] == post_id
    print(response)
    clear(post_id)


def new_post():
    body = {
        "name": "test",
        "data": {
            "test": "test"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    )
    return response.json()["id"]


def clear(post_id):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')
    assert response.status_code in [200, 204], 'Delete failed'


def put_a_post():
    post_id = new_post()
    body = {
        "name": "new_test",
        "data": {
            "test": "new_test"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{post_id}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == "new_test"
    print(response)
    clear(post_id)


def patch_a_post():
    post_id = new_post()
    body = {
        "name": "new_test_one"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{post_id}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == "new_test_one"
    print(response)
    clear(post_id)


def delete_a_post():
    post_id = new_post()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')
    assert response.status_code in [200, 204], 'Delete failed'
    print(response.status_code)


one_post()
all_posts()
put_a_post()
patch_a_post()
delete_a_post()
