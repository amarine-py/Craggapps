from django.conf.urls import patterns, url
from climbcast import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^cragguser/(?P<user_name_slug>[\w\-]+)/$', views.cragguser, name='cragguser'),
)
