import bs4 as bs
import urllib.request
from urllib.error import HTTPError
import time


def read_page(link, filename):
    f = open(filename, "a")
    try:
        source = urllib.request.urlopen(link).read()
    except HTTPError as e:
        if e.code == 429:
            time.sleep(5)
            source = urllib.request.urlopen(link).read()

    soup = bs.BeautifulSoup(source, 'lxml')

    urls = soup.select('.list__item__picture a')
    for url in urls:
        output = url.get('href')
        f.write(output + "\n")
        #call page scraping here

    is_last = 1
    next_pages = soup.select('.page-step a')
    for next_page in next_pages:
        if 'ostatnia' in next_page.get('title'):
            is_last = 0

    f.close()
    return bool(is_last)
