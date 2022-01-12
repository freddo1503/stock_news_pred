from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns=[
    path("home", views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('tables_data', views.tables_data, name='tables_data')
]