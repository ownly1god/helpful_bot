class ComicSite:
    def __init__(self, url):
        self.site_type = 'Default'
        self.site_name = None
        self.url = None
        self.last_chapter = None
        self.comic_name = None

    def print_name(self):
        return self.site_type
    
    def get_lastest_chapter(self, url):
        print(f'Retrieving last chapter for {self.site_type}')
        last_chapter = 'chapter-1' # test value
        return last_chapter.lower()


class Manhuaplus(ComicSite):
    def __init__(self, url):
        print('Instantiating Manhuaplus')
        #self.site_type = 'Manhuaplus'
        self.site_name = None
        self.url = url
        self.comic_name = self.get_comic_title()
        self.latest_chapter = self.get_lastest_chapter()
    
    def get_lastest_chapter(self):
        print(f'\tRetrieving lastest chapter for {self.comic_name}')
        # logic for retrieving latest_chapter
        last_chapter = 'chapter-102' # test value
        numbers = ''.join([ch for ch in last_chapter if ch.isdigit()])
        
                

        return last_chapter.lower()

    def get_comic_title(self):
        surl = self.url.split('manga/')[1]
        title = surl.split('/chapter')[0]
        title = title.replace('/','')
        print(f'\tGetting comic title: {title}\n')

        return title.lower()


class Manhwatop(ComicSite):
    def __init__(self, url):
        #self.site_type = 'Manhwatop'
        print('Instantiating Manhuatop')

    def get_last_chapter(self, url):
        print(f'Retrieving last chapter for {self.site_type}')
        # logic for retrieving latest_chapter
        last_chapter = 'chapter-121' # test value
        
        return last_chapter.lower()
    
    def get_comic_title(self):
        surl = self.url.split('manga/')[1]
        title = surl.split('/chapter')[0]
        title = title.replace('/','')

        return title.lower()

class Flamescans(ComicSite):
    def __init__(self, url):
        self.site_type = 'Flamescans'
        print('Instantiating Flamescans')
        

    def get_last_chapter(self, url):
        print(f'Retrieving last chapter for {self.site_type}')
        # logic for retrieving latest_chapter
        last_chapter = 'chapter-144' # test value
        
        return last_chapter.lower()

    def get_comic_title(self):
        if '/series/' in url:
            surl = url.split('series/')[1]
            title = surl.replace('/','')
        else:
            surl = url.split('.org/')[1]
            title = surl.split('-chapter')[0]
        
        return title.lower()

class Soloxleveling(ComicSite):
    def __init__(self, url):
        self.site_type = 'Soloxleveling'
        self.comic_name = 'solo-leveling'
                
    def get_last_chapter(self, url):
        print(f'Retrieving last chapter for {self.site_type}')
        # logic for retrieving latest_chapter
        last_chapter = 'chapter-156' # test value
        
        return last_chapter.lower()

    def get_comic_title(self):
        if 'manga' in url:
            surl = url.split('manga')[1]
            title = surl.split('-chapter')[0]
            title = title[1:]
        else:
            title ='solo-leveling'

        return title.lower()