from django.conf.urls import patterns, url
from wcdma_mapper import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^map/(?P<code>RU[0-9]{5}(\.T)?)/$', views.map_page),
    url(r'^map/(?P<code>RAN[0-9]{3,4}(\.[0-9])?C?(\.T)?)/$', views.map_page),
    url(r'^map/(?P<code>RNC[0-9]{4}\.T)/$', views.map_page),
    url(r'^map/(?P<code>MCRNC[0-9]{4}\.T)/$', views.map_page),
    url(r'^map/(?P<code>RAS[0-9]{5})/$', views.map_page),
    url(r'^map/(?P<code>[\w\-\.]+)/$', views.map_nopage),
    )
