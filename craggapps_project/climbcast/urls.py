from django.conf.urls import patterns, url
from climbcast import views
from climbcast.views import AddRoute, UpdateRoute, UpdateUser, UpdateUserProfile, TickDetailView
from django.views.decorators.cache import cache_page


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^cragguser/(?P<user_name_slug>[\w\-]+)/$', views.cragguser, name='cragguser'),
        #url(r'^add_cragg_user/$', views.add_cragg_user, name='add_cragg_user'),
        url(r'^add_cragg_area/$', views.add_cragg_area, name='add_cragg_area'),
        url(r'^craggarea/(?P<area_name_slug>[\w\-]+)/$', cache_page(60 * 1200)(views.craggarea), name='craggarea'),
        url(r'^add_to_favorites/(?P<area_name_slug>[\w\-]+)/$', views.add_to_favorites, name='add_to_favorites'),
        #url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.logout, name='logout'),
        url(r'^route/add/$', AddRoute.as_view(), name='route_form'),
        url(r'^cragguser/update/user/(?P<pk>[\w\-]+)/$',
            UpdateUser.as_view(), name='user_update_form'),
        url(r'^cragguser/update/userprofile/(?P<user_name_slug>[\w\-]+)/$',
            UpdateUserProfile.as_view(), name='userprofile_update_form'),
        url(r'^cragguser/(?P<user_name_slug>[\w\-]+)/ticks/(?P<pk>[\w\-]+)/(?P<slug>[\w\-]+)/$',
            TickDetailView.as_view(), name='routetick_detail'),
        
)
