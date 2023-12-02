import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path


#######un programme pour envoyer un mail using outlook
#https://www.codeforests.com/2020/06/05/how-to-send-email-from-outlook/
#pip install pywin32
def way1():
    import win32com.client  # as admin !! àa vient de pywin32
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'contact@company.com'
    mail.Subject = 'Sample Email'
    mail.HTMLBody = '<h3>This is HTML Body</h3>'
    mail.Body = "This is the normal body"
    #mail.Attachments.Add('c:\\sample.xlsx')
    #mail.Attachments.Add('c:\\sample2.xlsx')
    mail.CC = 'somebody@company.com'
    mail.Send()


my_mail = 'xxxxxxxx@gmail.com'
passw = '*********************'

#another one

#des setups
'''
#got on 
    - https://stackoverflow.com/questions/26852128/smtpauthenticationerror-when-sending-mail-using-gmail-and-python
    - https://stackoverflow.com/questions/54657006/smtpauthenticationerror-5-7-14-please-log-n5-7-14-in-via-your-web-browser/56809076#56809076

#un mail doit être venu pour suspicious attemp: va dire c'est moi (ou va directement sur (https://myaccount.google.com/security) to do it
#https://accounts.google.com/b/0/DisplayUnlockCaptcha
#donner aces a des app tiers ::https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4Msp1oiXQ1arZcID_n5fAP4BdYw_kaqWdzLIrOjsjk-6aU_VVM9QaxtGqfeM5cN1vj4Wgpe3W2TYyzCh6d62KWE3Us6hw

'''

#comme,nt de ppala ::https://stackoverflow.com/questions/26852128/smtpauthenticationerror-when-sending-mail-using-gmail-and-python
#https://realpython.com/python-send-email/
#Using SMTP_SSL()
'''
Au premier usage, on recoit un mail: il faut diee que c'etait moi. En plus, il faut accepter le app moins sécurisés à se logger. Sinon, on est bloque
'''

gmail_user = 'xxxxxxxx@gmail.com'
password = '********************'

port = 465  # For SSL
receiver = 'xxxxxxxx@gmail.com'
receiver = 'xxxxxxxx@company.com'
subject = 'subject set'
test_num = 2
message_plain = str(test_num) + ': test from code '

html_text = """\
<html>
  <body>
    <p>Hi,
       How are you ?<br>
       up<br>
       <a href="http://www.realpython.com">Real Python</a> <br>
       has many great tutorials.<br>
    </p>
  </body>
</html>
"""


def way3():

    #headers
    message = MIMEMultipart("alternative")
    message["Subject"] = subject + '1'
    message["From"] = gmail_user
    message["To"] = receiver

    # body
    #cas du plain text
    text = message_plain + '2'
    part1 = MIMEText(text, "plain")
    message.attach(part1)

    #cas du html: il override les precedents car c'est le denier attach qui est considéré
    html = html_text
    part2 = MIMEText(html, "html")
    message.attach(part2)

    with smtplib.SMTP_SSL('smtp.googlemail.com', port) as server:

        server.login(gmail_user, password)
        server.sendmail(gmail_user, receiver, message.as_string())
        print('mail 1 envoyé')


def way4():
    # Create a secure SSL context
    context = ssl.create_default_context()

    #headers
    message = MIMEMultipart("alternative")
    message["Subject"] = subject + '21'
    message["From"] = gmail_user
    message["To"] = receiver

    # body
    #cas du plain text
    text = message_plain + '2'
    part1 = MIMEText(text, "plain")
    message.attach(part1)

    #cas du html: il override les precedents car c'est le denier attach qui est considéré
    html = html_text
    part2 = MIMEText(html, "html")
    message.attach(part2)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(gmail_user, password)
        #message = """\
        #Subject: {} \n\n{}""".format(subject,message_plain+'2')
        server.sendmail(gmail_user, receiver, message.as_string())
        print('mail 2 envoyé')

        # TODO: Send email here


###https://developers.google.com/gmail/api/guides/sending#python
#Using .starttls() for office 365
def way5():
    # Create a secure SSL context
    context = ssl.create_default_context()

    receiver = 'xxxxxxxx@gmail.com'

    liste_reception = ['xxxxxxxx@gmail.com', 'xxxxxxxx2@gmail.com']
    receiver = ';'.join(liste_reception)
    gmail_user = 'xxxxxxxx@company.com'
    password = '******************'

    #headers
    message = MIMEMultipart("alternative")
    message["Subject"] = subject + '3'
    message["From"] = gmail_user
    message["To"] = receiver

    # body
    #cas du plain text
    text = message_plain + '3'
    part1 = MIMEText(text, "plain")
    message.attach(part1)

    #cas du html: il override les precedents car c'est le denier attach qui est considéré
    html = html_text
    part2 = MIMEText(html, "html")
    message.attach(part2)

    with smtplib.SMTP('smtp.office365.com', 587) as server:
        server.ehlo()
        server.starttls()
        server.login(gmail_user, password)
        #message = """\
        #Subject: {} \n\n{}""".format(subject,message_plain+'2')
        server.sendmail(gmail_user, receiver, message.as_string())
        print('mail 3 envoyé')

        # TODO: Send email here
