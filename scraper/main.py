from scraper import get_links
import confuse

config = confuse.Configuration('HouseHunter', __name__)
pages_count = config["pages"].__iter__()


def main():
    #rynek wtorny
    url = config['pages']["page_1"]['url'].get(str)
    filename = config['pages']["page_1"]['filename'].get(str)

    f = open(filename, "w")
    f.write("")
    f.close()

    counter = 0
    is_page_last = 0
    while not bool(is_page_last):
        is_page_last = get_links.read_page(url + str(counter), filename)
        print(str(counter) + "\n")
        counter += 1


if __name__ == '__main__':
    main()