import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """Send GET request and return raw response text"""
        response = requests.get(self.url)
        response.raise_for_status()  # raises error if request fails
        return response.text

    def load_json(self):
        """Send GET request and return parsed JSON"""
        response = requests.get(self.url)
        response.raise_for_status()
        return response.json()
