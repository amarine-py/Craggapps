from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from climbcast.models import CraggUser, CraggArea, UserProfile
from climbcast.forms import CraggAreaForm, UserForm, UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
        context_dict['user_name'] = users.user.username

        # Retrieve THE ASSOCIATED AREAS IN THE FUTRE. For now, attributes.
        user_area_list = users.craggarea_set.all()

        # Note that filter returns >= 1 model instance.
        u_e = users.user.email
        f_n = users.user.first_name
        l_n = users.user.last_name

        # Add the variables into the context dictionary.
        context_dict['email_address'] = u_e
        context_dict['first_name'] = f_n
        context_dict['last_name'] = l_n
        context_dict['user_areas'] = user_area_list
        
        # Also add the user object from the database.
        # We will use this in the template to verify that the user exists.
        context_dict['cragguser'] = users       

    except CraggUser.DoesNotExist:
        # If user doesn't exist...
        # Don't do anything - the template displays the "no user" message for us.
        pass

    return render(request, 'climbcast/cragguser.html', context_dict)

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

def add_cragg_user(request):
    # Boolean value for telling template whether registration was successful.
    registered = False
    
    # An HTTP POST?
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # Have we been provided with a valid form?
        if user_form.is_valid() and profile_form.is_valid():
            # Save the new user to database.
            user = user_form.save(commit=True)

            #Now we hash the password.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we can save instance.
            profile.save()

            # Update variable to tell template of success.
            registered = True
            
        else:
            # The supplied form contained errors - just print them to the terminal.
            print user_form.errors
            print profile_form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request,
            'climbcast/add_cragg_user.html', {'user_form': user_form, 'profile_form': profile_form,
            'registered': registered})

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
    
def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/climbcast/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'climbcast/login.html', {})

@login_required
def user_logout(request):
    # Since we know the user must be logged in, we can now log them out
    logout(request)

    # Take user back to homepage
    return HttpResponseRedirect('/climbcast/')














        
