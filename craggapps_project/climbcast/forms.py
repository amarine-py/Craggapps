from django import forms
from climbcast.models import CraggUser, CraggArea, UserProfile
from django.contrib.auth.models import User

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
    area_noaa_station_code = forms.CharField(max_length=6, help_text="Enter nearest NOAA station code.")
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
    
