from email.message import EmailMessage
import smtplib
import os
import imghdr
#authlogin
username = os.environ.get('mymail')
password = os.environ.get('mypass')
def sendEmail(files=[],to='shubharthakofficial@gmail.com', content='This person is not wearing mask'):
    msg = EmailMessage()
    msg['Subject'] = 'Mail From Face Mask Detection'
    msg['From'] = username
    msg['To'] = to
    msg.set_content(content)
    for file in files:
        with open (file, 'rb') as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name
            
        msg.add_attachment(file_data, maintype='image', subtype=file_type,filename=file_name)
        print('Email Have been sent!!')
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(username, password)
        smtp.send_message(msg)
        
#sendEmail(input('Enter the sending email: '), input('Enter the message: '))
sendEmail()
