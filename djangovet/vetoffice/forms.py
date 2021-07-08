from django import forms
from django.forms.widgets import SelectDateWidget
from .models import Owner, Patient, Appointment

class OwnerCreateForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'phone',)


class OwnerUpdateForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = "__all__"

class PatientCreateForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

class AppointmentCreateForm(forms.ModelForm):

    class Meta:
        widgets = {"day": SelectDateWidget()}
        model = Appointment
        fields = ('patient', 'day', 'time')

class AppointmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        widgets = {"day": SelectDateWidget()}
        fields = ('patient', 'day', 'time')




