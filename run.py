#! /usr/bin/env python3

import os
import requests


def get_public_ip() -> str:
    return (requests.get('https://api.ipify.org').text).strip()

def get_item_description(base_path:str, filename:str) -> dict:

    with open('{}/{}'.format(base_path, filename), 'r', encoding="utf8") as file:
            
        header = ["name", "weight", "description"]

        data = {}
        for order, line in enumerate(file):
            # In case the line contains no text, skip and check the next line
            if line == '\n':
                continue

            if header[order] == "weight":
                data[header[order]] = int(line.split(' ')[0])
            else:
                data[header[order]] = line.strip()

        data["image_name"] = filename.replace('txt', 'jpeg')

        return data

def upload_description(data:dict) -> None:
    response = requests.post('http://{}/fruits/'.format(PUBLIC_IP), json=data)
    # print(response.status_code)


BASE_PATH = './supplier-data/descriptions'
PUBLIC_IP = get_public_ip()

if __name__ == "__main__":

    for filename in os.listdir(BASE_PATH):
        item_desc = get_item_description(base_path=BASE_PATH, filename=filename)
        upload_description(data=item_desc)
