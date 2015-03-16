from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import pywapi
import urllib2
import json


# Create your models here.

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    slug = models.SlugField(unique=True, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

'''
class CraggUser(models.Model):
    username = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(unique=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(CraggUser, self).save(*args, **kwargs)
'''

class CraggArea(models.Model):
    area_name = models.CharField(max_length=50, unique=True)
    area_state = models.CharField(max_length=2)
    area_city = models.CharField(max_length=50)
    area_lat = models.DecimalField(max_digits=7, decimal_places=5, blank=True, null=True)
    area_lon = models.DecimalField(max_digits=8, decimal_places=5, blank=True, null=True)
    area_zip = models.CharField(max_length = 5, blank=True)
    area_noaa_station_code = models.CharField(max_length=6, blank=True)
    slug = models.SlugField(unique=True)
    cragg_users = models.ManyToManyField(UserProfile)
    cover_image = models.ImageField(upload_to='cover_images', blank=True)

    @property
    def get_weather(self):
        
        # This method contains all of the variables and setups for actual weather data.
        # Store appropriate API calls first (and parse JSON data for wunder).
        weather_yahoo = pywapi.get_weather_from_yahoo(self.area_zip)
        weather_com = pywapi.get_weather_from_weather_com(self.area_zip)
        weather_wunder = urllib2.urlopen('http://api.wunderground.com/api/060cb0792aec8a1c/forecast/q/' + self.area_zip +'.json')
        wunder_string = weather_wunder.read()
        wunder_parsed = json.loads(wunder_string)
        # Separate API call for wunder current weather data.
        wunder_current = urllib2.urlopen('http://api.wunderground.com/api/060cb0792aec8a1c/conditions/q/' + self.area_zip +'.json')
        wunder_current_string = wunder_current.read()
        wunder_current_parsed = json.loads(wunder_current_string)

        # Store current conditions for all 3 sites.
        temp_f_yahoo = (int(weather_yahoo['condition']['temp']) * 9/5) + 32
        temp_f_com = (int(weather_com['current_conditions']['temperature']) * 9/5) + 32
        temp_f_wunder = int(wunder_current_parsed['current_observation']['temp_f'])        

        # Create empty lists for Weater.com forecast data.
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

        # Initialize and store appropriate data in context_dict{}.
        context_dict = {}
        context_dict['area_name'] = self.area_name
        context_dict['area_city'] = self.area_city
        context_dict['area_state'] = self.area_state
        context_dict['yahoo_temp_f'] = temp_f_yahoo
        context_dict['com_temp_f'] = temp_f_com
        context_dict['wunder_temp_f'] = temp_f_wunder
        context_dict['day_temp_com'] = day_temp_com
        context_dict['day_temp_yahoo'] = day_temp_yahoo
        context_dict['day_temp_wunder'] = day_temp_wunder

        return context_dict

    def save(self, *args, **kwargs):
        self.slug = slugify(self.area_name)
        super(CraggArea, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.area_name

class Route(models.Model):
    mp_id = models.CharField(max_length=9, blank=True, unique=True)
    name = models.CharField(max_length=100, unique=False)
    style = models.CharField(max_length=10, unique=False, blank=True)
    rating = models.CharField(max_length=15)
    stars = models.CharField(max_length=3, blank=True)
    star_votes = models.CharField(max_length=10, blank=True)
    pitches = models.CharField(max_length=3, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    area1 = models.CharField(max_length=50, blank=True, null=True)
    area2 = models.CharField(max_length=50, blank =True, null=True)
    area3 = models.CharField(max_length=50, blank=True, null=True)
    area4 = models.CharField(max_length=50, blank=True, null=True)
    area5 = models.CharField(max_length=50, blank=True, null=True)
    mp_url = models.URLField(unique=True, blank=True)
    image_small_url = models.URLField(blank=True, null=True)
    image_medium_url = models.URLField(blank=True, null=True)
    image_small = models.ImageField(null=True, blank=True)
    image_medium = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=False)
    users = models.ManyToManyField(UserProfile, null=True, blank=True)
    created_by = models.ForeignKey(User, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name) + '-' + str(self.pk)
        super(Route, self).save(*args, **kwargs)

    def get_route_data(self):
        # This function gets the MP data for a route given it's unique mp_id.
        MP_API_KEY = '&key=106762537-cdd76cb5153460d85b3d72fcdc3391a5'
        action = 'getRoutes&routeIds='
        mp_api_url = 'https://www.mountainproject.com/data?action='
        request_string = mp_api_url + action + self.mp_id + MP_API_KEY
        mp_request = urllib2.urlopen(request_string)
        mp_string = mp_request.read()
        parse = json.loads(mp_string)
        mp_request.close()

        self.name = parse['routes'][0]['name']
        self.style = parse['routes'][0]['type']
        self.rating = parse['routes'][0]['rating']
        self.stars = parse['routes'][0]['stars']
        self.star_votes = parse['routes'][0]['starVotes']
        self.pitches = parse['routes'][0]['pitches']
        self.city = parse['routes'][0]['location'][1]
        self.state = parse['routes'][0]['location'][0]
        self.mp_url = parse['routes'][0]['url']
        self.image_small_url = parse['routes'][0]['imgSmall']
        self.image_medium_url = parse['routes'][0]['imgMed']

        area_list = []

        for area in parse['routes'][0]['location']:
            area_list.append(parse['routes'][0]['location'])

        length_of_area_list = len(area_list)
        if length_of_area_list == 0:
            self.area1 = None
        elif length_of_area_list == 1:
            self.area1 = area_list[0]
        elif length_of_area_list == 2:
            self.area1 = area_list[0]
            self.area2 = area_list[1]
        elif length_of_area_list == 2:
            self.area1 = area_list[0]
            self.area2 = area_list[1]
            self.area3 = area_list[2]
        elif length_of_area_list == 3:
            self.area1 = area_list[0]
            self.area2 = area_list[1]
            self.area3 = area_list[2]
            self.area4 = area_list[3]
        else:
            pass

    def get_absolute_url(self):
        return reverse('route-detail', kwargs={'pk': self.pk})
    
    def __unicode__(self):
        return self.name
    

        


