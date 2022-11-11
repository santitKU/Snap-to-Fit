from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from base.models import  DailyVitals
from account.models import Patient
# Create your views here.

class HomeView(TemplateView):
    template = "home.html"

class DoctorView(ListView):
    template_name =  'doctorview.html'
    model = Patient
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patients_list = Patient.objects.filter(doctor=self.request.user.doctor)
        context['patients_list'] = patients_list
        return context

class DoctorDetailView(TemplateView):
    template_name = "detail_view.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        vitals_list = []
        for value in DailyVitals.objects.all():
            if value.patient.user.id == self.kwargs.get('id'):
                vitals_list.append(value)

        context['vitals_list'] = vitals_list
        return context


class EnterpriseCreateView(CreateView):
    model = DailyVitals
    template_name =  'add_record.html'
    fields =  ['sugar_level', 'blood_pressure', 'temperature', 'weight', 'age', 'gender', 'height', 'bodyfat', 'diastolic', 'systolic', 'gripForce', 'situps_count', 'sit_bend_forward', 'broadjump_cm', 'outcome', 'bmi', 'pregnancy']

    def form_valid(self, form):
        form.instance.patient = self.request.user.patient
        return super().form_valid(form)

class PatientView(TemplateView):
    template = "patientview.html"

# class EnterpriseView()

