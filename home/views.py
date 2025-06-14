from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

def home_view(request):
    return redirect('show_appointment')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, username = email, password = password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            
            response = redirect('show_appointment')
            response.set_cookie('access_token', access_token, httponly=True)
            response.set_cookie('refresh_token', str(refresh), httponly=True)
            return response
        else:
            return render(request, 'home/login.html', {'error': 'Invalid credentials'})
            
    return render(request, 'home/login.html', {})

def logout_view(request):
    response = redirect('login')
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
    return response