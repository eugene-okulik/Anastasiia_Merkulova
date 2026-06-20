import requests

from base_endpoint import BaseEndpoint

class GetOneObject(BaseEndpoint):
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    def get_one_object(self, post_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url}/{post_id}',
            headers=headers
        )
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = {}