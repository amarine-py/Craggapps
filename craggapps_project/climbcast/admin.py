from django.contrib import admin
from climbcast.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("username",)}

admin.site.register(User, UserAdmin)


