from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, "admin/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'users/login.html', {
                'message':'Invalid credentials.'
            })
    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {
        'message':'Logged out.'
    })

def tables_data(request):
    return render(request,'admin/tables-data.html')

def tables_basic(request):
    pass