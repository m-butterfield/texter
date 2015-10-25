"""
Tests for texter

"""
import mock
import unittest

from texter.lib import (
    CARRIER_GATEWAYS,
    GMAIL_EMAIL,
    GMAIL_PASSWORD,
    GMAIL_SMTP_SERVER,
    send_message,
)


CARRIER_NAME = 'verizon'
PHONE_NUMBER = '1234567890'
MESSAGE = 'hello'


class TestSendMessage(unittest.TestCase):

    @mock.patch("texter.lib.smtplib.SMTP")
    def test_send_message(self, server):
        send_message(PHONE_NUMBER, CARRIER_NAME, MESSAGE)
        expected_message = '\n' + MESSAGE
        to_email = PHONE_NUMBER + CARRIER_GATEWAYS[CARRIER_NAME]
        calls = [
            mock.call(GMAIL_SMTP_SERVER),
            mock.call().starttls(),
            mock.call().login(GMAIL_EMAIL, GMAIL_PASSWORD),
            mock.call().sendmail(GMAIL_EMAIL, to_email, expected_message),
            mock.call().quit()
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
