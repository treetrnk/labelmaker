from django.urls import path
from . import views

urlpatterns = [
    #url(r'^(?P<year>\d{4})\/(?P<month>\d{1,2})\/(?P<day>\d{1,2})\/(?P<slug>\S+)$', views.post, name='post'),
    #url('posts/(?P<slug>.*)', views.post, name='post'),
    #url(r'^(?:rss(?:\.xml)?)|(?:feed(?:.xml)?)$', views.rss, name='rss'),
    path(r'generate-pdf/', views.generate, name='generate'),
    path('', views.index, name='index'),
]
