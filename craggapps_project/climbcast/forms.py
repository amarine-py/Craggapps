from django import forms
from climbcast.models import CraggArea, UserProfile, Route, RouteTick
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    first_name = forms.CharField(help_text="Enter first name of user.")
    last_name = forms.CharField(help_text="Enter last name of user.")
    username = forms.CharField(help_text="Enter a unique username.")
    email = forms.EmailField(help_text="Enter a valid email address.")
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)
        exclude = ['password',]
        
class CraggAreaForm(forms.ModelForm):
    area_name = forms.CharField(max_length=50, help_text="Enter name of cragg.")
    area_state = forms.CharField(max_length=2, help_text="Enter 2-letter state of cragg.")
    area_city = forms.CharField(max_length=50, required=False, help_text="Enter city of cragg.")
    area_zip = forms.CharField(max_length=5, required=False, help_text="Enter zip code of cragg, if known.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    cover_image = forms.ImageField(required=False, widget=forms.FileInput, help_text="Choose a cover picture for the area.")
    #cragg_users = forms.ManyToManyField(widget=forms.HiddenInput(), required=False)


    class Meta:
        # Provide an association between the ModelForm and model.        
        model = CraggArea
        fields = ('area_name', 'area_state', 'area_city', 'area_zip', 'cover_image',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', 'heat_tolerance', 'cold_tolerance', 'mind_windy')

class RouteForm(forms.ModelForm):
    # Define choices constants for form.
    ROUTE_TYPE_CHOICES = (('trad','Trad'), ('sport','Sport'), ('ice','Ice'),
                      ('mixed','Mixed'), ('dry','Dry'), ('aid','Aid'),
                      ('top rope','Tope Rope'), ('snow','Snow'))
    ROUTE_RATING_CHOICES = (('third class','Third Class'), ('fourth class','Fourth Class'),
                        ('easy snow','Easy Snow'), ('moderate snow','Moderate Snow'),
                        ('difficult snow','Difficult Snow'),('C1','C1'), ('C2','C2'),
                        ('C3','C3'), ('C4','C4'), ('C5','C5'), ('WI2','WI2'), ('WI3','WI3'),
                        ('WI4','WI4'), ('WI5','WI5'), ('WI6','WI6'), ('M3','M3'), ('M4','M4'),
                        ('M5','M5'), ('M6','M6'), ('M7','M7'), ('M8','M8'), ('M9','M9'),
                        ('M10','M10'), ('M11','M11'), ('M12','M12'), ('M13','M13'), ('M14','M14'),
                        ('5.3','5.3'), ('5.4','5.4'), ('5.5','5.5'), ('5.6','5.6'), ('5.7','5.7'),
                        ('5.8','5.8'), ('5.9','5.9'), ('5.10a','5.10a'), ('5.10b','5.10b'),
                        ('5.10c','5.10c'), ('5.10d','5.10d'), ('5.11a','5.11a'), ('5.11b','5.11b'),
                        ('5.11c','5.11c'), ('5.11d','5.11d'), ('5.12a','5.12a'), ('5.12b','5.12b'),
                        ('5.12c','5.12c'), ('5.12d','5.12d'), ('5.13a','5.13a'), ('5.13b','5.13b'),
                        ('5.13c','5.13c'), ('5.13d','5.13d'), ('5.14a','5.14a'), ('5.14b','5.14b'),
                        ('5.14c','5.14c'), ('5.14d','5.14d'), ('5.15a','5.15a'))
    ROUTE_STARS_CHOICES = [('0','0'), ('1','1'), ('2','2'), ('3','3'), ('4','4')]
    STATE_CHOICES = [("AL","Alabama"), ("AK","Alaska"), ("AZ","Arizona"), ("AR","Arkansas"),
                 ("CA","California"), ("CO","Colorado"), ("CT","Connecticut"), ("DC","District of Columbia"),
                 ("DE","Delaware!"), ("FL","Florida"), ("GA","Georgia"), ("HI","Hawaii"),
                 ("ID","Idaho"), ("IL","Illinois"), ("IN","Indiana"), ("IA","Iowa"),
                 ("KS","Kansas"), ("KY","Kentucky"), ("LA","Louisiana"), ("ME","Maine"),
                 ("MD","Maryland"), ("MA","Massachusetts"), ("MI","Michigan"), ("MN","Minnesota"),
                 ("MS","Mississippi"), ("MO","Missouri"), ("MT","Montana"), ("NE","Nebraska"),
                 ("NV","Nevada"), ("NH","New Hampshire"), ("NJ","New Jersey"), ("NM","New Mexico"),
                 ("NY","New York"), ("NC","North Carolina"), ("ND","North Dakota"), ("OH","Ohio"),
                 ("OK","Oklahoma"), ("OR","Oregon"), ("PA","Pennsylvania"), ("RI","Rhode Island"),
                 ("SC","South Carolina"), ("SD","South Dakota"), ("TN","Tennessee"), ("TX","Texas"),
                 ("UT","Utah"), ("VT","Vermont"), ("VA","Virginia"), ("WA","Washington"),
                 ("WV","West Virginia"), ("WI","Wisconsin"), ("WY","Wyoming")]
        
    mp_id = forms.CharField(max_length=9, required=False, help_text='Enter unique MountainProject.com route ID.')
    name = forms.CharField(max_length=100, required=True, help_text='Enter name of route.')
    style = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=ROUTE_TYPE_CHOICES, help_text='Choose the type of route this is.')
    rating = forms.MultipleChoiceField(widget=forms.SelectMultiple, choices=ROUTE_RATING_CHOICES, help_text='Select difficulty rating.')
    stars = forms.ChoiceField(widget=forms.RadioSelect, choices=ROUTE_STARS_CHOICES, help_text='How many stars does this route deserve?')
    pitches = forms.CharField(max_length=3, help_text='Enter number of pitches.')
    city = forms.CharField(max_length=50, help_text='Enter the name of the closest city.')
    state = forms.ChoiceField(widget=forms.Select, choices=STATE_CHOICES, help_text='Choose the state this route is in.')
    mp_url = forms.URLField(required=False, widget=forms.URLInput, help_text='Enter unique MountainProject.com URL for route.')
    image_medium = forms.ImageField(required=False, widget=forms.FileInput, help_text='Choose a cover picture for the route.')
    
    class Meta:
        # Provides an association between the ModelForm and the model.
        model = Route
        exclude = ('created_by',)
        fields = ('mp_id', 'name', 'style', 'rating', 'stars', 'pitches', 'city', 'state',
                  'mp_url', 'image_medium')

class UpdateUserForm(forms.ModelForm):
    success_url = '/cragguser/'
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        
class UpdateUserProfileForm(forms.ModelForm):
    HEAT_TOLERANCE_CHOICES = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))
    COLD_TOLERANCE_CHOICES = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))
    heat_tolerance = forms.ChoiceField(widget=forms.Select, choices=HEAT_TOLERANCE_CHOICES, help_text="What is your tolerance for heat?")
    cold_tolerance = forms.ChoiceField(choices=COLD_TOLERANCE_CHOICES, help_text="What is your tolerance for cold?")
    mind_windy = forms.NullBooleanField(help_text="Do you mind climbing in windy conditions?")
    picture = forms.ImageField(required=False, widget=forms.FileInput, help_text="Choose a profile picture (optional).")
    success_url = '/cragguser/'

    class Meta:
        model = UserProfile
        fields = ('heat_tolerance', 'cold_tolerance', 'mind_windy', 'picture',)
