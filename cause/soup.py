from BeautifulSoup import BeautifulSoup
import requests

r = requests.get('http://en.wikipedia.org/wiki/hair loss')
wiki_soup = BeautifulSoup(r.text)

headline = wiki_soup.find(attrs={"class": "mw-headline", "id": "Causes"})
print headline

next_sib = headline.parent.nextSibling.nextSibling
print next_sib.findAll(text=True)
