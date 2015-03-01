from django.contrib import admin
from climbcast.models import CraggUser, CraggArea

# Register your models here.

class CraggUserAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("username",)}

class CraggAreaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("area_name",)}

admin.site.register(CraggUser, CraggUserAdmin)
admin.site.register(CraggArea, CraggAreaAdmin)



