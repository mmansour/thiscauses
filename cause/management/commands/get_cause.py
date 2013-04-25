from django.core.management.base import BaseCommand, CommandError
from BeautifulSoup import BeautifulSoup
import urllib2
import datetime
import pprint
from math import ceil
import time
import requests

class Command(BaseCommand):
    help = 'Get REA'
    def handle(self, *args, **options):
        r = requests.get('http://en.wikipedia.org/wiki/Lung_cancer')
        causesoup=BeautifulSoup(r.text)
        print causesoup.prettify()











        


  