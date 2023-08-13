from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ClosetClutter.views import index, charityOrganization, charityDetails, individualsAndFamilies, entityDetails, \
    humanitarianContainers, containerCard, getDirections, containerPic, learnAboutUs, events, eventDetails, \
    IndividualWizardView, successPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name="index"),
    path('charity/', charityOrganization, name="charityOrganization"),
    path("charity/<int:charityOrg_id>/", charityDetails, name="charityDetails"),
    path('individualsAndFamilies/', individualsAndFamilies, name="individualsAndFamilies"),
    path("entity/<int:entity_id>/<str:is_family>/", entityDetails, name="entityDetails"),  # FAMILIES AND INDIVIDUALS
    path("humanitarianContainers/", humanitarianContainers, name="humanitarianContainers"),
    path("containerCard/<int:container_id>/", containerCard, name="containerCard"),
    path("getDirections/<int:container_id>/", getDirections, name="getDirections"),
    path("containerPic/<int:container_id>/", containerPic, name="containerPic"),
    path("learnAboutUs/", learnAboutUs, name="learnAboutUs"),
    path("events/", events, name="events"),
    path("event/<int:event_id>/", eventDetails, name="eventDetails"),
    path('individualForm/', IndividualWizardView.as_view(), name='individualForm'),
    path('success/', successPage, name='successPage'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
