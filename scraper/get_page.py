import bs4 as bs
import urllib.request
import json


def set_description(soup, selector):
    description = ""
    for i in soup.select(str(selector)):
        description += i.text
    return description


def set_additional_info(soup, selector):
    additional_info = []
    for i in soup.select(str(selector)):
        additional_info.append(i.string)
    return additional_info


def set_images_links(soup, selector):
    images_links = []
    for i in soup.select(str(selector)):
        images_links.append(i["src"])
    return images_links


class Page:
    def __init__(self, link, selectors):
        source = urllib.request.urlopen(link).read()
        soup = bs.BeautifulSoup(source, "lxml")

        self.link = link
        self.address = soup.select(str(selectors["address"]))[0].text
        self.price = soup.select(str(selectors["price"]))[0].text
        self.area = soup.select(str(selectors["area"]))[0].text
        self.floor_no = soup.select(str(selectors["floor_no"]))[0].text
        self.no_of_rooms = soup.select(str(selectors["no_of_rooms"]))[0].text
        self.no_of_floors_in_building = soup.select(str(selectors["no_of_floors_in_building"]))[0].text
        self.offer_id = soup.select(str(selectors["offer_id"]))[0].text
        self.description = set_description(soup, selectors["description"])
        self.additional_info = set_additional_info(soup, selectors["additional_info"])
        self.images_links = set_images_links(soup, selectors["images_links"])


def get_json(self):
    return json.dumps(self, ensure_ascii=False, default=lambda x: x.__dict__)
