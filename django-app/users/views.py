from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http.response import HttpResponseRedirect
from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.urls import reverse

from postgres.models import *

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return render(request, "admin/dashboard.html")


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

@login_required
def tables_data(request):
    return render(request,'admin/tables-data.html')

@login_required
def tables_basic(request):
    return render(request,'admin/tables-basic.html')

@login_required
def table_ticker(request):
    return render(request,'admin/table-ticker.html',{
        "tickers": Ticker.objects.all()
    })

@login_required
def table_news(request):
    return render(request,'admin/table-news.html',{
        "tickers": Ticker.objects.all()
    })