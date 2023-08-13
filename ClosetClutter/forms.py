from django import forms
from .models import Individual, Family, Subscriber


class IndividuaFormStep1(forms.ModelForm):
    class Meta:
        model = Individual
        fields = ['firstName', 'lastName', 'description', 'telephone', 'mail', 'gender', 'size']
        widgets = {
            'gender': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }


class IndividuaFormStep2(forms.ModelForm):
    class Meta:
        model = Individual
        fields = ['notifyMe']


class FamilyFormStep1(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['name', 'description', 'telephone', 'mail', 'numOfMembers', 'numOfMembersMale', 'numOfMembersFemale',
                  'location', 'additionalInfo', 'members']


class FamilyFormStep2(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['notifyMe']


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', 'phone']
