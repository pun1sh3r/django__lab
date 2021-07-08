import datetime
from django.utils import timezone
from django.db import models

class Week(models.Model):
  pub_date = models.DateTimeField("date published")

  def start_of_week(self):
      today = datetime.date.today()
      start_of_week = today + datetime.timedelta(days=-today.weekday(), weeks=1)
      return start_of_week

  def was_published_recently(self):
      return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
  week = models.ForeignKey(Week, on_delete=models.CASCADE)
  dessert_choice = models.CharField(max_length=200)
  dessert_details = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  def __str__(self):
    return self.dessert_choice