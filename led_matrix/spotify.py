import os, time, threading, random
import feedparser
import requests
import json
from PIL import Image, ImageFont, ImageDraw
from urllib.request import urlretrieve
import subprocess

BITLY_ACCESS_TOKEN="BITLY_ACCESS_TOKEN"
items=[]
displayItems=[]



def showOnLEDDisplay():
    pass
    #for disp in displayItems[:60]:
        #os.system("sudo ./examples-api-use/demo --led-cols=64 --led-rows=32 --led-chain=1 -t 60 -m 25 -D 1 "+disp)

def run():
    link_temp = ""
    while True:
        response = requests.get("https://api.spotify.com/v1/me/player/currently-playing")
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer BQBwaT5baICyAFDOQQ8yGlr_OH4fpFC_OZ4KN228jrIAMf9d8UGRSxmPRTozAVPzM12YSMAlqT-_jNXVtdDqbARdKUn6OMkTTCZgn4TN90sKrHCU4ONidWmfpNA9RzvgLFx9ohKiMsaLnhF4YN-Ezw'
        }

        params = (
            ('market', 'ES'),
        )

        response = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers, params=params)

        # NB. Original query string below. It seems impossible to parse and
        # reproduce query strings 100% accurately so the one below is given
        # in case the reproduced version is not "correct".
        # response = requests.get('https://api.spotify.com/v1/me/player/currently-playing?market=ES', headers=headers)
        #print(response.json())
        y = response.json()
        link = y['item']['album']['images'][0]['url']
        urlretrieve(link,"temp.jpg")

        album = Image.open("temp.jpg")

        #im = Image.new("RGB",(32,32),"black")
        #draw = ImageDraw.Draw(album)
        album = album.resize((32,32))
        album.save("my.ppm")

        #os.system("sudo ./examples-api-use/demo --led-cols=64 --led-rows=32 --led-chain=1 -t 60 -m 25 -D 1 " + "my.ppm")

        os.system("sudo ./demo -D 6 --led-cols=64 --led-rows=32 --led-brightness=50 --led-slowdown-gpio=0 --led-chain=2 --led-pixel-mapper='U-mapper'")

       # subprocess.call(["sudo", "./utils/led-image-viewer", "my.ppm", "-C", "--led-cols=64", "--led-rows=32"])

        #if link changes
        #if link_temp == link:
            #pass
        #else:
            #link_temp = link
            #subprocess.call(["sudo", "./utils/led-image-viewer", "my.ppm", "-C", "--led-cols=64", "--led-rows=32"])
            #kill

if __name__ == '__main__':
    run()