from django.contrib import admin
from account.models import Doctor, Patient, User
# Register your models here.
admin.site.register(Patient)
admin.site.register(User)
admin.site.register(Doctor)