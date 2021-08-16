
import sys
from bs4 import BeautifulSoup
import urllib.request
from requests_html import HTMLSession


url = 'https://manhuaplus.com/manga/martial-peak/'
url2 = 'https://manhwatop.com/manga/fffclass-trashero'
id_val = '#manga-chapters-holder'
class_val = 'wp-manga-chapter'

 
# create an HTML Session object
session = HTMLSession()
 
# Use the object above to connect to needed webpage
resp = session.get(url2)
 
# Run JavaScript code on webpage
resp.html.render(sleep=2, keep_page=True, scrolldown=1)
soup = BeautifulSoup(resp.html.raw_html, "html.parser")

chapter_list= soup.find_all("li", class_=class_val)


chapter_list_item = chapter_list[0]
chapter_link = chapter_list_item.find_all('a')[0]
latest_chapter = chapter_link['href'].split('/')[-2]
print(f'Latest Chapter: {latest_chapter}\n')

#print(resp.html.html)
#b = soup.findAll("li", class_=class_val) #title
#for i in b:
#    print(i)

#chapter_list = resp.html.find(id_val)
#li_tags = chapter_list[0].find('li')
#chapter_link = li_tags[0].find('a')
#li_tags = resp.html.search(id_val)
#print(chapter_link)





