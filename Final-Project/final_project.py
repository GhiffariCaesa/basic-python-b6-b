#https://github.com/samlopezf/Python-Email/blob/master/send_email.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from getpass import getpass

def get_email(filename):
    emails = []
    with open(filename,"r") as contacts_email:
        for contact in contacts_email:
            temp_email = contact
            temp_email = temp_email.replace('\n', '')
            emails.append(temp_email)
    return emails

# Data email
email_user = input("Masukkan emailmu : ")
email_password = getpass("Password: ")
#email_send = get_email("receiver_list.txt")
email_send = get_email("C:/Users/LENOVO/Documents/MIne/Indonesia.AI/basic-python-b6-b/Final-Project/receiver_list.txt")
subject = input("Masukkan subject email : ")
body = input("Masukkan isi dari emailmu : ")

for email in email_send:
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email
    msg['Subject'] = subject

    msg.attach(MIMEText(body,'plain'))

    #filename="download.jpg"
    filename='C:/Users/LENOVO/Documents/MIne/Indonesia.AI/basic-python-b6-b/Final-Project/download.jpg'
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    #kirim
    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,email,text)
    server.quit()
    print("Sent !")