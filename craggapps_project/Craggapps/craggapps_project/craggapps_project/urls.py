from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from registration.backends.simple.views import RegistrationView
from registration.users import UserModel
from climbcast.models import UserProfile
from django.contrib.auth import authenticate
from django.contrib.auth import login
from registration import signals

# Create a new class that redirects the user to the index page,
# if successful at registering, and also assigns User to UserProfile
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request,user):
        return '/climbcast/'

    def register(self, request, **cleaned_data):
        username, email, password = cleaned_data['username'], cleaned_data['email'], cleaned_data['password1']
        new_user_mod = UserModel().objects.create_user(username, email, password)
        new_user_p = UserProfile.objects.get_or_create(user=new_user_mod)
        

        new_user = authenticate(username=username, password=password)
        login(request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user
    
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'craggapps_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^climbcast/', include('climbcast.urls')),
    # This URL pattern overrides the default redirect for when users register
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}), )

