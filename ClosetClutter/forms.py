from django import forms
from .models import Individual


class IndividuaFormStep1(forms.ModelForm):
    class Meta:
        model = Individual
        fields = ['firstName', 'lastName', 'description', 'telephone', 'mail', 'gender', 'size']


class IndividuaFormStep2(forms.ModelForm):
    class Meta:
        model = Individual
        fields = ['notifyMe']
