from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm, LoginForm




def home_view(request):
    context = {}
    return render(request, 'user/home.html',context)


def register_view(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 == password2:
                user.set_password(password1)
                user.save()
                login(request, user)
                return redirect('offer-home')
    else:
        form = RegisterForm()
    context = {'form':form}
    return render(request, 'user/register.html',context)

def login_view(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('offer-home')
            else:
                print("none")
    else:
        form = LoginForm()

    context = {'form':form}
    return render(request, 'user/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('offer-home')