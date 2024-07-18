import requests

from notes_app import endpoints


class API:
    def post_req(self, endpoint, payload):
        url = f"{endpoints['base_url']}{endpoints[endpoint]}"
        request = requests.post(url, payload)
        return request

    def get_req(self, endpoint):
        request = requests.get(endpoint)
        return request

    def put_req(self, endpoint, payload):
        request = requests.put(endpoint, payload)
        return request
