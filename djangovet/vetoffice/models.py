from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.
class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def has_multiple_pets(self):
        return self.patient_set.count() > 1

    def get_absolute_url(self):
        return "list"

class Patient(models.Model):
    breed = models.CharField(max_length=201)
    pet_name = models.CharField(max_length=201)
    age = models.IntegerField(default=0)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    DOG = "DO"
    CAT = "CA"
    BIRD = "BI"
    REPTILE = "RE"
    OTHER = "OT"
    ANIMAL_TYPE_CHOICES = [
        (DOG, "Dog"),
        (CAT, "Cat"),
        (BIRD, "Bird"),
        (REPTILE, "Reptile"),
        (OTHER, "Other")]
    animal_type = models.CharField(max_length=2, choices=ANIMAL_TYPE_CHOICES, default=OTHER)

    def __str__(self):
        return self.pet_name + ", " + self.animal_type

    def get_absolute_url(self):
        return "list"
    class Meta:
        ordering = ["pet_name"]

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    day = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        return '/appointment/list'

    def __str__(self):
        return self.patient.__str__() + "\t" + str(self.day.month) + " " + str(self.day.day) + " " + str(self.day.year) + " " + str(self.time.hour) + " " + str(self.time.min)


