from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Owner, Patient, Appointment
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import OwnerCreateForm, OwnerUpdateForm, PatientCreateForm, AppointmentCreateForm, AppointmentUpdateForm
from django.http import Http404
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
pets = [
   { 'petname': 'Fido', 'animal_type': 'dog'},
   { 'petname': 'Clementine', 'animal_type': 'cat'},
   { 'petname': 'Cleo', 'animal_type': 'cat'},
   { 'petname': 'Oreo', 'animal_type': 'dog'},
]




#@login_required
def home(request):
    '''
    try:
        found_pet = Patient.objects.get(pk=1)
        context = {"name": "Spot", "pets": found_pet}
    except Patient.DoesNotExist:
        raise Http404()
    return render(request, 'vetoffice/home.html', context)
    '''
    context = {"name": request.user}
    return render(request, "vetoffice/home.html", context)

def login_view(request):
    context = {
        "login_view" : "active"
    }
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['password']

        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/owner/list")
        else:
            return HttpResponse("invalid credentials")
    return render(request, "registration/login.html",context )

def logout_view(request):
    logout(request)
    return redirect("home")

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"


class OwnerList(LoginRequiredMixin,ListView):
  model = Owner
  template_name = "vetoffice/owner_list.html"
  context_object_name = "test_list" #this is so it can be addressed in the html template as a variable.

class PatientList(LoginRequiredMixin,ListView):
  model = Patient
  template_name = "vetoffice/patient_list.html"

# Create your other generic views below:

class OwnerCreate(LoginRequiredMixin,CreateView):
  
  model = Owner
  template_name = "vetoffice/owner_create_form.html"
  #fields =  ["first_name", "last_name", "phone"]
  form_class = OwnerCreateForm

class OwnerUpdateView(LoginRequiredMixin,UpdateView):
    model = Owner
    template_name = "vetoffice/owner_update_form.html"
    form_class = OwnerUpdateForm

class OwnerDelete(LoginRequiredMixin,DeleteView):
  model = Owner
  template_name = "vetoffice/owner_delete_form.html"

def OwnerCreate_(request): #disabled
    if request.method == "POST":
        newOwner = Owner()
        newOwner.first_name = request.POST['first_name']
        newOwner.last_name = request.POST["last_name"]
        newOwner.phone_number = request.POST["phone_number"]
        newOwner.save()

class OwnerUpdate_(UpdateView): # disabled
  model = Owner
  template_name = "vetoffice/owner_update_form.html"
  fields =  ["first_name", "last_name", "phone"]



class PatientCreate(LoginRequiredMixin,CreateView):
  model = Patient
  template_name = "vetoffice/patient_create_form.html"
  form_class = PatientCreateForm
  #fields = ["animal_type", "breed", "pet_name", "age", "owner"]

class PatientUpdate(LoginRequiredMixin,UpdateView):
  model = Patient
  template_name = "vetoffice/patient_update_form.html"
  fields = ["animal_type", "breed", "pet_name", "age", "owner"]

class PatientDelete(LoginRequiredMixin,DeleteView):
  model = Patient
  template_name = "vetoffice/patient_delete_form.html"

class AppointmentList(LoginRequiredMixin,ListView):
    model = Appointment
    template_name = "vetoffice/appointment_list.html"

class AppointmentCreate(LoginRequiredMixin,CreateView):
    model = Appointment
    template_name = "vetoffice/appointment_create_form.html"
    form_class = AppointmentCreateForm

class AppointmentUpdate(LoginRequiredMixin,UpdateView):
    model = Appointment
    template_name = "vetoffice/appointment_update_form.html"
    form_class = AppointmentUpdateForm
    
class AppointmentDelete(LoginRequiredMixin,DeleteView):
  model = Appointment
  template_name = "vetoffice/appointment_delete_form.html"