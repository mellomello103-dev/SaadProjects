from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

# LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('myFirstapp:home')
        else:
            return HttpResponse('Invalid username or password')

    return render(request, 'login.html')


# REGISTER
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #for #ing password
        User.objects.create_user(username=username, password=password)

        return redirect('myFirstapp:login')

    return render(request, 'register.html')


# HOME


@login_required(login_url='myFirstapp:login')
def home(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    context = {
        'balance': profile.balance
    }

    return render(request, 'home.html', context)


def withdraw(request):
    if request.method == 'POST':
        amount = float(request.POST['amount'])
        profile = Profile.objects.get(user=request.user)

        if profile.withdraw(amount):
            return redirect('myFirstapp:home')
        else:
            return HttpResponse('Insufficient balance')

    return render(request, 'home.html')

# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('myFirstapp:login')
