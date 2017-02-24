from django.test import TestCase

# Create your tests here.

import datetime
from show_news.app_classes import Source, Article
from show_news.models import News, Sources

class Articles_Tests(TestCase):
    def setUp(self):
	date = datetime.date.today()
	received = datetime.datetime.now()
	test_item_1 = Article("Test Headline TWO", "https://www.ft.com/", date, received, "Test Description", "Test Source One", "Test Category")
	test_item_1.save_article()
	test_item_1 = None

	test_item_3 = Article("Test Headline One", "https://www.ft.com/", date, received, "Test Description", "Test Source One", "Test Category")
	test_item_3.save_article()
	test_item_3 = None
	
	date = None
	received = None

    def test_save_article(self):
	date = datetime.date.today()
    	received = datetime.datetime.now()
	testitem_save_article = Article("Test Headline Three", "https://www.ft.com/", date, received, "Test Description", "Test Source One", "Test Category")
	self.assertEqual(testitem_save_article.save_article(), "Item saved.")
    	test_item = News.objects.filter(url = testitem_save_article.url).get(headline = testitem_save_article.headline) 
	self.assertIsNotNone(test_item)
	self.assertEqual(test_item.headline, testitem_save_article.headline)
	self.assertEqual(test_item.url, testitem_save_article.url)
	self.assertEqual(test_item.date, testitem_save_article.date)
	self.assertEqual(str(test_item.received)[:-6], str(testitem_save_article.received))
	self.assertEqual(test_item.description, testitem_save_article.description)
	self.assertEqual(test_item.source, testitem_save_article.source)
	self.assertEqual(test_item.category, testitem_save_article.category)

	testitem_save_article_2 = Article("Test Headline Three", "https://www.ft.com/", date, received, "Test Description", "Test Source One", "Test Category")
	try:
		testitem_save_article_2.save_article()
	except Exception as error:
		self.assertEqual(str(error)[0:13], "duplicate key")

	date = None
	received = None

    def test_check_for_item(self):
	date = datetime.date.today()
	received = datetime.datetime.now()
    	test_item_1 = Article("Test Headline TWO", "https://www.ft.com/", date, received, "Test Description", "Test Source One", "Test Category")
    	test_item_2 = Article("Test Headline One", "https://docs.djangoproject.com/en/1.10/intro/tutorial05/", date, received, "Test Description", "Test Source One", "Test Category")
	test_item_3 = Article("Test Headline One", "https://www.ft.com/", date, received, "Test Description", "Test Source One", "Test Category")
        test_item_4 = Article("Test Headline One", "https://www.ft.com/", date, received, "Test Description 2", "Test Source One 2", "Test Category 2")

	self.assertEqual(test_item_1.check_for_item(), "Item already exists.")
    	
	self.assertIsNone(test_item_2.check_for_item())
	
	self.assertEqual(test_item_3.check_for_item(), "Item already exists.")

	self.assertEqual(test_item_4.check_for_item(), "Item already exists.")		

class Sources_Tests(TestCase):

    def setUp(self):
	test = Source("Bradford DeLong", "http://delong.typepad.com/", "","100")
	code='''try:
    	items = soup.find_all("h3","entry-header")
    	for i in range(0,min(10,len(items))):
        	headline = items[i].find("a").string
        	if headline is not None:
            		url = items[i].find("a")["href"]
            		date = datetime.date.today()
            		category = ""
            		source = smart_str(self.name)
            		description = ""
            		received = datetime.datetime.now()
            		article = Article(headline, url,date,received,description,source,category)
            		assert article is not None
            		self.articles_to_add.append(article)
            		print len(self.articles_to_add)
            		assert len(self.articles_to_add) > 0
            		article = None
except:
   	raise'''
	test.code = code
	
	test_source = Sources(name = test.name, url = test.url, code = test.code, rangking = test.rangking)
	test_source.save()

    def test_save_news(self):
	test_source = Source("TestSource", "http://delong.typepad.com/", "","100")
	date = datetime.date.today()
	received = datetime.datetime.now()
	item = Article("Test Headline TWO", "https://www.ft.com/", date, received, "Test Description", "Test Source One", "Test Category")
    	item2 = Article("Test Headline One", "https://docs.djangoproject.com/en/1.10/intro/tutorial05/", date, received, "Test Description", "Test Source One", "Test Category")
	item3 = Article("Test Headline One", "https://www.ft.com/", date, received, "Test Description", "Test Source One", "Test Category")
	test_source.articles_to_add.append(item)
	test_source.articles_to_add.append(item2)
	test_source.articles_to_add.append(item3)

	self.assertEqual(len(test_source.articles_to_add),3)
	self.assertIsNone(item.check_for_item())
	self.assertIsNone(item2.check_for_item())
	self.assertIsNone(item3.check_for_item())
	test_source.save_news()
	self.assertEqual(len(test_source.articles_to_add),0)
	self.assertEqual(item.check_for_item(), "Item already exists.")
	self.assertEqual(item2.check_for_item(), "Item already exists.")
	self.assertEqual(item3.check_for_item(), "Item already exists.")
	
	item = Article("Test Headline TWO", "https://www.ft.com/", date, received, "This should not exists.", "Test Source One", "Test Category")
    	item2 = Article("Test Headline One", "https://docs.djangoproject.com/en/1.10/intro/tutorial05/", date, received, "This should not exists.", "Test Source One", "Test Category")
	item3 = Article("Test Headline One", "https://www.ft.com/", date, received, "This should not exists.", "Test Source One", "Test Category")
	test_source.articles_to_add.append(item)
	test_source.articles_to_add.append(item2)
	test_source.articles_to_add.append(item3)

	self.assertEqual(len(test_source.articles_to_add),3)
	test_source.save_news()
	self.assertEqual(len(test_source.articles_to_add),0)
	self.assertEqual(len(News.objects.filter(description = item.description)),0)


    def test_get_news(self):
	from bs4 import BeautifulSoup
	import requests
	import datetime
	source_from_db = Sources.objects.get(url = "http://delong.typepad.com/")
	source = Source(source_from_db.name, source_from_db.url, source_from_db.code, source_from_db.rangking)
	source.get_news()
	
	self.assertEqual(len(source.articles_to_add),5)
	for each in source.articles_to_add:
		self.assertEqual(each.source, source.name)
		self.assertIsNotNone(each.headline)
		self.assertEqual(each.date, datetime.date.today())
	






