#importing function url and all views from the blog application
from django.conf.urls import url
from . import views

#signing a view called post_list to the ^$ URL
#this pattern tells Django that views.post_list is the right place to go if someone enters the website
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),

]