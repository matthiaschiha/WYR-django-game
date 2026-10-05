from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin

# Create your models here.

class WYR_Users(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=40)

    date_joined = models.DateField("Date user joined")

    def __str__(self):
        return self.first_name

    def __str__(self):
        return self.last_name

    def __str__(self):
        return self.username

    def date_joined(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_joined <= now

    

class Category(models.Model):
    #Stores all the categories going to the Scenario
    category = models.CharField(max_length=70)

    def __str__(self):
        return self.category
    

class Scenario(models.Model):
    scenario_question_1 = models.CharField(max_length=75, default="")
    scenario_question_2 = models.CharField(max_length=75, default="")
    votesQ1 = models.IntegerField(default=0)
    votesQ2 = models.IntegerField(default=0)
    category_choice =  models.ManyToManyField(Category)


    date_published = models.DateTimeField("Date scenario was published")

    created_by = models.ForeignKey(WYR_Users, on_delete=models.SET_NULL ,null=True)

    def __str__(self):
        return self.scenario_question_1

    def __str__(self):
        return self.scenario_question_2