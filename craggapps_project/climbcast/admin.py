from django.contrib import admin
from climbcast.models import CraggUser, CraggArea, UserProfile


# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    pass
class CraggUserAdmin(admin.ModelAdmin):
    #prepopulated_fields = {"slug": ("User.username",)}
    pass

class CraggAreaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("area_name",)}

admin.site.register(CraggUser, CraggUserAdmin)
admin.site.register(CraggArea, CraggAreaAdmin)
admin.site.register(UserProfile, UserProfileAdmin)




