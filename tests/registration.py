from tests.base import BaseTest
from tests.input_output import REGISTRATION_CHECK_INPUT, REGISTRATION_CHECK_OUTPUT


class RegistrationTest(BaseTest):
    def get_input_output(self):
        return REGISTRATION_CHECK_INPUT, REGISTRATION_CHECK_OUTPUT

    def test_case_0(self):
        self.post_request(self.get_input_output_pair())
