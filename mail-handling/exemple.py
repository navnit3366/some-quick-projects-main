gmail_user = 'xxx.xxxx@gmail.com'
password = 'xxx'
liste_receivers = [
    'xxx@gmail.com',
]

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(subject, liste_receivers, corps_du_mail):

    #headers
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = gmail_user
    message["To"] = liste_receivers
    # body
    text = corps_du_mail
    part1 = MIMEText(text, "plain")
    message.attach(part1)

    with smtplib.SMTP_SSL('smtp.googlemail.com', 465) as server:

        server.login(gmail_user, password)
        server.sendmail(gmail_user, receiver, message.as_string())
