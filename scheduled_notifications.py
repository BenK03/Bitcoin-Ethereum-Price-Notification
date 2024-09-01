import smtplib
from email.message import EmailMessage

def email_notification(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    
    user = 'BTC.ETH.notification@gmail.com'
    msg['from'] = user
    password = 'uwmu ocsu bwej ioao'
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

