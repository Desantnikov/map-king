import unittest

from input_output import INPUT_OUTPUT_DICT
from base import BaseTest


class AuthTest(BaseTest):
    def test_registration(self):
        self.input_data, self.expected_output = INPUT_OUTPUT_DICT['registration'][:]
        request_type, input_data, output = self.get_request_data()
        if request_type == 'post':
            self.login_response = self.post_request(input_data, output)

    def test_login(self):
        self.input_data, self.expected_output = INPUT_OUTPUT_DICT['login'][:]
        request_type, input_data, output = self.get_request_data()
        if request_type == 'post':
            self.login_response = self.post_request(input_data, output)

    def test_jwt_access(self):
        self.input_data, self.expected_output = INPUT_OUTPUT_DICT['login'][:]
        request_type, input_data, output = self.get_request_data()
        if request_type == 'post':
            self.login_response = self.post_request(input_data, output)

        self.input_data, self.expected_output = INPUT_OUTPUT_DICT['jwt_access'][:]
        request_type, input_data, output = self.get_request_data()
        input_data.update({'headers': {'Authorization': f'Bearer {self.login_response["auth_token"]}'}})


        if request_type == 'get':
            self.get_request(input_data, output)


if __name__ == "__main__":
    unittest.main()
