import smtplib
import ssl
import os


def send_email(receiver, message):
    host = "smtp.gmail.com"
    port = 465

    username = "billyq151515@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = receiver
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)