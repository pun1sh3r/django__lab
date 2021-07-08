from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Choice,Week

# this is to add fields to UserCreationForm
class UserForm(UserCreationForm):

    age = forms.IntegerField()
    year = forms.IntegerField()
    class Meta:
        model= User
        fields = ('age','year','username','email','password1','password2')

class DessertCreateForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'