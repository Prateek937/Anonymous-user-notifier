import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders, message
from typing import Sequence

# pip install python-decouple
from decouple import config

'''
For creating and using Environment varibales you can use decouple module.
$ pip install python-decouple

Once installed, create a ".env" file in the root of your project which you can then open up to add your environment variables.
$ touch .env   # create a new .env file
$ nano .env    # open the .env file in the nano text editor

You can then add your environment variables like this:

USER=alex
PASS=hfy92kadHgkk29fahjsu3j922v9sjwaucahf

For accessing them use the below example:

from decouple import config

USERNAME = config('USER')
PASS = config('PASS')
'''


# Function to send Email
def sendEmail(attachment):
    #Sender, Reciever, Body of Email
    sender = config('SENDER')
    password = config('PASSWORD')
    receiver = config('RECIEVER')

    #Creating the Message, Subject line, From and To
    msg = MIMEMultipart()
    msg['Subject'] = 'Hello Prateek! This is your face.'
    msg['From'] = sender
    msg['To'] = receiver

    #Adds a csv file as an attachment to the email 
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attachment, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename = Prateek.jpg')
    msg.attach(part)

    #Connecting to Gmail SMTP Server
    s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
    s.login(user = sender, password = password)
    s.sendmail(sender, receiver, msg.as_string())
    print("Mailed successfully!")
    s.quit()

