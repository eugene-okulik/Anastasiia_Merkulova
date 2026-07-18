from locust import task, HttpUser


class GetAllObjects (HttpUser):

    @task
    def get_all_objects(self):
        self.client.get(
            '/object',
            headers={'Content-Type': 'application/json'}
        )


class GetOneObject (HttpUser):

    def on_start(self):
        body = {
            "name": "locust_test",
            "data": {
                "test": "one"
            }
        }
        response = self.client.post(
            '/object',
            json=body
        )
        self.object_id = response.json().get('id')

    @task
    def get_one_object(self):
        self.client.get(
            f'/object/{self.object_id}',
            headers={'Content-Type': 'application/json'}
        )

    def on_stop(self):
        self.client.delete(
            f'/object/{self.object_id}',
            name="/object/[id]"
        )


class PostOneObject (HttpUser):

    @task
    def create_object(self):
        body = {
            "name": "create_object",
            "data": {
                "test": "one"
            }
        }
        response = self.client.post(
            '/object',
            json=body
        )
        object_id = response.json().get('id')
        if object_id:
            self.client.delete(
                f'/object/{object_id}',
                name="/object/[id]"
            )


class PutOneObject (HttpUser):

    def on_start(self):
        body = {
            "name": "locust_test",
            "data": {
                "test": "one"
            }
        }
        response = self.client.post(
            '/object',
            json=body
        )
        self.object_id = response.json().get('id')

    @task
    def put_object(self):
        body = {
            "name": "put_name",
            "data": {
                "test": "one"
            }
        }
        self.client.put(
            f'/object/{self.object_id}',
            headers={'Content-Type': 'application/json'},
            json=body
        )

    def on_stop(self):
        self.client.delete(
            f'/object/{self.object_id}',
            name="/object/[id]"
        )


class PatchOneObject (HttpUser):

    def on_start(self):
        body = {
            "name": "locust_test",
            "data": {
                "test": "one"
            }
        }
        response = self.client.post(
            '/object',
            json=body
        )
        self.object_id = response.json().get('id')

    @task
    def patch_object(self):
        body = {
            "name": "patched_name"
        }
        self.client.patch(
            f'/object/{self.object_id}',
            headers={'Content-Type': 'application/json'},
            json=body
        )

    def on_stop(self):
        self.client.delete(
            f'/object/{self.object_id}',
            name='/object/[id]'
        )


class DeleteOneObject (HttpUser):

    @task
    def delete_object(self):
        body = {
            "name": "delete_test",
            "data": {
                'test': 'one'
            }
        }

        response = self.client.post(
            '/object',
            json=body
        )
        object_id = response.json().get('id')
        if object_id:
            self.client.delete(
                f'/object/{object_id}',
                name="/object/[id]",
            )
