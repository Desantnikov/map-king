import unittest

import requests

MASTER_DOMAIN = 'http://map-kings.herokuapp.com'
DEVELOPENT_DOMAIN = 'http://map-kings-development.herokuapp.com'


class BaseTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.domain = DEVELOPENT_DOMAIN
        unittest.TestCase.__init__(self, *args, **kwargs)

    def get_request_data(self, step=0):
        request_type, request_data = self.input_data[step] # ref before assignment
        expected_response = self.expected_output[step]

        return request_type, request_data, expected_response

    def post_request(self, input_data, output_data):
        url = f"{self.domain}{input_data['url']}"
        request_data = input_data['data']
        headers = input_data['headers']

        rsp = requests.post(url, data=request_data, headers=headers)
        response_data = rsp.json()

        self.assertTrue(199 < rsp.status_code < 300, 'Not 2xx code -> not ok')

        for exp_item, act_item in zip(output_data.items(), response_data.items()):
            self.assertTupleEqual(exp_item, act_item)

        return response_data

    def get_request(self, input_data, output_data):
        url = f"{self.domain}{input_data['url']}"
        headers = input_data['headers']

        rsp = requests.get(url, headers=headers)
        if not isinstance(output_data, dict):
            response_data = rsp.text
            self.assertEqual(output_data, response_data)
        else:
            response_data = rsp.json()
            for exp_item, act_item in zip(output_data.items(), response_data.items()):
                self.assertTupleEqual(exp_item, act_item)

        self.assertTrue(199 < rsp.status_code < 300, 'Not 2xx code -> not ok')



        return response_data
