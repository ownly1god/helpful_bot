class ComicSite:
    def __init__(self, url):
        self.site_type = 'Default'
        self.site_name = None
        self.url = None
        self.last_chapter = None
        self.comic_name = None

    def print_name():
        return self.site_type
    
    def get_last_chapter(self, url):
        print(f'Retrieving last chapter for {self.site_type}')
        last_chapter = 'chapter-1' # test value
        return last_chapter.lower()


class Manhuaplus(ComicSite):
    def __init__(self, url):
        self.site_type = 'Manhuaplus'
    
    def get_comic_title(self):
        surl = url.split('manga/')[1]
        title = surl.split('/chapter')[0]
        title = title.replace('/','')



    def get_last_chapter(self, url):
        print(f'Retrieving last chapter for {self.site_type}')
        # logic for retrieving latest_chapter
        last_chapter = 'chapter-100' # test value

        return last_chapter.lower()

class Manhwatop(ComicSite):
    def __init__(self, url):
        self.site_type = 'Manhwatop'

    def get_last_chapter(self, url):
        print(f'Retrieving last chapter for {self.site_type}')
        # logic for retrieving latest_chapter
        last_chapter = 'chapter-121' # test value
        
        return last_chapter.lower()
    
    def get_comic_title(self):
        surl = url.split('manga/')[1]
        title = surl.split('/chapter')[0]
        title = title.replace('/','')

        return title

class Flamescans(ComicSite):
    def __init__(self, url):
        self.site_type = 'Flamescans'
        

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

        return(title)