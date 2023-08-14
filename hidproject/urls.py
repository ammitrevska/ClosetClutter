from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ClosetClutter.views import index, charityOrganization, charityDetails, individualsAndFamilies, entityDetails, \
    humanitarianContainers, containerCard, getDirections, containerPic, learnAboutUs, events, eventDetails, \
    IndividualWizardView, successPage, create_family_step1, create_family_step2, notifyMe

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('index/', index, name="index"),
                  path('charity/', charityOrganization, name="charityOrganization"),
                  path("charity/<int:charityOrg_id>/", charityDetails, name="charityDetails"),
                  path('individualsAndFamilies/', individualsAndFamilies, name="individualsAndFamilies"),
                  path("entity/<int:entity_id>/<str:is_family>/", entityDetails, name="entityDetails"),
                  # FAMILIES AND INDIVIDUALS are entities

                  path("learnAboutUs/", learnAboutUs, name="learnAboutUs"),
                  path("events/", events, name="events"),
                  path("event/<int:event_id>/", eventDetails, name="eventDetails"),
                  path('individualForm/', IndividualWizardView.as_view(), name='individualForm'),
                  path('success/', successPage, name='successPage'),
                  path('create_family/step1/', create_family_step1, name='create_family_step1'),
                  path('create_family/step2/', create_family_step2, name='create_family_step2'),
                  path('notifyMe', notifyMe, name="notifyMe")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



