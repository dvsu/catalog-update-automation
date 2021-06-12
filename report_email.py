#!/usr/bin/env python3

import os
import emails
import reports
from datetime import datetime


BASE_PATH = './supplier-data/descriptions'

if __name__ == "__main__":

    attachment = '/tmp/processed.pdf'
    # attachment = 'processed.pdf'
    title = "Processed Update on {}".format(datetime.now().strftime("%B %d, %Y"))
    paragraph = []

    for filename in os.listdir(BASE_PATH):
        header = ["name", "weight"]

        with open('{}/{}'.format(BASE_PATH, filename), 'r', encoding='utf8') as file:
            
            item_text = []
            for order, line in enumerate(file):
                # because description is not required, break from the loop after name and weight have been obtained
                if order > 1:
                    break
                item_text.append("{}: {}".format(header[order], line.strip()))
            paragraph.append(item_text)

    username = 'obtained_from_autogen' #TODO

    reports.generate_report(attachment=attachment, title=title, paragraph=paragraph)
    message = emails.generate_email(
        sender='automation@example.com', 
        receiver='{}@example.com'.format(username), 
        subject='Upload Completed - Online Fruit Store', 
        body='All fruits are uploaded to our website successfully.\nA detailed list is attached to this email.', 
        attachment=attachment)
    
    emails.send_email(message=message)
