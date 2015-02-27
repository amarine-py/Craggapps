from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=255, unique=True)
    user_password = models.CharField(max_length=50)
    user_created = models.DateField(auto_now_add=True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.username
