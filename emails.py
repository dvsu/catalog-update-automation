import smtplib
import mimetypes
from os import path
from email.message import EmailMessage


def generate_email(sender:str, receiver:str, subject:str, body:str, attachment:str) -> EmailMessage:
    
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.set_content(body)

    attached_file = path.basename(attachment)
    mime_type, _ = mimetypes.guess_type(attachment)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment, 'rb') as attch:
        msg.add_attachment(
            attch.read(), 
            maintype=mime_type, 
            subtype=mime_subtype, 
            filename=attached_file)
    
    return msg

def generate_error_report(sender:str, receiver:str, subject:str, body:str) -> EmailMessage:

    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.set_content(body)

    return msg
    
def send_email(message:EmailMessage) -> None:
    server = smtplib.SMTP('localhost')
    server.send_message(message)
    server.quit()
