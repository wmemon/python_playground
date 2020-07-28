import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

content = Template(Path('plain-text.html').read_text(encoding='utf-8'))
email = EmailMessage()
email['from'] = 'Wasim Memon'
email['to'] = 'wmemon579@gmail.com'
email['subject'] = 'Test last in the afternoon.'
email.set_content(content.substitute({'firstname': 'Wasim'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('memwasim00@gmail.com','Wasim@123')
    smtp.send_message(email)
    smtp.close()