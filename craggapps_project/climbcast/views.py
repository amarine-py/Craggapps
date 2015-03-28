from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from climbcast.models import CraggArea, UserProfile, Route, RouteTick
from climbcast.forms import CraggAreaForm, UserForm, UserProfileForm, RouteForm, UpdateUserForm, UpdateUserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.decorators.cache import cache_page
from django.forms.models import inlineformset_factory
import pywapi
import urllib2
import json

    
# Create your views here.

def index(request):
    # Query the database for a list of ALL users currently stored.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    user_list = UserProfile.objects.all()[:5]
    context_dict = {'users': user_list}

    area_list = CraggArea.objects.all()[:5]
    context_dict['areas'] = area_list

    # Get the number of visits to the site.
    # We use the COOKIES.get() function to obtain the visits cookie.
    # If the cookie exists, the value returned is casted to an integer.
    # If the cookie doesn't exist, we default to zero and cast that.
    visits = int(request.COOKIES.get('visits','1'))
    reset_last_visit_time = False
    response = render(request, 'climbcast/index.html', context_dict)
    #HERHEEHRERHEH
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'climbcast/index.html', context_dict)

def about(request):
    return render(request, 'climbcast/about.html', {})

def cragguser(request, user_name_slug):
    
    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a username slug with the given username?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        users = UserProfile.objects.get(slug=user_name_slug)
        user_link = User.objects.get(username=users.user.username)
        context_dict['user_name'] = users.user.username

        # Get the User model PK to send to template
        context_dict['user_pk'] = users.user.pk

        # Get the slug for the template
        context_dict['slug'] = users.slug

        # Get UserProfile weather preferences
        heat = users.heat_tolerance
        cold = users.cold_tolerance
        mind_wind = users.mind_windy

        # Retrieve THE ASSOCIATED AREAS IN THE FUTRE. For now, attributes.
        user_area_list = users.craggarea_set.all()

        # Retrieve the user's ticks
        user_tick_list = user_link.routetick_set.all()[:10]

        # Note that filter returns >= 1 model instance.
        u_e = users.user.email
        f_n = users.user.first_name
        l_n = users.user.last_name

        # Add the variables into the context dictionary.
        context_dict['email_address'] = u_e
        context_dict['first_name'] = f_n
        context_dict['last_name'] = l_n
        context_dict['user_areas'] = user_area_list
        context_dict['user_ticks'] = user_tick_list
        context_dict['heat'] = heat
        context_dict['cold'] = cold
        context_dict['mind_wind'] = mind_wind
        
        # Also add the user object from the database.
        # We will use this in the template to verify that the user exists.
        context_dict['cragguser'] = users       

    except User.DoesNotExist:
        # If user doesn't exist...
        # Don't do anything - the template displays the "no user" message for us.
        pass

    return render(request, 'climbcast/cragguser.html', context_dict)

class UpdateUserProfile(UpdateView):
    model = UserProfile
    template_name = 'climbcast/userprofile_update_form.html'
    form_class = UpdateUserProfileForm
    slug_url_kwarg = 'user_name_slug'
    


class UpdateUser(UpdateView):
    model = User
    template_name = 'climbcast/user_update_form.html'
    form_class = UserForm
    
    
    def get_context_data(self, **kwargs):
        context = super(UpdateUser, self).get_context_data(**kwargs)
        me = self.request.user
        context['user_name_slug'] = me.userprofile
        return context

    
