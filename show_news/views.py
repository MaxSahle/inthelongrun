from django.shortcuts import render


from show_news.models import News, Sources
from bs4 import BeautifulSoup
import re
import requests
import datetime
from show_news.app_classes import Source, Article

def index(request):

    all_sources = Sources.objects.all()
    all_news = News.objects.all()
    context ={
	'all_news': all_news,
	'all_sources': all_sources
	}
    for each in all_sources:
    	source_instance = Source(name=each.name, url=each.url, rangking = each.rangking, code = each.code)
    	print len(source_instance.articles_to_add)
	print "Source:" + source_instance.name
	source_instance.get_news()
	print "Articles to add:" + str(len(source_instance.articles_to_add))
    	source_instance.save_news()
    	source_instance= None
    
    return render(request, 'show_news/index.html', context)