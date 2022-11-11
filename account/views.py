from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import User
from django.contrib.auth import login
from django.shortcuts import redirect
from .forms import PatientSignUpForm, DoctorSignUpForm, EnterpriseSignUpForm
from django.shortcuts import redirect
from django.http import HttpResponse


# Create your views here.
class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


class PatientSignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('create_record')


class DoctorSignUpView(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('doctor')


class EnterpriseSignUpView(CreateView):
    model = User
    form_class = EnterpriseSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'enterprise'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('doctor')


def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if request.user.is_patient:
        # user is an admin
        return redirect("http://127.0.0.1:8000/patient")
    elif request.user.is_doctor:
        return redirect("http://127.0.0.1:8000/doctor")
    elif request.user.is_patient:
        return redirect("http://127.0.0.1:8000/enterprise")
        