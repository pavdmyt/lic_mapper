from django.conf.urls import patterns, url
from wcdma_mapper import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^map/(?P<ra_item_input>[\w\.]+)/$',
                           views.map_page,
                           name='map_page'),)
