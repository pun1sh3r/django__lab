from django.db import models
from django.utils import timezone

# Create your models here.
class Line(models.Model):
    name = models.CharField(unique=True, max_length=200)
    schedule = models.TimeField(default=timezone.now())

    def get_absolute_url(self):
        return "/lines"

    def __str__(self):
        return f"{self.name} : {self.schedule}"

class Station(models.Model):
    name = models.CharField(unique=True, max_length=200)
    accessible = models.BooleanField(default=False)
    age = models.PositiveIntegerField(default=0)
    last_cleaned_date = models.DateField(default=timezone.now())

    def get_absolute_url(self):
        return "/stations"

    def __str__(self):
        return f"{self.name}{' (♿)' if self.accessible else ''}"

class Stop(models.Model):
    line = models.ForeignKey(Line,on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    stop_number = models.PositiveIntegerField()
    class Meta:
        unique_together = (('line','stop_number'))

    def get_absolute_url(self):
        return "/stops"

    def __str__(self):
        return f"{self.line.name} -- {self.station.name} [{self.stop_number}]"