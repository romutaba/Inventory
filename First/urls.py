#First/urls.py
from django.conf.urls import url, include
from . import views
from django.contrib import admin

#adding a url called /home
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^item/(?P<id>\d+)/', views.item_detail, name='item_detail'),
	#url(r'^admin/', include(admin.site.urls)),
]