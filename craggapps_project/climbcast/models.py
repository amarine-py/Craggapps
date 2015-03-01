from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class CraggUser(models.Model):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=255, unique=True)
    user_password = models.CharField(max_length=50)
    user_created = models.DateField(auto_now_add=True)
    slug = models.SlugField(unique=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(CraggUser, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.username

class CraggArea(models.Model):
    area_name = models.CharField(max_length=50, unique=True)
    area_state = models.CharField(max_length=2)
    area_city = models.CharField(max_length=50)
    area_lat = models.DecimalField(max_digits=7, decimal_places=5, blank=True)
    area_lon = models.DecimalField(max_digits=8, decimal_places=5, blank=True)
    area_zip = models.CharField(max_length = 5, blank=True)
    area_noaa_station_code = models.CharField(max_length=6, blank=True)
    '''
    area_current_temp_yahoo_c = models.DecimalField(max_digits=5, decimal_places=2, required=False)
    area_current_temp_yahoo_f = models.DecimalField(max_digits=5, decimal_places=2, required=False)
    area_current_temp_weathercom_c = models.DecimalField(max_digits=5, decimal_places=2, required=False)
    area_current_temp_weathercom_f = models.DecimalField(max_digits=5, decimal_places=2, required=False)
    area_current_temp_noaa_c = models.DecimalField(max_digits=5, decimal_places=2, required=False)
    area_current_temp_noaa_f = models.DecimalField(max_digits=5, decimal_places=2, required=False)
    area_humidity_yahoo = models.PositiveSmallIntegerField(required=False)
    area_humidity_weathercom = models.PositiveSmallIntegerField(required=False)
    area_humidity_noaa = models.PositiveSmallIntegerField(required=False)
    area_pressure_yahoo_mb = models.DecimalField(max_digits=6, decimal_places=2, required=False)
    area_pressure_weathercom_mb = models.DecimalField(max_digits=6, decimal_places=2, required=False)
    area_pressure_noaa_mb = models.DecimalField(max_digits=6, decimal_places=2, required=False)
    area_wind_speed_yahoo_kmh = models.PositiveSmallIntegerField(required=False)
    area_wind_speed_weathercom_kmh_string = models.CharField(max_length=15, required=False)
    area_wind_speed_noaa_mph = models.PositiveSmallIntegerField(required=False)
    '''
    slug = models.SlugField(unique=True)
    cragg_users = models.ManyToManyField(CraggUser)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.area_name)
        super(CraggArea, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.area_name
