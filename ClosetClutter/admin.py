from django.contrib import admin
from .models import CharityOrg, Family, Individual, Subscriber, Event, HumanitarianContainer
from django.contrib import admin
from .models import CharityOrg, Individual, Family, Subscriber, Event, HumanitarianContainer


class permissionsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


admin.site.register(CharityOrg, permissionsAdmin)
admin.site.register(Individual, permissionsAdmin)
admin.site.register(Family, permissionsAdmin)
admin.site.register(Subscriber, permissionsAdmin)
admin.site.register(Event, permissionsAdmin)
admin.site.register(HumanitarianContainer, permissionsAdmin)
