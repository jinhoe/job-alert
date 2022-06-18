import smtplib
from email.message import EmailMessage
import config
from datetime import date


today = date.today()


def curated_job(subject, email_body):
    message = EmailMessage()
    message['from'] = "Job Alert <" + config.sender_email + ">"
    message['to'] = config.receiver_email
    message['subject'] = f"{subject}" + today.strftime("%a, %d %b")

    body = f"{email_body}"
    message.set_content(body)

    mail_server = smtplib.SMTP_SSL(config.smtp_server)
    mail_server.login(config.sender_email, config.sender_password)
    mail_server.send_message(message)
    mail_server.quit()

