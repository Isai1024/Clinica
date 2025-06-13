from django.shortcuts import render
import bcrypt
from .models import User
from .forms import UserForm

# Create your views here.
def show_users(request):
    users = User.objects.all()
    return render(request, 'home/calendar.html', {'users': users})

def user_details(request, user_id):
    user = User.objects.get(user_id=user_id)
    form = UserForm()
    
    form.fields['first_name'].initial = user.first_name
    form.fields['last_name'].initial = user.last_name
    form.fields['email'].initial = user.email
    
    return render(request, 'user/user_form.html', {'form': form})

def create_user(request):
    if request.method == 'POST':
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        
        password = request.POST.get('password')

        bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytes, salt)

        encrypted_password = hash
        salt = salt
        
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            encrypted_password=encrypted_password,
            salt=salt
        ).save()

        return render(request, 'home/calendar.html', {'user': user})
    else:
        form = UserForm()
    return render(request, 'user/user_form.html', {'form': form})