from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

#define some variables
email_sender = "olarinre.ayobami02@gmail.com"
email_password = password
email_reciever ="olarinre.ayobami00@gmail.com" #try this out with a temp mail
subject = "SUBJECT OF THE MAIL"

body = ''' this is me trying out how to send an email in python
            using python email server'''

#create an intsance of email message.
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject

em.set_content(body) #sets the email message body

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465, context = context) as smtp:
    smtp.login(email_sender, email_password) # authentcates the mail sender
    smtp.sendmail(email_sender, email_reciever, em.as_string()) # finaaly send the mail.




