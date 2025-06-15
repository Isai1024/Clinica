from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

# Create your views here.
def show_users(request):
    users = User.objects.all()
    return render(request, 'home/calendar.html', {'users': users})

def user_details(request, id):
    user = User.objects.get(id=id)
    form = UserForm()
    
    form.fields['first_name'].initial = user.first_name
    form.fields['last_name'].initial = user.last_name
    form.fields['email'].initial = user.email
    
    return render(request, 'user/user_form.html', {'form': form})

def create_user(request):
    if request.method == 'POST':
        
        user = User.objects.create_user(
            email=request.POST.get('email'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            password=request.POST.get('password')
        )

        return redirect('/', id=user.id)
    else:
        form = UserForm()
    return render(request, 'user/user_form.html', {'form': form})