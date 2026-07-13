import requests

from endpoints.base_endpoint import BaseEndpoint


class PutObject(BaseEndpoint):
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    def update_object(self, body, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{object_id}',
            json=body,
            headers=headers
        )
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = {}
