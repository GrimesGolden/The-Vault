import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        url = self.site
        r = urllib.request.urlopen(self.site)
        html = r.read()
        content = BeautifulSoup(html, "html.parser")
        content = content.findAll('', attrs={'class': 'title'})
        for headline in content:
            if 'iran' in str(headline):
                print(headline)
                print('\n')
         
ol_scrapey = Scraper('http://foxnews.com')
ol_scrapey.scrape()
