import smtplib
import os
import imghdr
from email.message import EmailMessage

PASSWORD = os.getenv("PASSWORD")
SENDER = "billyq151515@gmail.com"
RECEIVER = "billyq151515@gmail.com"


def send_email(image_path):
    print("start email")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("sent email")

if __name__ == "__main__":
    send_email(image_path="images/19.png")

