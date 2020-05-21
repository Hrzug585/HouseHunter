import bs4 as bs
import urllib.request
import time


def read_page(link, filename):
    f = open(filename, "a")
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
    time.sleep(1)
    return bool(is_last)
