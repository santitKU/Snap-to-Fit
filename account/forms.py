from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from .models import User, Doctor, Patient, Enterprise
from django import forms

class PatientSignUpForm(UserCreationForm):
    doctor = forms.ModelMultipleChoiceField(queryset=User.objects.all().filter(is_doctor=True),
        widget=forms.CheckboxSelectMultiple,
        required=True)
    

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        Patient.objects.create(user=user, doctor = Doctor.objects.get(user_id=self.cleaned_data['doctor'][0]))
        #patient.doctor.add(self.cleaned_data['doctor']) 
        return user

class DoctorSignUpForm(UserCreationForm):


    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
        Doctor.objects.create(user=user)
        
        return user

class EnterpriseSignUpForm(UserCreationForm):


    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_enterprise = True
        if commit:
            user.save()
        Enterprise.objects.create(user=user)
        
        return user
