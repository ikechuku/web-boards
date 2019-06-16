from django.conf.urls import url
from boards import views

app_name = 'boards'

urlpatterns = [
    url(r'^$', views.home, name='boards'),   
    url(r"(?P<pk>\d+)/new/", views.new_topic, name='new_topic'),
  
#   new topic
    #  url(r'(?P<pk>[0-9]+)/new/$', views.new_topic(), name='new_topic'),

    url(r'(?P<pk>\d+)/$', views.board_topics, name='board_topics'),

]