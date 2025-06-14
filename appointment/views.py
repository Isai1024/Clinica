from django.shortcuts import render
from .models import Appointment
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

def show_appointment(request):
    token = request.COOKIES.get('access_token')
    
    if not token:
        return render(request, 'home/login.html', {'error': 'You must be logged in to view appointments.'})
    
    try:
        jwt_auth = JWTAuthentication()
        validated_token = jwt_auth.get_validated_token(token)
        user = jwt_auth.get_user(validated_token)
    
        appointments = Appointment.objects.all()
        return render(request, 'home/calendar.html', {'appointments': appointments})

    except Exception as e:
        return render(request, 'home/login.html', {'error': 'Invalid token. Please log in again.'})