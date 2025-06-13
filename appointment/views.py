from django.shortcuts import render
from .models import Appointment

# Create your views here.

def show_appointment(request):
    appointments = Appointment.objects.all()
    return render(request, 'home/calendar.html', {'appointments': appointments})