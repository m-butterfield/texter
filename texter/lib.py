"""
lib for texter

"""
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

FROM_ADDRESS = 'texter@mattbutterfield.com'
SMTP_SERVER = 'localhost'


def send_message(phone_number,
                 carrier_name,
                 message,
                 from_address=FROM_ADDRESS):
    """
    Send a message to the given phone_number.

    Args:
        phone_number (str): The 10 digit phone number to send to.
        carrier_name (str): Name of the carrier the phone number is on.
        message (str): The message to send.

    Kwargs:
        from_address (str): The address the text will be sent from

    """
    _validate_phone_number(phone_number)
    carrier_gateway = _validate_carrier_gateway(carrier_name)

    to_address = phone_number + carrier_gateway
    message = '\n' + message
    smtp = smtplib.SMTP(SMTP_SERVER)
    smtp.sendmail(from_address, to_address, message)


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
