from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^save', 'home.views.save', name='save'),
    url(r'^check/(?P<user_name>\w+)$', 'home.views.check', name='check'),
    url(r'^logout', 'home.views.logout', name='logout'),
    url(r'^signin', 'home.views.signin', name='signin'),
    url(r'^login$', 'home.views.login', name='login'),
)
