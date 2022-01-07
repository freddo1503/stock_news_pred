"""List of all urls allowed that can be accessed from /postgres"""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("ticker", views.tickers, name="ticker"),
    path("news", views.news, name="news"),
    path("tweets", views.tweets, name="tweets"),
    path("stocks", views.stocks, name="stocks")
]
