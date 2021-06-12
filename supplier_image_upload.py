#!/usr/bin/env python3

import requests
import os


def get_public_ip() -> str:
    return (requests.get('https://api.ipify.org').text).strip()

def upload_jpeg_to_server(base_path:str, filename:str) -> None:

    url = "http://{}/upload/".format(PUBLIC_IP)

    with open('{}/{}'.format(base_path, filename), 'rb') as opened:
        r = requests.post(url, files={'file': opened})


BASE_PATH = './supplier-data/images'
PUBLIC_IP = get_public_ip()

if __name__ == '__main__':

    for file in os.listdir(BASE_PATH):
        if 'jpeg' in file:
            upload_jpeg_to_server(base_path=BASE_PATH, filename=file)
