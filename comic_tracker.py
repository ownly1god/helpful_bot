import os
import comic_sites
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
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
        self.lastest_chapter = None
        self.stored_chapter = None
        self.site = None
        self.url = None
        self.comic = None

        mongo_url, db_name, collection_name = self.db_info()
        self.db_collection = self.get_db(mongo_url, db_name, collection_name)


    def db_info(self):
        load_dotenv()
        user_password = os.getenv('USER_PASSWORD')
        user_name = os.getenv('USER_NAME')
        mongo_url = f'mongodb+srv://{user_name}:{urllib.parse.quote(user_password)}@cluster0.bxftk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

        db_name = 'test_database'
        collection_name = 'manga'
        return (mongo_url,db_name,collection_name)
    
    def parse_url(self, url):
        # set the url and site
        try:
            self.url = url
            site = (url.split('/')[2]).split('.')[0]
            self.site = site.lower().capitalize()
            
        except:
            print(f'Unable to parse url: {url}')
    
    def get_comic(self, site):
        try:
            print(f'Site: {site}')
            class_ = getattr(comic_sites, site)
            comic = class_(self.url)
            return comic
        except:
            print(f'Unable to retrieve comic: {site}')


    def track_comic(self, url):
        self.parse_url(url)
        self.comic = self.get_comic(self.site)
        comic_title = self.comic.comic_name
        entry_id, comic_list = self.retrieve_comic_list_db()

        new_entry = {"comic_list" : 
                            {
                            comic_title : {"url": url, 'latest_chapter': self.comic.latest_chapter}, 
                            }
                        }

        # check to see if the url is in the database
        if not comic_list:
            self.insert_url_info_db(new_entry)
        else:
            print(self.comic.comic_name in comic_list)
            if not self.comic.comic_name in comic_list:
                self.update_comic_list_db(entry_id, new_entry['comic_list'])

    
    def check_for_new_chapters(self):
        #try:

        entry_id, comic_list = self.retrieve_comic_list_db()
        for title, data in comic_list.items():
            print(f'\tcomic name: {title}')
            print(f'\tcomic values: {data}\n')
            stored_chapter = data['latest_chapter']

            self.lastest_chapter = self.comic.latest_chapter

            if self.lastest_chapter != stored_chapter:
                print(f'{self.comic.comic_name}: New chapter out!')
            else:
                print(f'{self.comic.comic_name}: No updates...')



        #stored_chapter = self.get_stored_chapter() #retrieve from db

        #print(f'Stored Chapter: {stored_chapter}')
        #print(f'Lastest chapter: {self.lastest_chapter}')
            
        #except:
        #    print('Unable to get updates')


    
    def get_db(self, mongo_url, db_name, collection_name):
        cluster = MongoClient(mongo_url)
        db = cluster[db_name]
        collection = db[collection_name]

        return collection




    def insert_url_info_db(self, new_entry):
        self.db_collection.insert_one(new_entry) # insert_many() for larger sets


    def retrieve_comic_list_db(self):
        results = self.db_collection.find({"comic_list": {"$exists": True}})

        entry_id = None
        comic_list = {}
        for result in results:
            comic_list = result['comic_list']
            entry_id = result['_id']

        return entry_id, comic_list

    
    def update_comic_list_db(self, entry_id, new_entry): 
        results = self.db_collection.update_one({"_id":entry_id}, {"$set":{"comic_list": new_entry}})



# local testing
urls = [
'https://manhuaplus.com/manga/martial-peak/',
'https://manhwatop.com/manga/fffclass-trashero',
'https://soloxleveling.com/',
'https://sololeveling.com/',
'https://flamescans.org/series/omniscient-readers-viewpoint/',
]

url = 'https://manhuaplus.com/manga/martial-peak/'
ct = ComicTracker()
ct.track_comic(url)
ct.check_for_new_chapters()

#for url in urls:
    #ct.parse_url(url)
    #print(ct.url)
    #print(ct.site)
    #ct.get_comic(ct.site)
    #ct.check_for_update()
    #comic_class = ct.comic_class
    #print(comic_class.name)
    #latest_chapter = comic_class.get_last_chapter(url)
    
    #print(latest_chapter)
    #insert_url_info_db(url, latest_chapter)

    #print('\n')
