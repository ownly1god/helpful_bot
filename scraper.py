import requests
import time
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession, HTMLSession
import nest_asyncio
import asyncio


def track_comic(url, db):
    #url = 'https://manhuaplus.com/manga/martial-peak/'

    #add name, url, and latest chapter to database
    print(f'Scanning Link: {url}')
    time.sleep(1)

    if url.endswith('/'):
        name = url.split('/')[-2] 
    else:
        name = url.split('/')[-1] 

    print(f'Name Retrieved: {name}')
    time.sleep(1)

    if not name:
        print(f'No name: {name}...\n')
        return (None, name)

    print(f'Comic Name: {name}\n')
    
    latest_chapter = get_last_chapter(url)
    if not latest_chapter:
        return (None, None)

    print(f'Checking DB for:{name}...\n')
    time.sleep(1)


    for comic in db:
        if name in comic[0]:
            print(f'{name} already being tracked\n')
            print(f'DB List:{db}...\n')
            return (False, name)
        else:
            print(f'Tracking: {name}\n')
            print(f'Updating DB List...\n')
            db.append([name, url, latest_chapter])
            print(f'DB List:{db}...\n')
            return (True, name)
        

    
    


async def get_last_chapter(url):
    
    if asyncio.get_event_loop().is_running():
        
        nest_asyncio.apply()
        session = AsyncHTMLSession()
        page = session.get(url)
        page.html.arender(sleep=5, keep_page=True, scrolldown=1)

        print(page)
        soup = BeautifulSoup(page.html.raw_html, "html.parser")
 

        print(f'Retrieving Chapter List...\n')
        

    #manhuaplus
    if 'manhuaplus' in url:
        print('Retrieveing from Manhuaplus\n')
        chapter_list= soup.find_all("li", class_="wp-manga-chapter")
        if not chapter_list:
            print(f'No Chapter List Element Found')
            return

        chapter_list_item = chapter_list[0]
        print(f'Checking Chapter List for url element...\n')
        time.sleep(1)
        chapter_link = chapter_list_item.find_all('a')[0]

        print(f'Retrieving Link...\n')
        time.sleep(1)
        latest_chapter = chapter_link['href'].split('/')[-2]
        print(f'Latest Chapter: {latest_chapter}\n')

    #manhuatop
    if 'manhwatop' in url:
        print('Retrieveing from Manhuatop\n')
        chapter_list = soup.find_all("li", class_="wp-manga-chapter")
        if not chapter_list:
            print(f'No Chapter List Element Found')
            return

        chapter_list_item = chapter_list[0]
        print(f'chapterlist: {chapter_list_item}')
        time.sleep(1)

        print(f'Checking Chapter List for url element...\n')
        time.sleep(1)
        chapter_link = chapter_list_item.find_all('a')[0]

        print(f'Retrieving Link...\n')
        time.sleep(1)
        latest_chapter = chapter_link['href'].split('/')[-2]
    

    return latest_chapter

def check_for_update(db):
    #go through database, for each title retrieve the url and curr_chapter

    try:
        while True:
            print(f'Initiating Scan')
            print(f'current db: {db}\n')
            for comic in db:
                name, url, curr_chapter = comic #get from database
                print(f'Scanning for: {name}')
                scanned_chapter = get_last_chapter(url)

                print(f'Stored chapter: {curr_chapter}')
                if scanned_chapter != curr_chapter:
                    comic[2] = scanned_chapter #update database
                    

                    print(f'New chapter out!: {curr_chapter}')
                    print(f'\tStored chapter changed to: {curr_chapter}')
                else:
                    print(f'\tNo new chapter')
                
                print(f'\tStored chapter: {curr_chapter}')

            print(f'\tSleeping for 10 seconds\n')
            time.sleep(7)

            #if track command is triggered
            #   track_comic(summary_page_URL)

    except KeyboardInterrupt:
        print('Exiting Scan')


summary_page_URL = 'https://manhuaplus.com/manga/martial-peak/'


#db = [['martial-peak', 'https://manhuaplus.com/manga/martial-peak/', 'chapter-1350']]

#print(f'current db: {db}\n')
#track_comic(summary_page_URL, db)
#time.sleep(3)

#check_for_update() #create thread for continuous update

