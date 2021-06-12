#!/usr/bin/env python3

import os
from PIL import Image


BASE_PATH = './supplier-data/images'

def resize_image(image: Image, width:int, height:int) -> Image:
    return image.resize((width, height))

def convert_tiff_to_jpeg(base_path:str, filename:str, resize:bool=False, width:int=0, height:int=0) -> None:

    with Image.open("{}/{}".format(base_path, filename)) as im:

        im_converted = im.convert('RGB')

        if resize:
            im_converted = resize_image(image=im_converted, width=width, height=height)

        output_name = filename.split('.')[0] + '.jpeg'

        im_converted.save("{}/{}".format(base_path, output_name), "JPEG")


if __name__ == "__main__":

    for file in os.listdir(BASE_PATH):
        if 'tiff' in file:
            convert_tiff_to_jpeg(base_path=BASE_PATH, filename=file, resize=True, width=600, height=400)