def craggarea(request, area_name_slug):

    #Create a context dictionary that we can pass to template rendering engine
    context_dict = {}

    try:
        # Can we find an area slug with the given area name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        areas = CraggArea.objects.get(slug=area_name_slug)
        weather_yahoo = pywapi.get_weather_from_yahoo(areas.area_zip)
        weather_com = pywapi.get_weather_from_weather_com(areas.area_zip)
        weather_wunder = urllib2.urlopen('http://api.wunderground.com/api/060cb0792aec8a1c/forecast/q/' + areas.area_zip +'.json')
        wunder_string = weather_wunder.read()
        wunder_parsed = json.loads(wunder_string)
        context_dict['area_name'] = areas.area_name

        # Note that filter returns >= 1 model instance.
        a_c = areas.area_city
        a_s = areas.area_state
        temp_f_yahoo = (int(weather_yahoo['condition']['temp']) * 9/5) + 32
        temp_f_com = (int(weather_com['current_conditions']['temperature']) * 9/5) + 32
        wunder_current = urllib2.urlopen('http://api.wunderground.com/api/060cb0792aec8a1c/conditions/q/' + areas.area_zip +'.json')
        wunder_current_string = wunder_current.read()
        wunder_current_parsed = json.loads(wunder_current_string)
        temp_f_wunder = int(wunder_current_parsed['current_observation']['temp_f'])

        # Create empty lists for Weather.com forecast data
        forecast_high_c_com = []
        forecast_dayofweek_com = []
        day_temp_com = []

        # Populate forecast temps in celsius and convert fo fahrenheit (Weather.com)
        for x in range(1,4):
            forecast_high_c_com.append((int(weather_com['forecasts'][x]['high']) * 9/5) + 32)

        # Populate days of week
        for x in range(1,4):
            forecast_dayofweek_com.append(weather_com['forecasts'][x]['day_of_week'])

        # Zip the lists together for display
        day_temp_com = zip(forecast_dayofweek_com, forecast_high_c_com)

        # Create empty lists for Weather Underground forecast data
        forecast_high_f_wunder = []
        forecast_dayofweek_wunder = []
        day_temp_wunder = []

        # Populate forecast temps in farhenheit (Weather Underground)
        for x in range(1,4):
            forecast_high_f_wunder.append(wunder_parsed['forecast']['simpleforecast']['forecastday'][x]['high']['fahrenheit'])

        # Populate days of week
        for x in range(1,4):
            forecast_dayofweek_wunder.append(wunder_parsed['forecast']['simpleforecast']['forecastday'][x]['date']['weekday'])
                                          
        # Zip the lists together for display
        day_temp_wunder = zip(forecast_dayofweek_wunder, forecast_high_f_wunder)

        # Create empty lists for Yahoo forecast data
        forecast_high_c_yahoo = []
        forecast_dayofweek_yahoo = []
        day_temp_yahoo = []

        # Populate forecast temps in fahrenheit (Yahoo)
        for x in range(1,4):
            forecast_high_c_yahoo.append((int(weather_yahoo['forecasts'][x]['high']) * 9/5) + 32)

        # Populate days of week
        for x in range(1,4):
            forecast_dayofweek_yahoo.append(weather_yahoo['forecasts'][x]['day'])

        # Convert to full name of day of week
        for day in forecast_dayofweek_yahoo:
            if x == 'Thu':
                x = 'Thursday'
            elif x == 'Fri':
                x = 'Friday'
            elif x == 'Sat':
                x = 'Saturday'
            elif x == 'Sun':
                x = 'Sunday'
            elif x == 'Mon':
                x = 'Monday'
            elif x == 'Tue':
                x = 'Tuesday'
            else:
                x = 'Wednesday'

        # Zip the lists together for display
        day_temp_yahoo = zip(forecast_dayofweek_yahoo, forecast_high_c_yahoo)
        
        # Add variables into context dictionary.
        context_dict['area_city'] = a_c
        context_dict['area_state'] = a_s
        context_dict['yahoo_temp_f'] = temp_f_yahoo
        context_dict['com_temp_f'] = temp_f_com
        context_dict['wunder_temp_f'] = temp_f_wunder
        context_dict['day_temp_com'] = day_temp_com
        context_dict['day_temp_yahoo'] = day_temp_yahoo
        context_dict['day_temp_wunder'] = day_temp_wunder
        
        # Also add the area object from the database.
        # We will use this in teh template to verify that the user exists.
        context_dict['craggarea'] = areas

        # Is area a favorite of current user?
        current_user = UserProfile.objects.get(user__username=request.user)
        user_list = areas.cragg_users.all()
        
        if current_user in user_list:
            user_favorite = True
        else:
            user_favorite = False

        context_dict['user_favorite'] = user_favorite
        context_dict['current_user'] = current_user

    except CraggArea.DoesNotExist:
        # If area doesn't exist...
        # Let the template handle it with a "no area" message.
        pass

    return render (request, 'climbcast/craggarea.html', context_dict)

def add_to_favorites(request, area_name_slug):
    # This view adds a given cragg to a user's favorites list.
    area = CraggArea.objects.get(slug=area_name_slug)
    user_list = area.cragg_users.all()
    current_user = UserProfile.objects.get(user__username=request.user)
    user_favorite = True

    if current_user not in user_list:
        area.cragg_users.add(current_user)
        area.save()
        user_favorite = True
    else:
        user_favorite = False

    
    # Return control to the craggarea view and pass it the area_name_slug.
    return craggarea(request, area_name_slug)


@login_required
def add_cragg_area(request):
    # An HTTP POST?
    if request.method == 'POST':
        form = CraggAreaForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new Cragg to database.
            form.save(commit=True)
            

            #Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CraggAreaForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'climbcast/add_cragg_area.html', {'form': form})


class AddRoute(CreateView):
    model = Route
    form_class = RouteForm
    template_name = 'climbcast/route_form.html'
    success_url = '/climbcast/'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AddRoute, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        route_creater = form.save(commit=False)
        route_creater.created_by = self.request.user
        route_creater.save()
        return HttpResponseRedirect(AddRoute.get_success_url())

class UpdateRoute(UpdateView):
    model = Route
    form_class = RouteForm


    '''
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(add_route, self).dispatch(*args, **kwargs)
    
    def get(self, request):
        form = self.form_class(initial=self.initial)    
        
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            route = form.save(commit=False)

            if 'image_medium' in request.FILES:
                route.image_medium = request.FILES['image_medium']

            route.save()
            updated = True
            return HttpResponseRedirect('/climbcast/')
            
        return render(request, self.template_name, {'form': form, 'updated': updated})
        '''
    
class TickDetailView(DetailView):
    model = RouteTick
    slug_url_kwarg = 'slug'
    template_name = 'climbcast/routetick_detail.html'















        
