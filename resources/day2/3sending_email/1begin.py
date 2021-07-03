#This basic code sends automatic emails using TLS encryption to a recipient just in text.
import os
import smtplib   #inbuilt

email_add = 'your_email_here'
passwd_pass  = 'your_password_here'

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login( email_add , passwd_pass)

    subject = 'hello'
    body = 'how you doing?'

    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(email_add , 'pdsc.nepal@gmail.com', msg)
