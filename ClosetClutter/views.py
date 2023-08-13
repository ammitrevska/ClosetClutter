from django.shortcuts import render, get_object_or_404
from .models import CharityOrg, Individual, Family, HumanitarianContainer, Event


# Create your views here.
def index(request):
    events = Event.objects.all()
    context = {"events": events}
    return render(request, "index.html", context=context)


def charityOrganization(request):
    qs = CharityOrg.objects.all()  # Fetch all entries from the database
    context = {"charities": qs}
    return render(request, "charityOrganization.html", context=context)


def charityDetails(request, charityOrg_id):
    charity = get_object_or_404(CharityOrg, pk=charityOrg_id)
    context = {"charity": charity}
    return render(request, "charityDetails.html", context=context)
