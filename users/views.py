from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        username = User.objects.get(email=email).username

        user = authenticate(username=username, password=password)
        print(user, email, password)
        if user is not None:
            login(request, user)
            return render(request,'users/dashboard.html')
        else:
            return render(request,'users/login.html')

    return render(request,'users/login.html')

def dashboard(request):
    return render(request, 'users/dashboard.html')