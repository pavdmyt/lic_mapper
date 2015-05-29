from django.conf.urls import patterns, url
from wcdma_mapper import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'))
