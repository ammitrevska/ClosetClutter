from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from ClosetClutter.views import index, charityOrganization, charityDetails, containers, individualsAndFamilies, events, eventDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name="index"),
    path('charity/', charityOrganization, name="charityOrganization"),
    path("charity/<int:charityOrg_id>/", charityDetails, name="charityDetails"),
    path("containers/", containers, name="containers"),
    path("directly/", individualsAndFamilies, name="individualsAndFamilies"),
    path("events/", events, name="events"),
    path("events/<int:eventId>/", eventDetails, name="eventDetails"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
