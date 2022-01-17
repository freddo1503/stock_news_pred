from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns=[
    path("", views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('tables_data', views.tables_data, name='tables_data'),
    path('tables_basic', views.tables_basic, name='tables_basic'),
    path('table_ticker', views.table_ticker, name='table_ticker'),
    path('table_news,', views.table_news, name='table_news')
]