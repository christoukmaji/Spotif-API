import os, time, threading, random
import feedparser
import requests
import json
from PIL import Image, ImageFont, ImageDraw
from urllib.request import urlretrieve
import subprocess


OAuth_Key = "REPLACE KEY HERE"
# ex: Bearer BQBwaT5baOQQ8yGlr_OH4fpFC_OZ4dfsdfsdK9d8UGRSx912bxfascAVPzM12YSMAlqT-_jNXVtd

def run():

    while True:
        response = requests.get("https://api.spotify.com/v1/me/player/currently-playing")
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': OAuth_Key'
        }

        params = (
            ('market', 'ES'),
        )

        response = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers, params=params)


        y = response.json()
        link = y['item']['album']['images'][0]['url']
        urlretrieve(link,"temp.jpg")

        album = Image.open("temp.jpg")

        album = album.resize((32,32))
        album.save("my.ppm")


        os.system("sudo ./utils/led-image-viewer my.ppm -C --led-cols=64 --led-rows=32 --led-brightness=50 --led-slowdown-gpio=0 --led-chain=2 --led-pixel-mapper='U-mapper'")


if __name__ == '__main__':
    run()