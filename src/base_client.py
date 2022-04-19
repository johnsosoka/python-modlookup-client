import requests

class BaseClient:

    def __init__(self):
        self.base_url = 'https://modlookup.3v.fi/api'
        self.headers = {'User-Agent': 'python-modlookup-client / Version: 0.0.1 / URL: https://github.com/johnsosoka/python-modlookup-client'}

    def get_request(self, path):
        request_url = '{base_url}{path}'.format(base_url=self.base_url,
                                                path=path)
        response = requests.get(request_url, headers=self.headers)
        return response.text

