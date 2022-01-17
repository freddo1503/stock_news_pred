from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_news', views.get_day_news, name='add_news')
]