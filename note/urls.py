from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^notes/', include('notes.urls') ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'note.views.login'),
    url(r'^accounts/auth/$', 'note.views.auth_view'),
    url(r'^accounts/logout/$', 'note.views.logout'),
    url(r'^accounts/loggedin/$', 'note.views.loggedin'),
    url(r'^accounts/invalid/$', 'note.views.invalid_login'),
    url(r'^accounts/register/$', 'note.views.register'),
    url(r'^accounts/success/$', 'note.views.success'),
)



   
