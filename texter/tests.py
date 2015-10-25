"""
Tests for texter

"""
import mock
import unittest

from texter.lib import (
    CARRIER_GATEWAYS,
    FROM_ADDRESS,
    send_message,
    SMTP_SERVER,
)


CARRIER_NAME = 'verizon'
PHONE_NUMBER = '1234567890'
MESSAGE = 'hello'


class TestSendMessage(unittest.TestCase):

    @mock.patch("texter.lib.smtplib.SMTP")
    def test_send_message(self, server):
        send_message(PHONE_NUMBER, CARRIER_NAME, MESSAGE)
        self._check_send_message(server)

    @mock.patch("texter.lib.smtplib.SMTP")
    def test_specify_from_address(self, server):
        new_from_address = 'bob@aol.com'
        send_message(PHONE_NUMBER, CARRIER_NAME, MESSAGE, new_from_address)
        self._check_send_message(server, new_from_address)

    def _check_send_message(self, server, from_address=FROM_ADDRESS):
        expected_message = '\n' + MESSAGE
        to_email = PHONE_NUMBER + CARRIER_GATEWAYS[CARRIER_NAME]
        calls = [
            mock.call(SMTP_SERVER),
            mock.call().sendmail(from_address, to_email, expected_message),
        ]
        self.assertTrue(server.mock_calls == calls)

    def test_invalid_phone_numbers(self):
        self.assertRaises(
            ValueError, send_message, '123', CARRIER_NAME, MESSAGE)
        self.assertRaises(
            ValueError, send_message, 'tenletters', CARRIER_NAME, MESSAGE)

    def test_invalid_carrier_name(self):
        self.assertRaises(
            ValueError, send_message, PHONE_NUMBER, 'blah', MESSAGE)
