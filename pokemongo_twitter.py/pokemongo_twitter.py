# !/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import time
import tweepy

def get_status():

    """

    :return: Online!, Unstable!, Offline!, False (No Internet Connection)
    """

    WEBSITE = "http://cmmcd.com/PokemonGo/"

    try:
        r = requests.get(WEBSITE)
        soup = BeautifulSoup(r.text, 'html.parser')
        status = soup.body.h2.font.text
    except:
        status = False

    print "The Status is: " + str(status)
    return status

def start_tweeting(every=900):
    icons = {}
    icons['online']='pokeok.png'
    icons['unstable']='pokeunstable.png'
    icons['offline']='pokedown.png'
    icons['false']='pokeinit.png'

    # YOUR INFO DOWN HERE
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_KEY = ''
    ACCESS_SECRET = ''

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    while True:
        status = get_status()
        line = ""

        if not status:
            line = "We are experiencing some server issues. :D " + " #pokemongo" + " #serverstatus"
            api.update_with_media(icons['false'], line)
        else:
            line = "Pokemon GO Servers are currently: " + status + " #pokemongo" + " #serverstatus"
            api.update_with_media(icons[status.lower().rstrip('!')], line)

        time.sleep(every)  # Tweet every 15 minutes


if __name__ == "__main__":
    start_tweeting(every=900)