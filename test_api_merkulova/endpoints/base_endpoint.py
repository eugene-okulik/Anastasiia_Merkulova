class BaseEndpoint:
    response = None
    json = None

    def check_status_code(self, code):
        assert self.response.status_code == code
