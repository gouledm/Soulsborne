class scraper:
    from urllib.request import urlretrieve
    import requests
    from bs4 import BeautifulSoup
    url="https://eldenring.wiki.fextralife.com/Astrologer"
    response = requests.get(url).text

    soup = BeautifulSoup(response, 'lxml')

    div = soup.find('p').text
    img = soup.find('td')
    img = img.find('img')
    image = img.attrs.get('src')
