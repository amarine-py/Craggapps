from django.db import models

# Create your models here.

class User(models.User):
    
    def __unicode__(self):
        return self.username
    
