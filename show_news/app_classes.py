class Source(object):
 
    def __init__(self, name, url, code, rangking):
        assert type(name) == str or type(name) == unicode, "type is: " + str(type(name))
        assert type(url) == str or type(url) == unicode, "type is: " + str(type(url))

        self.name = name
        self.url = url
        self.ranking = rangking
        self.code = code
        self.articles_to_add = []
        
    def get_news(self):
	import requests
	from bs4 import BeautifulSoup
	import datetime
	from django.utils.encoding import smart_str, smart_unicode
        assert self.url is not None
        assert requests.get(self.url, verify=False).status_code == 200
        soup = BeautifulSoup(requests.get(self.url,verify=False).text, "lxml") 
	code_clean = '\n'+self.code+'\n'
	code_clean = code_clean.replace(" stopline ","\n")
        exec(code_clean)
	code_clean=None
       
        
    def save_news(self):
	import requests
	from show_news.models import News, Sources
	from show_news.app_classes import Source, Article
        assert self.articles_to_add is not None, "No new articles to add."
        for i in self.articles_to_add:
            assert i is not None
            assert i.url is not None 
            if i.check_for_item() == None:
                i.save_article()
            else:
                print i.check_for_item()
	del self.articles_to_add[:]          

class Article(object):
    def __init__(self, headline, url,date,received,description,source,category):
        self.headline = headline
        self.url = url
        self.date = date
        self.received = received
        self.description = description
        self.source  = source
        self.category = category

    def check_for_item(self):
	from show_news.models import News
        if not News.objects.filter(url = self.url):
            return None
        else: 
            return "Item already exists."
    
    def save_article(self):
	from show_news.models import News
        article = News(url = self.url, headline = self.headline, date = self.date, received=self.received, description=self.description, source=self.source, category = self.category)     
        article.save()
        return "Item saved."
    
    def putonlist(self):
        print "nothing yet"
        
    def favourSource(self):
        print "nothing yet"
        
    def remove(self):
        print "nothing yet"
        
class Newslist(object):
    def __init__(self, name, custom, category,articles,sources):
        print "nothing yet"
    
    def order(object):
        print "nothing yet"