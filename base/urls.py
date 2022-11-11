from django.urls import path,include
from base.views import DoctorView,  DoctorDetailView, EnterpriseCreateView, HomeView, PatientView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('doctor', DoctorView.as_view(), name='doctor'),
    path('patient', PatientView.as_view(), name='patient'),
    path('<int:pk>', DoctorDetailView.as_view(), name="patient_detail_view"),
    path('add_record', EnterpriseCreateView.as_view(), name="add_record"),
    path('home/', HomeView.as_view(), name='home')

]