import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import path


login_email = 'your email'
login_password = 'your password'

html = Template(path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Soubahgya pradhan'
email['to'] = 'soubahgya.developer@gmail.com'
email['subject'] = 'you own 1,000,000 dollars!'

email.set_content(html.substitute({'name':'TinTin'}))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(login_email,login_password)
    smtp.send_message(email)
    print('all good boss!')