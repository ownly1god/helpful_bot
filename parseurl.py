

#url = 'https://manhuaplus.com/manga/martial-peak/chapter-1244/'
#url = 'https://manhwatop.com/manga/fffclass-trashero/chapter-91'
#url = 'https://flamescans.org/omniscient-readers-viewpoint-chapter-67/'
# url = 'https://soloxleveling.com/manga/solo-leveling-chapter-161/'
#url = 'https://soloxleveling.com/'
#url = 'https://manhuaplus.com/manga/martial-peak/'
#url= 'https://flamescans.org/series/omniscient-readers-viewpoint/'



import pymongo
from pymongo import MongoClient
import time
import urllib


def get_db():
    user_password = 'saXES@8npBcp'
    mongo_url = f"mongodb+srv://deolijus:{urllib.parse.quote(user_password)}@cluster0.bxftk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    cluster = MongoClient(mongo_url)
    db = cluster["test_database"]
    collection = db["manga"]

    return collection

def insert_url_info_db():
    print('inserting url info...')
    time.sleep(2)

    collection = get_db()

    site_url = 'https://flamescans.org/series/omniscient-readers-viewpoint/'
    latest_chapter = '144'
    
    #ping_cm = {'comic_name': 'solo-friend','url': site_url,'latest_chapter': latest_chapter}
    ping_cm = {
        'comics_list': {
            {'comic_name': 'solo-friend','url': site_url,'latest_chapter': latest_chapter},
            {'comic_name': 'solo-dolo','url': site_url,'latest_chapter': latest_chapter}
        }
    }
    #insert data into the database
    collection.insert_one(ping_cm) # insert_many() for larger sets
    print('url info insertion complete...')

def retrieve_url_info_db():
    print('retrieving url info...')
    time.sleep(2)

    collection = get_db()

    comic_list = list(collection.find())
    #print(f'\ncomic_list: {comic_list}')
    
    print(f'{comic_list}')


insert_url_info_db()
retrieve_url_info_db()