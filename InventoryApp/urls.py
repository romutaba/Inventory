"""InventoryApp URL Configuration

"""
from django.conf.urls import url, include
from django.contrib import admin
#adding views import
from django.contrib.auth import views
from First.forms import LoginForm


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('First.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}), 
]
