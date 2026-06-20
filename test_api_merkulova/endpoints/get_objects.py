import requests

from base_endpoint import BaseEndpoint

class GetObjects(BaseEndpoint):
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    def get_objects(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            self.url,
            headers=headers
        )
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = {}