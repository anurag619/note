from django.conf.urls import patterns, url
from notes import views

urlpatterns = patterns('',
    url(r'^index/', views.index, name='index'),
    url(r'^profile/', views.Profile, name='Profile'),
    url(r'^login/', views.login_user, name='login_user'),
    url(r'^invalid_login/', views.invalid_login, name='invalid_login'),
    url(r'^create/', views.create, name='create'),
    url(r'^all_notes/', views.all_notes, name='all_notes'),
    url(r'^delete/(?P<note_id>\d+)/', views.delete, name='delete'),
    url(r'^edit/(?P<note_id>\d+)/', views.edit_note, name='edit_note'),
    #url(r'^edit_note/', views.edit_note, name='edit_note'),
    url(r'^get_notes/(?P<note_id>\d+)/', views.get_notes, name='get_notes'),
    url(r'^logout/', views.logout_user, name='logout_user'),
    
    
)



