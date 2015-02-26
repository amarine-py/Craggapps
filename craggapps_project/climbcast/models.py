from django.db import models

# Create your models here.
<<<<<<< HEAD
<<<<<<< HEAD
=======

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=255, unique=True)
    user_password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username
    
>>>>>>> parent of f7a69e5... Revert "Bad commit"
=======

class User(models.User):
    
    def __unicode__(self):
        return self.username
    
>>>>>>> parent of ba92341... Revert "Third commit"
