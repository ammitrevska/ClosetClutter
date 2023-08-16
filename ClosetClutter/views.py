from django.shortcuts import render, get_object_or_404
from .forms import IndividuaFormStep1, IndividuaFormStep2 , FamilyFormStep1, FamilyFormStep2, SubscriberForm
from .models import CharityOrg, Individual, Family, HumanitarianContainer, Event, Subscriber
from django.shortcuts import render, redirect
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


def containers(request):
    return render(request, "containers.html")


def individualsAndFamilies(request):
    qs = Family.objects.all()
    qs = Individual.objects.all(
    )
    return render(request, "individualsAndFamilies.html")


def events(request):
    qs = Event.objects.all()
    context = {"events": qs}
    return render(request, "events.html", context=context)


def eventDetails(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    context = {"event": event}
    return render(request, "eventDetails.html", context=context)


def getNotified(request):
    return render(request, "getNotified.html")


def entityDetails(request, entity_id, is_family):
    is_family_bool = is_family.lower() == 'true'
    if (is_family_bool):
        entity = get_object_or_404(Family, pk=entity_id)
    else:
        entity = get_object_or_404(Individual, pk=entity_id)
    context = {"entity": entity}
    return render(request, "entityDetails.html", context=context)

  
def learnAboutUs(request):
    return render(request, "learnAboutUs.html")


class IndividualWizardView(SessionWizardView):
    template_name = 'individualForm.html'
    form_list = [IndividuaFormStep1, IndividuaFormStep2]

    def done(self, form_list, **kwargs):
        # Combine data from all form steps
        combined_data = {}
        for form in form_list:
            if form.is_valid():
                combined_data.update(form.cleaned_data)
            else:
                # Handle form errors here if needed
                return self.render_revalidation_failure(form)

        individual = Individual(**combined_data)
        individual.save()

        return redirect('successPage')  # Redirect to a success page


def create_family_step1(request):
    if request.method == 'POST':
        form = FamilyFormStep1(request.POST)
        if form.is_valid():
            family_data = {
                'name': form.cleaned_data['name'],
                'members': list(form.cleaned_data['members'].values_list('id', flat=True)),
                'description': form.cleaned_data['description'],
                'telephone': form.cleaned_data['telephone'],
                'mail': form.cleaned_data['mail'],
                'numOfMembers': form.cleaned_data['numOfMembers'],
                'numOfMembersMale': form.cleaned_data['numOfMembersMale'],
                'numOfMembersFemale': form.cleaned_data['numOfMembersFemale'],
                'location': form.cleaned_data['location'],
                'additionalInfo': form.cleaned_data['additionalInfo'],
            }
            request.session['family_data'] = family_data
            return redirect('create_family_step2')
    else:
        form = FamilyFormStep1()

    context = {'form': form}
    return render(request, 'family_form_step1.html', context)


def create_family_step2(request):
    family_data = request.session.get('family_data', {})

    if request.method == 'POST':
        form = FamilyFormStep2(request.POST)
        if form.is_valid():
            members = family_data['members']
            family = Family.objects.create(name=family_data['name'],
                                           description=family_data['description'],
                                           telephone=family_data['telephone'],
                                           mail=family_data['mail'],
                                           numOfMembers=family_data['numOfMembers'],
                                           numOfMembersMale=family_data['numOfMembersMale'],
                                           numOfMembersFemale=family_data['numOfMembersFemale'],
                                           location=family_data['location'],
                                           additionalInfo=family_data['additionalInfo'],
                                           notifyMe=form.cleaned_data['notifyMe'], )
            family.members.set(members)  # Use set() to update the many-to-many relationship
            return redirect('successPage')

    else:
        form = FamilyFormStep2()

    context = {'form': form}
    return render(request, 'family_form_step2.html', context)


def notifyMe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'notifyMe.html')  # Render a success page or redirect
    else:
        form = SubscriberForm()

    return render(request, 'notifyMe.html', {'form': form})
