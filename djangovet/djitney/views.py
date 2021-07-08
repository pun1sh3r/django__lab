from django.shortcuts import render
from .models import Line, Station, Stop
from .forms import StopForm, StationForm, LineForm
from django.views.generic import TemplateView
# Create your views here.

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class HomeView(TemplateView):
    template_name = 'djitney/home.html'

    def get_context_data(self):
        context = super().get_context_data()
        context["lines"] = Line.objects.all()
        context["stations"] = Station.objects.all()
        context["stops"] = Stop.objects.all()
        return context

class LinesView(ListView):
    model = Line
    template_name = 'djitney/lines.html'

class CreateLineView(CreateView):
    model = Line
    template_name = 'djitney/add_line.html'
    form_class = LineForm


class UpdateLineView(UpdateView):
    model = Line
    template_name = 'djitney/update_line.html'
    form_class = LineForm

class DeleteLineView(DeleteView):
    model = Line
    template_name = 'djitney/delete_line.html'


class StationsView(ListView):
    model = Station
    template_name = 'djitney/stations.html'

class CreateStationView(CreateView):
    model = Station
    template_name = 'djitney/add_station.html'
    form_class = StationForm


class UpdateStationView(UpdateView):
    model = Station
    template_name = 'djitney/update_station.html'
    form_class = StationForm

class DeleteStationView(DeleteView):
    model = Station
    template_name = 'djitney/delete_station.html'

class StopsView(ListView):
    model = Stop
    template_name = 'djitney/stops.html'


class CreateStopView(CreateView):
    model = Stop
    template_name = 'djitney/add_stop.html'
    form_class = StopForm


class UpdateStopView(UpdateView):
    model = Stop
    template_name = 'djitney/update_stop.html'
    form_class = StopForm

class DeleteStopView(DeleteView):
    model = Stop
    template_name = 'djitney/delete_stop.html'