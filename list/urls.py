from django.conf.urls import patterns, url

from list import views, models

urlpatterns = patterns('',
    url(r'^$', views.homepage, name='index'),
    url(r'^(?P<prog_id>\d+)/$', views.detail, name='detail'),
    url(r'^login', views.login11, name='login'),
    url(r'^logout', views.logout_view, name='logout'),
    url(r'^lost', views.lost, name='lost'),
    url(r'^visual', views.visual, name='visual'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^users', views.users, name='users'),
    url(r'^homepage', views.index, name='homepage'),
)

