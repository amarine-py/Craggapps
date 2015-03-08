from django.conf.urls import patterns, url
from climbcast import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^cragguser/(?P<user_name_slug>[\w\-]+)/$', views.cragguser, name='cragguser'),
        url(r'^add_cragg_user/$', views.add_cragg_user, name='add_cragg_user'),
        url(r'^add_cragg_area/$', views.add_cragg_area, name='add_cragg_area'),
        url(r'^craggarea/(?P<area_name_slug>[\w\-]+)/$', views.craggarea, name='craggarea'),
        url(r'^add_to_favorites/(?P<area_name_slug>[\w\-]+)/$', views.add_to_favorites, name='add_to_favorites'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        
)
