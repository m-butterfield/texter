"""
Tests for instant_nostalgia

"""
import mock
import unittest

from lib import send_message, CARRIER_GATEWAYS
from settings import USER_NAME, PASSWORD, FROM_ADDRESS, SMTP_SERVER


CARRIER_NAME = 'verizon'
PHONE_NUMBER = '1234567890'
TO_EMAIL = PHONE_NUMBER + CARRIER_GATEWAYS[CARRIER_NAME]
MESSAGE = 'hello'
EXPECTED_MESSAGE = '\n' + MESSAGE


class TestSendMessage(unittest.TestCase):

    @mock.patch("lib.smtplib.SMTP")
    def test_send_message(self, server):
        send_message(PHONE_NUMBER, CARRIER_NAME, MESSAGE)
        calls = [
            mock.call(SMTP_SERVER),
            mock.call().starttls(),
            mock.call().login(USER_NAME, PASSWORD),
            mock.call().sendmail(FROM_ADDRESS, TO_EMAIL, EXPECTED_MESSAGE),
            mock.call().quit()
        ]
        self.assertTrue(server.mock_calls == calls)
