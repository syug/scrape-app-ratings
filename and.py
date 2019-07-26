#!/usr/local/bin/python2.7
# coding: utf-8
import sys
import re
import json
import requests
from bs4 import BeautifulSoup
import emoji

def getRatingValue(url):
  responce = requests.get(url)
  soup = BeautifulSoup(responce.text, 'lxml')
  jsonldString = soup.find(name='script', attrs={'type': 'application/ld+json'})

  if jsonldString == None:
    return -1

  jsonld = json.loads(jsonldString.get_text())
  rateRaw = jsonld['aggregateRating']['ratingValue']
  return float(rateRaw)

def getResultMessage(ratingValue):
  rate = str(round(ratingValue, 1))
  rateNum = int(round(ratingValue))
  stars = []
  if rateNum < 1:
    stars.append(':cry:')
  for i in range(rateNum):
    stars.append(':star:')
  thumsup = ':sparkles: :thumbs_up: :sparkles:' if (rateNum >= 4) else ''
  return emoji.emojize('Your rating is: ' + ' '.join(stars) + ' (' + rate + ') ' + thumsup, use_aliases=True)
  # return round(float(rate), 1)

if __name__ == "__main__":
  for arg in sys.argv:
    if arg != __file__:
      print('URL: ' + arg)

      ratingValue = getRatingValue(url=arg)

      if ratingValue >= 0:
        message = getResultMessage(ratingValue=ratingValue)
      elif ratingValue == -1:
        message = emoji.emojize(':exclamation: Can not find <script type="application/ld+json"> on this URL :exclamation:', use_aliases=True)

      print(message)
