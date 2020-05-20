import tut_scrape as scraper
import confuse

config = confuse.Configuration('HouseHunter', __name__)
pages_count = config["pages"].__iter__()


def main():
    for i in pages_count:
        url = config['pages'][str(i)]['url'].get(str)
        filename = config['pages'][str(i)]['filename'].get(str)
        # print("url: " + url)
        # print("filename: " + filename)
        f = open(filename, "w")
        f.write("")
        f.close()

        counter = 0
        is_page_last = 0
        while not bool(is_page_last):
            is_page_last = scraper.read_page(url + str(counter), filename)
            print(str(counter) + "\n")
            counter += 1


if __name__ == '__main__':
    main()
