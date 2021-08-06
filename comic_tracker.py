import comic_sites

'''
Open for refactoring in the future
This is were all logic for comic_tracker will be placed
    parse_url
    connect to db
    add and maintain list of urls and last known chapter in db
    periodically go through tracked comics in db and check for updates
    remove url from db upon request


    each comic class will house its own way of getting its chapter
    and return it.

    Compare last_known_chapter with latest_chapter and update discord
        if they differ

    alternative to running db. retrieve intial chapter upon run. 
        store values in class variable/dict
        data will not persist if bot is turned off.
'''

class ComicTracker:
    def parse_url(self, url):
        try:
            site = (url.split('/')[2]).split('.')[0]
            return site.lower().capitalize()
        except:
            print(f'Unable to parse url: {url}')

    def get_comic_class(self, site):
        try:
            class_ = getattr(comic_sites, site)
            instance = class_()

            instance.get_last_chapter()
        except:
            print(f'Unable to retrieve comic_class: {site}')



# local testing
urls = [
'https://manhuaplus.com/manga/martial-peak/',
'https://manhwatop.com/manga/fffclass-trashero',
'https://soloxleveling.com/',
'https://sololeveling.com/',
'https://flamescans.org/series/omniscient-readers-viewpoint/',
]

ct = ComicTracker()
for url in urls:
    site = ct.parse_url(url)
    ct.get_comic_class(site)