

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

    db_name = 'test_database'
    db = cluster[db_name]

    collection_name = 'manga'
    collection = db["manga"]

    print('db retrieved')
    return collection


def db_post():
    collection = get_db()

    print('creating entry')
    #post = {"_id":0, "name":"tim", "score" : 5}
    #collection.insert_one(post)

    #post = {"_id":2, "name":"jim", "score" : 6}
    #post2 = {"_id":3, "name":"kim", "score" : 7}
    #collection.insert_many([post, post2])

    #post3 = {"_id":11,"comic_list" : [{"name":"one-piece", "genre": "shonen"},{"name":"naruto", "genre": "shonen"}]}
    post3 = {"_id":10,"comic_list" : {"one-piece" : {"genre": "shonen", 'rating': 6}, 
                                        "naruto": {"genre": "shonen", 'rating': 9.5}}}

    
    collection.insert_one(post3)

def db_query():
    collection = get_db()

    print('querying...')
    # results = collection.find({"name":"kim"})
    results = collection.find({})


    comic_list = {}
    results = collection.find({"_id":10})
    for result in results:
        #print(result)
        comic_list = result['comic_list']
        #result['comic_list']
        #print(f'results: {tracked_comics}')
        
    #print(comic_list)
    for comic, details in comic_list.items():
        print(f'{comic}: {details}')
    #for comic in tracked_comics:
     #       print(f'tracked comic: {comic}')
    
def db_delete():
    collection = get_db()

    print('deleting...')
    #results = collection.delete_one({"_id": 0})
    results = collection.delete_many({})

def db_replace():
    collection = get_db()

    print('replacing...')
    #results = collection.update_many({"_id":2}, {"$set":{"name": "tim"}})
    results = collection.update_many({"_id":2}, {"$set":{"friends": "no"}})

def db_count():
    collection = get_db()

    print('counting...')
    count = collection.count_documents({})

    print(f'count: {count}')
    






def insert_url_info_db():
    print('inserting url info...')
    time.sleep(2)

    collection = get_db()

    site_url = 'https://onepiece.piece'
    site_url2 = 'https://naruto.filler'
    latest_chapter = '144'
    
    post_comics = {"_id":11,"comic_list" : {
                            "one-piece" : {"url": site_url, 'latest_chapter': 6}, 
                            "naruto": {"url": site_url2, 'latest_chapter': 9}}}


    #insert data into the database
    collection.insert_one(post_comics) # insert_many() for larger sets
    print('url info insertion complete...')

def retrieve_url_info_db():
    print('retrieving url info...')
    time.sleep(2)
    collection = get_db()

    
    comic_list = {}
    results = collection.find({"comic_list": {"$exists": True}})

    for result in results:
        comic_list = result['comic_list']
        entry_id = result['_id']

    #for comic, details in comic_list.items():
    #    print(f'{comic}: {details}')

    return entry_id, comic_list
 
def update_comic_list_db(entry_id, new_value):
    collection = get_db()

    print('replacing...')   
    results = collection.update_one({"_id":entry_id}, {"$set":{"comic_list": new_value}})

#db_post()
#db_query()
#db_delete()
#db_replace()
#db_count()




new_entry = {"comic_list" : 
                {
                'martial-peak' : {
                    "url": 'https://manhuaplus.com/manga/martial-peak/', 
                    'latest_chapter': 'chapter-100'}, 
                'martial-park' : {
                    "url": 'https://manhuaplus.com/manga/martial-peak/', 
                    'latest_chapter': 'chapter-200'}, 
                'martial-perk' : {
                    "url": 'https://manhuaplus.com/manga/martial-peak/', 
                    'latest_chapter': 'chapter-300'}, 
                }
            }

for key, value in new_entry['comic_list'].items():
    print(f'comic name: {key}')
    print(f'comic values: {value}\n')