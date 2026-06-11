import requests


class CreatePost:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}


    def new_post(self, body, headers = None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=body,
            headers=headers
        )
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = {}


class GetPost:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}


    def get_posts(self, headers = None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            self.url,
            headers=headers
        )
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = {}

