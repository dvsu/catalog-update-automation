#!/usr/bin/env python3

import sys
import psutil
import threading
import emails
from time import sleep

username = 'obtained_from_autogen' #TODO
sender = 'automation@example.com'
receiver = '{}@example.com'.format(username)
body = 'Please check your system and resolve the issue as soon as possible.'

def get_cpu_load() -> float:
    return psutil.cpu_percent(interval=1)

def get_disk_percent_remaining() -> float:
    return 100.0 - (psutil.disk_usage('/').percent)

def get_available_memory() -> float:
    # in MBs (megabytes)
    return psutil.virtual_memory().available / 10**6

def localhost_check() -> bool:

    interface = psutil.net_if_addrs()['lo']

    for addr in interface:
        if addr.address == '127.0.0.1':
            return True
        
    return False

def system_health_monitoring():

    while True:
        if get_cpu_load() > 80.0:
            emails.send_email(emails.generate_error_report(
                sender=sender,
                receiver=receiver,
                subject='Error - CPU usage is over 80%',
                body=body
            ))

        if get_disk_percent_remaining() < 20.0:
            emails.send_email(emails.generate_error_report(
                sender=sender,
                receiver=receiver,
                subject='Error - Available disk space is less than 20%',
                body=body
            ))            

        if get_available_memory() < 500.0:
            emails.send_email(emails.generate_error_report(
                sender=sender,
                receiver=receiver,
                subject='Error - Available memory is less than 500MB',
                body=body
            ))

        if not localhost_check():
            emails.send_email(emails.generate_error_report(
                sender=sender,
                receiver=receiver,
                subject='Error - localhost cannot be resolved to 127.0.0.1',
                body=body
            ))            

        sleep(60)

def run():
    threading.Thread(target=system_health_monitoring, daemon=True).start()

    while True:
        try:
            sleep(10)
        except KeyboardInterrupt:
            sys.exit(1)

if __name__ == "__main__":
    run()
