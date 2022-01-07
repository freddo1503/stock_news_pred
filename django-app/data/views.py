
from django.shortcuts import render
import requests
import json

def index(request):
    response = requests.get('https://eodhistoricaldata.com/api/news?api_token=OeAFFmMliFG5orCUuwAKQ8l4WWFQ67YX&s=AMZN.US&offset=0&limit=10')
    newsdata = response.json()
    print (newsdata)
    return render(request, 'news/index.html', {
        'title': newsdata[0]['title'],
        'content': newsdata[0]['content']
    })
