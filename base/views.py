from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from base.models import  DailyVitals
from account.models import Patient
import joblib
import numpy
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
    template_name = "patientview.html"
    # template_name =  'patient.html'
    model = DailyVitals
    
    
    all_data = DailyVitals.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['vitals_list'] = DailyVitals.objects.filter(patient=self.request.user.patient)
        last_index = DailyVitals.objects.filter(patient=self.request.user.patient).count()
        context['vitals_list'] = DailyVitals.objects.filter(patient=self.request.user.patient)[last_index-1: ]#latest data
        lis= DailyVitals.objects.filter(patient=self.request.user.patient)#all data

        systolic = []
        diastolic = []

        # weight = DailyVitals.objects.get("weight")
        file_name = "time.pkl"
        cls2 = joblib.load(file_name)
        three = cls2.forecast(3)
        

        queryset = DailyVitals.objects.filter(patient=self.request.user.patient)
        for pressure in queryset:
            systolic.append(pressure.systolic)
            diastolic.append(pressure.diastolic)
            weight = pressure.weight
            gender = pressure.gender
            age = pressure.age
            height = pressure.height
            date = pressure.date
            heartrate = pressure.heartrate

        three = three.tolist()
        
        final = diastolic + three

        if (diastolic[-1]>95) and (diastolic[-2]>93)and (diastolic[-3]>90):
            msg = "Your diastolic blood pressure is in Danger Zone. You visit to the doctor"
        else:
            msg = "Your diastolic blood pressure is fine. Maitain this"
        return{'context' : context['vitals_list'],
        'diastolic': final,
        'systolic': systolic,
        'predict' : three,
        'height': height,
        'gender':gender,
        'age': age,
        'weight':weight,
        'date': date,
        'heartrate': heartrate,
        'msg': msg

        }


# class EnterpriseView()

