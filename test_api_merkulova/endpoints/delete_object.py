import requests

from base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {'Content-Type': 'application/json'}

    def delete_object(self, post_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/{post_id}',
            headers=headers
        )
        try:
            self.json = self.response.json()
        except ValueError:
            self.json = {}