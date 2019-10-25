from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^add$', views.add, name='add'),
    url(r'^add_travel$', views.add_travel, name='add_travel'),
    url(r'^join/(?P<id>\d+)$', views.join, name='join'),
    url(r'^trip_detail/(?P<id>\d+)$', views.trip_detail, name='trip_detail')
]
