class scraper:
    def scrapeImage(self, link):
        from urllib.request import urlretrieve
        import requests
        from bs4 import BeautifulSoup
        url= link
        response = requests.get(url).text

        soup = BeautifulSoup(response, 'lxml')
        img = soup.find('td')
        img = img.find('img')
        image = img.attrs.get('src')
        return image

    def scrapeP(self, link):
        from urllib.request import urlretrieve
        import requests
        from bs4 import BeautifulSoup
        url= link
        response = requests.get(url).text

        soup = BeautifulSoup(response, 'lxml')

        p = soup.find('p').text
        return p

