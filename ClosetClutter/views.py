from django.shortcuts import render, get_object_or_404
from .models import CharityOrg, Individual, Family, HumanitarianContainer, Event
from django.shortcuts import render, redirect
from .forms import IndividuaFormStep1, IndividuaFormStep2
from formtools.wizard.views import SessionWizardView


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


def individualsAndFamilies(request):
    individuals = Individual.objects.all()
    families = Family.objects.all()
    context = {"individuals": individuals,
               "families": families}
    return render(request, "individualsAndFamilies.html", context=context)


def entityDetails(request, entity_id, is_family):
    is_family_bool = is_family.lower() == 'true'
    if (is_family_bool):
        entity = get_object_or_404(Family, pk=entity_id)
    else:
        entity = get_object_or_404(Individual, pk=entity_id)
    context = {"entity": entity}
    return render(request, "entityDetails.html", context=context)


def humanitarianContainers(request):
    containers = HumanitarianContainer.objects.all()  # Fetch all entries from the database
    context = {"containers": containers}
    return render(request, "humanitarianContainers.html", context=context)


def containerCard(request, container_id):
    container = get_object_or_404(HumanitarianContainer, pk=container_id)
    context = {"container": container}
    return render(request, "container.html", context=context)


def getDirections(request, container_id):
    container = get_object_or_404(HumanitarianContainer, pk=container_id)
    context = {"container": container}
    return render(request, "getDirections.html", context=context)


def containerPic(request, container_id):
    container = get_object_or_404(HumanitarianContainer, pk=container_id)
    context = {"container": container}
    return render(request, "containerPic.html", context=context)


def learnAboutUs(request):
    return render(request, "learnAboutUs.html")


def events(request):
    events = Event.objects.all()
    context = {"events": events}
    return render(request, "events.html", context=context)


def eventDetails(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    context = {"event": event}
    return render(request, "eventDetails.html", context=context)


class IndividualWizardView(SessionWizardView):
    template_name = 'individualForm.html'
    form_list = [IndividuaFormStep1, IndividuaFormStep2]

    def done(self, form_list, **kwargs):
        # Combine data from all form steps
        combined_data = {}
        for form in form_list:
            combined_data.update(form.cleaned_data)

        individual = Individual(**combined_data)
        individual.save()

        return redirect('successPage')  # Redirect to a success page


def successPage(request):
    return render(request, "successPage.html")
