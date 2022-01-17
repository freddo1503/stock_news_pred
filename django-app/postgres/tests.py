from django.test import TestCase, Client

from .models import Ticker
from .views import *

# Create your tests here.
class TickerTestCase(TestCase):

    def setUp(self):
        #Create Ticker
        t1 = Ticker.objects.create(ticker="AAAA")

    def test_number_ticker(self):
        t = Ticker.objects.get(ticker='AAAA')
        print (t)
        self.assertEqual(t.ticker, 'AAAA')
        