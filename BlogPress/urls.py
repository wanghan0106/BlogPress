from django.conf.urls import patterns, url,include

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BlogPress.views.home', name='home'),
    # url(r'^BlogPress/', include('BlogPress.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.index', name='index'),
    url(r'^register$', 'home.views.register', name='register'),
    url(r'^home/', include('home.urls',namespace='home')),
    url(r'^blog/', include('blog.urls',namespace='blog')),
    url(r'^user/', include('user.urls',namespace='user')),
)
