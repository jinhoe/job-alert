import smtplib
from email.message import EmailMessage
import config
from datetime import date


today = date.today()


def job_available(email_body):
    message = EmailMessage()
    message['from'] = "Job Alert <" + config.sender_email + ">"
    message['to'] = config.receiver_email
    message['subject'] = "Your job opportunities on " + today.strftime("%a, %d %b")

    body = email_body
    message.set_content(body)

    mail_server = smtplib.SMTP_SSL(config.smtp_server)
    mail_server.login(config.sender_email, config.sender_password)
    mail_server.send_message(message)
    mail_server.quit()


def job_unavailable():
    message = EmailMessage()
    message['from'] = "Job Alert <" + config.sender_email + ">"
    message['to'] = config.receiver_email
    message['subject'] = "No job opportunities on " + today.strftime("%a, %d %b")

    body = "No opportunities yet"
    message.set_content(body)

    mail_server = smtplib.SMTP_SSL(config.smtp_server)
    mail_server.login(config.sender_email, config.sender_password)
    mail_server.send_message(message)
    mail_server.quit()

