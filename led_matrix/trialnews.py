# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 02:54:08 2020

@author: itsal
"""
import os, time, threading, random
import feedparser
from PIL import Image, ImageFont, ImageDraw
from random import shuffle

BITLY_ACCESS_TOKEN="BITLY_ACCESS_TOKEN"
items=[]
displayItems=[]
"""
feeds=[
    #enter all news feeds you want here
    "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/PressReleases/rss.xml",
    "http://www.fiercepharma.com/feed",
    "http://www.fiercebiotech.com/feed",
    ]
"""
# feeds = ["https://www.espn.com/espn/rss/news"]
feeds = ["http://www.nba.com/heat/rss.xml"]
def colorRed():
    return (255, 0, 0)

def colorGreen():
    return (0, 255, 0)

def colorBlue():
    return (0, 255, 255)

def colorRandom():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def populateItems():
    #first clear out everything
    del items[:]
    del displayItems[:]

    #delete all the image files
    os.system("find . -name \*.ppm -delete")
    for url in feeds:
        feed=feedparser.parse(url)
        posts=feed["items"]
        for post in posts:
            items.append(post)
    shuffle(items)

def createLinks():
    try:
        populateItems()
        for idx, item in enumerate(items):
            writeImage(unicode(item["title"]), idx)
    except ValueError:
        print("Bummer :( I couldn't make you 'dem links :(")
    finally:
        print("\nWill get more news next half hour!\n\n")

def writeImage(url, count):
    link, headLine="", url[:]
    def randCol(index):
        if index % 3 == 0:
            return colorRed()
        elif index % 3 == 1:
            return colorGreen()
        elif index % 3 == 2:
            return colorBlue()
        else:
            return colorRandom()
    text = ((headLine, randCol(count)), (link, colorRandom()))
    #font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 16)
    #font = ImageFont.load_default()
    font = ImageFont.truetype("StockFont.ttf", size = 32)
    all_text = ""
    for text_color_pair in text:
        t = text_color_pair[0]
        all_text = all_text + t
    width, ignore = font.getsize(all_text)
    size = width + 30, 32
    im = Image.new("RGB", size, "black")
    draw = ImageDraw.Draw(im)
    x = 0;
    for text_color_pair in text:
        t = text_color_pair[0]
        c = text_color_pair[1]
        draw.text((x, 0), t, c, font=font)
        x = x + font.getsize(t)[0]
    filename=str(count)+".ppm"
    displayItems.append(filename)
    im.save(filename)


#use json for team colors

def run():
    print("News Fetched at {}\n".format(time.ctime()))
    createLinks()
    threading.Timer(len(items) * 60, run).start()
    showOnLEDDisplay()

def showOnLEDDisplay():
    for disp in displayItems[:60]:
        os.system("sudo ./examples-api-use/demo --led-cols=64 --led-rows=32 --led-chain=1 -t 60 -m 25 -D 1 "+disp)

if __name__ == '__main__':
    run()