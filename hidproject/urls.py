from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path

from ClosetClutter.views import index, charityOrganization, charityDetails, individualsAndFamilies, entityDetails, \
    containers, learnAboutUs, events, eventDetails, \
    IndividualWizardView, create_family_step1, create_family_step2, notifyMe, applyForAid, successPage

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('index/', index, name="index"),
                  path('charity/', charityOrganization, name="charityOrganization"),
                  path("charity/<int:charityOrg_id>/", charityDetails, name="charityDetails"),
                  path('directly/', individualsAndFamilies, name="individualsAndFamilies"),
                  path("entity/<int:entity_id>/<str:is_family>/", entityDetails, name="entityDetails"),
                  # FAMILIES AND INDIVIDUALS are entities
                  path("containers/", containers, name="containers"),
                  path("learnAboutUs/", learnAboutUs, name="learnAboutUs"),
                  path("events/", events, name="events"),
                  path("event/<int:event_id>/", eventDetails, name="eventDetails"),
                  path('individualForm/', IndividualWizardView.as_view(), name='individualForm'),
                  path('create_family/step1/', create_family_step1, name='create_family_step1'),
                  path('create_family/step2/', create_family_step2, name='create_family_step2'),
                  path('notifyMe', notifyMe, name="notifyMe"),
                  path('', lambda request: redirect('index/')),
                  path('applyForAid/', applyForAid, name="applyForAid"),
                  path('successPage/', successPage, name="successPage"),
                  path('entity/<int:entity_id>/<str:is_family>', entityDetails, name='entityDetails')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
