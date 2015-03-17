from django.contrib import admin
from climbcast.models import CraggArea, UserProfile, Route, RouteTick
from django.contrib.auth.models import User


# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    #prepopulated_fields = {"slug": ("user.username",)}
    pass

'''
class CraggUserAdmin(admin.ModelAdmin):
    #prepopulated_fields = {"slug": ("user.username",)}
    pass
'''

class CraggAreaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("area_name",)}

class RouteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", "mp_id")}

class RouteTickAdmin(admin.ModelAdmin):
    pass

# admin.site.register(CraggUser, CraggUserAdmin)
admin.site.register(CraggArea, CraggAreaAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(RouteTick, RouteTickAdmin)




