from django.test import TestCase

# Create your tests here.

import datetime
from show_news.app_classes import Source, Article
from show_news.models import News, Sources

class Articles_Tests(TestCase):

    def test_save_article(self):
    	date = datetime.date.today()
    	received = datetime.datetime.now()
    	item = Article("Test Headline One", "https://www.ft.com/", date, received, "Test Description", "Test Source One", "Test Category")
	self.assertEqual(item.save_article(), "Item saved.")
    	test_item = News.objects.get(url = item.url) 
	self.assertIsNotNone(test_item)
	self.assertEqual(test_item.headline, item.headline)
	self.assertEqual(test_item.url, item.url)
	self.assertEqual(test_item.date, item.date)
	self.assertEqual(str(test_item.received)[:-6], str(item.received))
	self.assertEqual(test_item.description, item.description)
	self.assertEqual(test_item.source, item.source)
	self.assertEqual(test_item.category, item.category)

    def test_check_for_item(self):
	date = datetime.date.today()
	received = datetime.datetime.now()
    	item = Article("Test Headline TWO", "https://www.ft.com/", date, received, "Test Description", "Test Source One", "Test Category")
    	item2 = Article("Test Headline One", "https://docs.djangoproject.com/en/1.10/intro/tutorial05/", date, received, "Test Description", "Test Source One", "Test Category")
	item3 = Article("Test Headline One", "https://www.ft.com/", date, received, "Test Description", "Test Source One", "Test Category")
        self.assertIsNone(item.check_for_item())
	item.save_article()
	self.assertEqual(item.check_for_item(), "Item already exists.")
    	self.assertIsNone(item2.check_for_item())
	self.assertEqual(item2.save_article(), "Item saved.")
	self.assertEqual(item3.save_article(), "Item saved.")
	try:
		item.save_article()
	except Exception as error:
		self.assertEqual(str(error)[0:13], "duplicate key")
		

class Sources_Tests(TestCase):

    def test_save_news(self):
	delong = Source("TestSource", "http://delong.typepad.com/", "","100")
	date = datetime.date.today()
	received = datetime.datetime.now()
	item = Article("Test Headline TWO", "https://www.ft.com/", date, received, "Test Description", "Test Source One", "Test Category")
    	item2 = Article("Test Headline One", "https://docs.djangoproject.com/en/1.10/intro/tutorial05/", date, received, "Test Description", "Test Source One", "Test Category")
	item3 = Article("Test Headline One", "https://www.ft.com/", date, received, "Test Description", "Test Source One", "Test Category")
	delong.articles_to_add.append(item)
	delong.articles_to_add.append(item2)
	delong.articles_to_add.append(item3)
	self.assertEqual(len(delong.articles_to_add),3)
	self.assertIsNone(item.check_for_item())
	self.assertIsNone(item2.check_for_item())
	self.assertIsNone(item3.check_for_item())
	delong.save_news()
	self.assertEqual(item.check_for_item(), "Item already exists.")
	self.assertEqual(item2.check_for_item(), "Item already exists.")
	self.assertEqual(item3.check_for_item(), "Item already exists.")

    def test_get_news(self):
	from bs4 import BeautifulSoup
	import requests
	import datetime
	test = Source("mainly macro", "https://mainlymacro.blogspot.de/", "","100")

	test.code = '''
try:
    items = soup.find_all("h3","post-title entry-title")
    for i in range(0,5):
        headline = items[i].find("a").string
        url = items[i].find("a")["href"]
        date = datetime.date.today()
        category = ""
        source = self.name
        description = items[i].find_next("div","post-body entry-content").text
        description = description[:240]+ "..."
        received = datetime.datetime.now()
        article = Article(headline, url,date,received,description,source,category)
        assert article is not None
        self.articles_to_add.append(article)
        article = None
except:
    	raise'''
	
	test.get_news()
	self.assertEqual(len(test.articles_to_add),5)
	for each in test.articles_to_add:
		self.assertEqual(each.source, test.name)
		self.assertIsNotNone(each.headline)
		self.assertEqual(each.date, datetime.date.today())
	






