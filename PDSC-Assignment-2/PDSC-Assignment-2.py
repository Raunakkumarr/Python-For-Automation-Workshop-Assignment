#This is the assignment of Day 2, that converts all images in this directory to pdf, attaches that pdf to the email and sends email automatically to all the recipients in emailsList.txt file.
import os
import img2pdf
import smtplib
from email.message import EmailMessage
imageFiles = [x for x in os.listdir(".") if x.endswith(".jpg") or x.endswith(".png")]
# print(imageFiles)
pdf_data = img2pdf.convert(imageFiles)
file = open("imagePDF.pdf","wb")
file.write(pdf_data)
file.close()
recepientList = []
file1 = open("emailsList.txt","r")
recepientList = [x.rstrip() for x in file1]
#print(recepientList)
for a in recepientList:
    email_id = 'kumarraunak077@gmail.com'
    pswd = os.environ.get('password')
    email = EmailMessage()
    email['Subject'] = 'Images converted to PDF by Raunak Mishra'
    email['From'] = email_id
    email['To'] = a
    email.set_content('Check the file attached with this mail !!')
    with open('imagePDF.pdf','rb') as f:
        file_data = f.read()
        file_type = 'pdf'
        file_name = f.name
        email.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename = file_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_id ,pswd)
        smtp.send_message(email)
        print("Email Sent!!")
