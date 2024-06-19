from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    fn = forms.CharField(label='First Name')
    ln = forms.CharField(label='Last Name')
    tech = forms.CharField(label='Technologies')
    email = forms.EmailField(label ='Email Id')
    photo = forms.FileField(label = 'Select Photo')
    class Meta:
        model = Info
        fields = '__all__'
