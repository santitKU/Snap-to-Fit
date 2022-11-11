from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from account.models import Patient
from django.urls import reverse

# Create your models here.
class DailyVitals(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    blood_pressure = models.IntegerField(blank = True, null=True)
    sugar_level = models.IntegerField(blank = True, null=True)
    temperature = models.IntegerField(blank = True, null=True)
    weight = models.IntegerField(blank = True, null=True)
    age = models.IntegerField(blank = True, null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)#either 1 or 0
    height = models.IntegerField(blank = True, null=True)
    bodyfat = models.IntegerField(blank = True, null=True)
    diastolic = models.IntegerField(blank = True, null=True)
    systolic = models.IntegerField(blank = True, null=True)
    gripForce = models.IntegerField(blank = True, null=True)
    situps_count = models.IntegerField(blank = True, null=True)
    sit_bend_forward = models.IntegerField(blank = True, null=True)
    broadjump_cm = models.IntegerField(blank = True, null=True)
    outcome = models.IntegerField(blank = True, null=True)
    bmi = models.IntegerField(blank = True, null=True)
    pregnancy = models.IntegerField(blank = True, null=True)
    

    def __str__(self):
        return str(self.date)

    def get_absolute_url(self):
        return reverse("patient") 