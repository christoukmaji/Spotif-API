import os, time, threading, random
import feedparser
import requests
import json
from PIL import Image, ImageFont, ImageDraw
from urllib.request import urlretrieve

BITLY_ACCESS_TOKEN="BITLY_ACCESS_TOKEN"
items=[]
displayItems=[]



def showOnLEDDisplay():
    pass
    #for disp in displayItems[:60]:
        #os.system("sudo ./examples-api-use/demo --led-cols=64 --led-rows=32 --led-chain=1 -t 60 -m 25 -D 1 "+disp)

def run():

    response = requests.get("https://api.spotify.com/v1/me/player/currently-playing")
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer BQBshVKo_qKJ2Tcf087MtOIzfkRkjdFItyLzcZ95ZQbqi8rKgZ1Yz78YOZgamgxEyw_5ZY4Tg9Sb2OuuX6sbaRUC7K26Mqyiiq4iFPiibpeDcrOXaEfRpMrF6BVFJ7coTFV0rcVk0B3JYcAybFJpxQ'
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

    os.system("sudo ./examples-api-use/demo --led-cols=64 --led-rows=32 --led-chain=1 -t 60 -m 25 -D 1 " + "my.ppm")

if __name__ == '__main__':
    run()