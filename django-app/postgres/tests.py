from django.test import TestCase

from .models import Ticker

# Create your tests here.
class TickerTestCase(TestCase):

    def setUp(self):
        #Create Ticker
        t1 = Ticker.objects.create(ticker="AAAA")

    def test_number_ticker(self):
        t = Ticker.objects.get(ticker='AAAA')
        print (t)
        self.assertEqual(t.ticker, 'AAAA')