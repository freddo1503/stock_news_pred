"""To display data from the database"""
from django.shortcuts import render

from .models import *

# Create your views here.
def index (request):
    """Methode to choose the table you want to show"""
    return render(request, "database/index.html", {
        "tickers": Ticker.objects.all()# pylint: disable=maybe-no-member
    })

def tickers (request):
    """Methode to get all the data in the ticker table"""
    return render(request, "tickers/index.html", {
        "tickers": Ticker.objects.all()# pylint: disable=maybe-no-member
    })

def news (request):
    """Methode to get all the news according to the date chosen"""
    return render(request, "ticker/index.html", {
        "tickers": News.objects.all()# pylint: disable=maybe-no-member
    })

def tweets (request):
    """Methode to get all the tweets according to the date chosen"""
    return render(request, "ticker/index.html", {
        "tickers": Tweets.objects.all()# pylint: disable=maybe-no-member
    })

def stocks (request):
    """Methode to get all the prices according to the date and the ticker chosen"""
    return render(request, "ticker/index.html", {
        "tickers": Stocks.objects.all()# pylint: disable=maybe-no-member
    })
    