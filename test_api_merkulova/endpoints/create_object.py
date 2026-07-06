import requests

from endpoints.base_endpoint import BaseEndpoint


class CreateObject(BaseEndpoint):
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    def new_object(self, body, headers=None):
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
