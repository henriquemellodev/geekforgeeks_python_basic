import requests
import xml.etree.ElementTree as ET

# url de noticias rss feed
RSS_FEED_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

def loadRSS():
  resp = requests.get(RSS_FEED_URL)
  return resp.content

def parseXML(rss):
  root = ET.fromstring(rss)
  
  newitens = []
  
  for item in root.findall('./channel/item'):
    news = []
    for child in item:
      if child.tag == '{http://search.yahoo.com/mrss/}content':
        news['media'] = child.attrib['url']
      else:
        news[child.tag] = child.text.encode('utf8')
    newitens.append(news)
  
  return newitens

def topStories():
  rss = loadRSS()
  
  newsitems = parseXML(rss)
  
  return newsitems