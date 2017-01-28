from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    
	url(r'^show_news/', include('show_news.urls')),
	url(r'^admin/', admin.site.urls),
	
]
