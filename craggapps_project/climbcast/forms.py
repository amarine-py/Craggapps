from django import forms
from climbcast.models import CraggUser, CraggArea, UserProfile, Route
from django.contrib.auth.models import User

ROUTE_TYPE_CHOICES = ('Trad', 'Sport', 'Ice', 'Mixed', 'Dry', 'Aid', 'Tope Rope', 'Snow')
ROUTE_RATING_CHOICES = ('Third Class', 'Fourth Class', 'Easy Snow', 'Moderate Snow', 'Difficult Snow',
                        'C1', 'C2', 'C3', 'C4', 'C5', 'WI2', 'WI3', 'WI4', 'WI5', 'WI6', 'M3', 'M4',
                        'M5', 'M6', 'M7', 'M8', 'M9', 'M10', 'M11', 'M12', 'M13', 'M14', '5.3', '5.4',
                        '5.5', '5.6', '5.7', '5.8', '5.9', '5.10a', '5.10b', '5.10c', '5.10d', '5.11a',
                        '5.11b', '5.11c', '5.11d', '5.12a', '5.12b', '5.12c', '5.12d', '5.13a', '5.13b',
                        '5.13c', '5.13d', '5.14a', '5.14b', '5.14c', '5.14d', '5.15a')
ROUTE_STARS_CHOICES = ('0', '1', '2', '3', '4')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password',)
        
class CraggAreaForm(forms.ModelForm):
    area_name = forms.CharField(max_length=50, help_text="Enter name of cragg.")
    area_state = forms.CharField(max_length=2, help_text="Enter 2-letter state of cragg.")
    area_city = forms.CharField(max_length=50, required=False, help_text="Enter city of cragg.")
    area_zip = forms.CharField(max_length=5, required=False, help_text="Enter zip code of cragg, if known.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    #cragg_users = forms.ManyToManyField(widget=forms.HiddenInput(), required=False)


    class Meta:
        # Provide an association between the ModelForm and model.        
        model = CraggArea
        fields = ('area_name', 'area_state', 'area_city', 'area_zip', 'area_noaa_station_code', 'cover_image',)
        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        # NEVERMIND - Coudn't get the EXCLUDE to work, so I made it hidden.
        # or specify the fields to include (i.e. not include the cragg)users field)
        # fields = ('area_name', 'area_state', 'area_city')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class RouteForm(forms.ModelForm):
    mp_id = forms.CharField(max_length=9, required=False, help_text='Enter unique MountainProject.com route ID.')
    name = forms.CharField(max_length=100, required=True, help_text='Enter name of route.')
    style = forms.CharField(widget=forms.CheckboxSelectMultiple, choices=ROUTE_TYPE_CHOICE, help_text='Select type of route.')
    rating = forms.CharField(widget=forms.CheckboxSelectMultiple, choices=ROUTE_RATING_CHOICES, help_text='Select difficult rating.')
    stars = forms.CharField(widget=forms.RadioSelect, choices=ROUTE_STARS_CHOICES, help_text='How many stars does this route deserve?')
    pitches = forms.CharField(max_length=3, help_text='Enter number of pitches.')
    city = forms.CharField(max_length=50, help_text='Enter name of city.')
    state = forms.CharField(widget=forms.Select, choices=STATE_CHOICES, help_text='Choose state.') )
    mp_url = forms.URLField(required=False, widget=forms.URLInput, help_text='Enter unique MountainProject.com URL for route.')
    image_medium = forms.ImageField(required=False, widget=forms.FileInput, help_text='Choose a picture for the route.')
    
    class Meta:
        # Provides an association between the ModelForm and the model.
        model = Route
        fields = ('mp_id', 'name', 'style', 'rating', 'stars', 'pitches', 'city', 'state',
                  'mp_url', 'image_medium')

    
