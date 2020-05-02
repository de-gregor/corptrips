from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import UserLoginForm, UserRegistrationForm


def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request,user)
        if next:
            return redirect(next)
        return redirect('/')
    
    return render(request, 'settlement/login.html', {'form':form})

def register_view(request):
    form = UserRegistrationForm(request.POST)
    return render(request, 'settlement/register.html', {'form':form})

def home(request):
    return render(request,'settlement/home.html',{})


# Create your views here.
