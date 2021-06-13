from bs4 import BeautifulSoup
import urllib.request

parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
resp = urllib.request.urlopen("https://www.unisys.com/about-us/newsroom/news-release-archive?k=UnisysAssetDate%3E=2021-6-1%20AND%20UnisysAssetDate%3C=2021-6-30")
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))

for link in soup.find_all('a', href=True):
    print(link)


