from django import forms
from climbcast.models import CraggUser, CraggArea

class CraggUserForm(forms.ModelForm):
    username = forms.CharField(max_length=50, help_text="Enter a unique username.")
    first_name = forms.CharField(max_length=50, help_text="Enter your first name.")
    last_name = forms.CharField(max_length=50, help_text="Enter your last name.")
    user_email = forms.EmailField(max_length=255, help_text="Enter your email address.")
    user_password = forms.CharField(max_length=50, help_text="Enter your password.")
    user_created = forms.DateField(widget=forms.HiddenInput(), required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    favorites = forms.ModelMultipleChoiceField(queryset=CraggArea.objects.all())

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = CraggUser
        fields = ('username', 'first_name', 'last_name', 'user_email', 'user_password')

class CraggAreaForm(forms.ModelForm):
    area_name = forms.CharField(max_length=50, help_text="Enter name of cragg.")
    area_state = forms.CharField(max_length=2, help_text="Enter 2-letter state of cragg.")
    area_city = forms.CharField(max_length=50, required=False, help_text="Enter city of cragg.")
    area_zip = forms.CharField(max_length=5, required=False, help_text="Enter zip code of cragg, if known.")
    area_noaa_station_code = forms.CharField(max_length=6, help_text="Enter nearest NOAA station code.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)


class Meta:
    # Provide an association between the ModelForm and model.        
    model = CraggArea

    # What fields do we want to include in our form?
    # This way we don't need every field in the model present.
    # Some fields may allow NULL values, so we may not want to include them...
    # Here, we are hiding the foreign key.
    # we can either exclude the category field from the form,
    exclude=('cragg_users')
    # or specify the fields to include (i.e. not include the cragg)users field)
    # fields = ('area_name', 'area_state', 'area_city')
