import comic_sites
import pymongo
from pymongo import MongoClient
import time
import urllib

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
    def __init__(self):
        self.last_chapter = None
        self.stored_chapter = None
        self.site = None
        self.url = None

    def track_comic(self, url):
        self.parse_url(url)
        # add url to db
        self.insert_url_info_db(self.url, self.last_chapter)



    def parse_url(self, url):
        try:
            self.url = url
            site = (url.split('/')[2]).split('.')[0]
            self.site = site.lower().capitalize()
            
        except:
            print(f'Unable to parse url: {url}')


    def retrieve_comic_list(self):
        #grab list of comics from db
        # {comic: {comic_name:'name', url: 'url', stored_chapter: 'chapter-1'}}
        pass


    def get_comic(self, site):
        try:
            class_ = getattr(comic_sites, site)
            comic = class_(self.url)
            return comic
        except:
            print(f'Unable to retrieve comic: {site}')

    def check_for_update(self):
        #try:
        comic = self.get_comic(self.site)
        last_chapter = comic.get_last_chapter(self.url)
        stored_chapter = 'chapter-144' #retrieve from db

        print(f'Stored Chapter: {stored_chapter}')
        print(f'Last chapter: {last_chapter}')
        if last_chapter != stored_chapter:
            print(f'{comic.comic_name}: New chapter out!')
        else:
            print(f'{comic.comic_name}: No updates...')
        #except:
        #    print('Unable to get updates')



    def insert_url_info_db(self, site_url, latest_chapter):
        print('inserting url info...')
        time.sleep(2)

        collection = self.get_db()


        ping_cm = {
            'comic': 
            {
                'url': site_url,
                'latest_chapter': latest_chapter
                }
            }

        #insert data into the database
        collection.insert_one(ping_cm) # insert_many() for larger sets
        print('url info insertion complete...')

    def retrieve_url_info_db(self, site_url, latest_chapter):
        print('retrieving url info...')
        time.sleep(2)

        collection = self.get_db()



    def get_db(self):
        user_password = 'saXES@8npBcp'
        mongo_url = f"mongodb+srv://deolijus:{urllib.parse.quote(user_password)}@cluster0.bxftk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        cluster = MongoClient(mongo_url)
        db = cluster["test_database"]
        collection = db["manga"]

        return collection


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
    ct.parse_url(url)
    print(ct.url)
    print(ct.site)
    #ct.get_comic(ct.site)
    ct.check_for_update()
    #comic_class = ct.comic_class
    #print(comic_class.name)
    #latest_chapter = comic_class.get_last_chapter(url)
    
    #print(latest_chapter)
    #insert_url_info_db(url, latest_chapter)

    print('\n')
