from django.shortcuts import render, get_object_or_404
from .models import State, Attraction
from .forms import StateCreateForm, AttractionCreateForm, StateUpdateForm, AttractionUpdateForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView


# Create your views here.
from django.shortcuts import render

# This is the dictionary for all the attractions
attractions = [
  { 'attraction_name' : 'Niagra Falls', 'state' : 'New York'},
  { 'attraction_name' : 'Grand Canyon National Park', 'state' : 'Arizona'},
  { 'attraction_name' : 'Mall of America', 'state' : 'Minnesota'},
  { 'attraction_name' : 'Mount Rushmore', 'state' : 'South Dakota'},
  { 'attraction_name' : 'Times Square', 'state' : 'New York'},
  { 'attraction_name' : 'Walt Disney World', 'state' : 'Florida'}
]

def home(request):
  # The context is all of the variables we want passed into the template.
  context = {"attractions" : attractions}
  return render(request, 'touristAttractions/home.html', context)

def details(request, statename):
  # We replace the dash with a space for later ease of use. The dash is there because of the slugify filter.
  context = {"attractions" : attractions, "statename" : statename.replace("-", " ")}
  return render(request, 'touristAttractions/details.html', context)

class StateList(ListView):
  model = State
  template_name = "touristAttractions/list.html"
  #context_object_name = "test_lister"



class StateCreate(CreateView):
  model = State
  form_class = StateCreateForm
  template_name = "touristAttractions/state_create_form.html"


class StateDelete(DeleteView):
  model = State
  template_name = "touristAttractions/state_delete_form.html"

class StateUpdate(UpdateView):
  model = State
  template_name = "touristAttractions/state_update_form.html"
  form_class = StateUpdateForm

class AttractionCreate(CreateView):
  model = Attraction
  form_class = AttractionCreateForm
  template_name = "touristAttractions/attraction_create_form.html"

class AttractionList(ListView):
  model = Attraction
  template_name = "touristAttractions/list.html"

class AttractionDelete(DeleteView):
  model = Attraction
  template_name = "touristAttractions/attraction_delete_form.html"

class AttractionUpdate(UpdateView):
  model = Attraction
  template_name = "touristAttractions/attraction_update_form.html"
  form_class = AttractionUpdateForm