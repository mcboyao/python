# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import utility
import config

logger = utility.get_logger()

default_message = Mail(
    from_email='no-reply@paralelogram.com',
    to_emails=['test@paralelogram.com'],
    subject='Default Subject',
    html_content='Default Content')


def send():
    send_message(default_message, config.SENDGRID_API_KEY)


def send_message(message, api_key):
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        logger.info('sendgrid response status code: %s', response.status_code)
        logger.debug(response.headers)
    except Exception as e:
        logger.error(e.message)


if __name__ == '__main__':
    send()
