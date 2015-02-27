from django.contrib import admin
from climbcast.models import CraggUser

# Register your models here.

class CraggUserAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("username",)}

admin.site.register(CraggUser, CraggUserAdmin)


