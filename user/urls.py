from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^profile$', 'user.views.profile', name='profile'),
    url(r'^blog$', 'user.views.blog', name='blog'),
    url(r'^column$', 'user.views.column', name='column'),
    url(r'^focus$', 'user.views.focus', name='focus'),
    url(r'^profile/save', 'user.views.save_profile', name='profile/save'),
    url(r'^logo$', 'user.views.logo', name='logo'),
    url(r'^logo/save', 'user.views.save_logo', name='logo/save'),
    url(r'^password$', 'user.views.password', name='password'),
    url(r'^password/check/(?P<password>\w+)$', 'user.views.check_password', name='password/check'),
    url(r'^password/save', 'user.views.save_password', name='password/save'),
    url(r'^blog/add', 'user.views.add_blog', name='blog/add'),
    url(r'^blog/save', 'user.views.save_blog', name='blog/save'),
    url(r'^blog/del/(?P<blog_id>\d+)$', 'user.views.delete_blog', name='blog/del'),
    url(r'^column/add', 'user.views.add_column', name='column/add'),
    url(r'^column/edit/(?P<column_id>\d+)$', 'user.views.edit_column', name='column/edit'),
    url(r'^column/save', 'user.views.save_column', name='column/save'),
    url(r'^column/del/(?P<column_id>\d+)$', 'user.views.delete_column', name='column/del'),

)
