from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.

    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class CraggUser(models.Model):
    username = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(unique=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(CraggUser, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.username

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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.area_name)
        super(CraggArea, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.area_name


