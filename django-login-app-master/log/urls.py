#!python
# log/urls.py
from django.conf.urls import url

from . import views

# We are adding a URL called /home
# Registration URLs
#url(r'^register/$', views.register, name='register'),
#url(r'^register/success/$', views.success, name='success'),
#url(r'^loggedin/$', views.loggedin, name='loggedin'),

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/success/$', views.registration_success, name='registration_success'),
	url(r'^loggedin/$', views.loggedin, name='loggedin'),
	
]
