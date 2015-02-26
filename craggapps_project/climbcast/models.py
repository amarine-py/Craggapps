from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=255, unique=True)
    user_password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username
