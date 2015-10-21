"""
lib for instant_nostalgia

"""
import smtplib

from settings import USER_NAME, PASSWORD, FROM_ADDRESS, SMTP_SERVER


TO_ADDRESS_SUFFIX = '@vtext.com'


def send_message(phone_number, message):
    to_address = phone_number + TO_ADDRESS_SUFFIX
    message = '\n' + message
    server = smtplib.SMTP(SMTP_SERVER)
    server.starttls()
    server.login(USER_NAME, PASSWORD)
    print "SENDING: {} TO: {}".format(message, to_address)
    server.sendmail(FROM_ADDRESS, to_address, message)
    server.quit()
