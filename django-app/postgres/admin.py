from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Ticker)
admin.site.register(News)
admin.site.register(Tweets)
admin.site.register(Stocks)
