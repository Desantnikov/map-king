from abc import abstractmethod
import requests
import json
import unittest
import pytest

MASTER_DOMAIN = 'http://map-kings.herokuapps.com'
DEVELOPENT_DOMAIN = 'http://map-kings-development.herokuapps.com'

FUN_TYPE = type(lambda x: x)


class BaseTest(unittest.TestCase):
    def __init__(self, domain):
        super().__init__()
        self.domain = domain
        self.input, self.output = self.get_input_output()

    @abstractmethod
    def get_input_output(self):
        return None, None

    def get_input_output_pair(self):
        try:
            return self.input.pop(0), self.output.pop(0)
        except AttributeError:
            return None, None

    def post_request(self, input_data, output_data):
        url = f"{self.domain}{input_data['url']}"
        request_data = input_data['data']
        headers = input_data['headers']

        rsp = requests.post(url, data=request_data, headers=headers)
        response_data = rsp.json()

        assert rsp.status_code // 100 == 2  # 2xx - OK
        assert set(output_data.keys()) == set(response_data.keys())  # keys matched
        # all values except functions matched
        assert all([response_data[key] == value for key, value in output_data if not isinstance(value, FUN_TYPE)])
        # all functions returned True for response data
        assert all([value(response_data[key]) for key, value in output_data if isinstance(value, FUN_TYPE)])



