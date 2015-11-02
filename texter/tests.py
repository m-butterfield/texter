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
    validate_carrier_name,
    validate_phone_number,
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
            mock.call().quit(),
        ]
        self.assertTrue(server.mock_calls == calls)


class TestValidateFunctions(unittest.TestCase):

    def test_validate_phone_number(self):
        self.assertRaises(ValueError, validate_phone_number, '123')
        self.assertRaises(ValueError, validate_phone_number, 'tenletters')

    def test_validate_carrier_name(self):
        self.assertRaises(ValueError, validate_carrier_name, 'blah')
