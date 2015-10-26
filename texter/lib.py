"""
lib for texter

"""
import os
import smtplib


CARRIER_GATEWAYS = {
    "at&t": "@txt.att.net",
    "cricket": "@mms.cricketwireless.net",
    "sprint": "@pm.sprint.com",
    "t-mobile": "@tmomail.net",
    "u.s. cellular": "@email.uscc.net",
    "verizon": "@vtext.com",
    "virgin": "@vmobl.com",
}

GMAIL_SMTP_SERVER = 'smtp.gmail.com:587'
GMAIL_EMAIL = os.getenv('GMAIL_EMAIL')
GMAIL_PASSWORD = os.getenv('GMAIL_PASSWORD')


def send_message(phone_number, carrier_name, message):
    """
    Send a message to the given phone_number.

    Args:
        phone_number (str): The 10 digit phone number to send to.
        carrier_name (str): Name of the carrier the phone number is on.
        message (str): The message to send.

    """
    _validate_phone_number(phone_number)
    carrier_gateway = _validate_carrier_gateway(carrier_name)
    to_address = phone_number + carrier_gateway
    message = '\n' + message
    _send_message(to_address, message)


def _send_message(to_address, message):
    smtp = smtplib.SMTP(GMAIL_SMTP_SERVER)
    smtp.starttls()
    smtp.login(GMAIL_EMAIL, GMAIL_PASSWORD)
    smtp.sendmail(GMAIL_EMAIL, to_address, message)
    smtp.quit()


def _validate_phone_number(phone_number):
    error_message = ("Please provide your phone number as 10 digits only. (No "
                     "punctuation, letters or spaces)")
    if len(phone_number) != 10:
        raise ValueError(error_message)
    try:
        int(phone_number)
    except ValueError:
        raise ValueError(error_message)


def _validate_carrier_gateway(carrier_name):
    if carrier_name not in CARRIER_GATEWAYS:
        carrier_names = ', '.join(CARRIER_GATEWAYS.keys())
        raise ValueError(
            "Invalid carrier name.  Valid carrier names are: " + carrier_names)
    return CARRIER_GATEWAYS[carrier_name]
