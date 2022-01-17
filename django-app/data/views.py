"""DOC"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from postgres.models import Ticker
import requests
import json

PUBLIC_TOKEN='OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX'

def index(request):
    response = requests.get('https://eodhistoricaldata.com/api/news?api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX&s=AMZN.US&offset=0&limit=10')
    newsdata = response.json()
    return render(request, 'news/index.html', {
        'title': newsdata[0]['title'],
        'content': newsdata[0]['content'],
        "tickers": Ticker.objects.all()
    })

@login_required
def get_day_news(request):
    ticker = request.GET['ticker']
    print(ticker)
    response = requests.get(f'https://eodhistoricaldata.com/api/news?api_token={PUBLIC_TOKEN}&s={ticker}.US&offset=0&limit=10')
    newsdata = response.json()
    print(response.__getattribute__)
    return render(request, 'news/index.html', {
        'date': newsdata[0]['date'],
        'title': newsdata[0]['title'],
        'content': newsdata[0]['content']
    })