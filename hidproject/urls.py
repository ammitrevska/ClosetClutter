from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ClosetClutter.views import index, charityOrganization, charityDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name="index"),
    path('charity/', charityOrganization, name="charityOrganization"),
    path("charity/<int:charityOrg_id>/", charityDetails, name="charityDetails"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
