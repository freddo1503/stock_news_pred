"""Database Design"""

from django.db import models

# Create your models here.
class Ticker(models.Model):
    """Ticker table"""
    ticker = models.CharField(max_length=80, primary_key=True)

    def get_all(self):
        """Return all the ticker"""
        return self.ticker

class News (models.Model):
    """News table"""
    title = models.TextField(default="title")
    content =  models.TextField(default="article")
    date = models.DateTimeField()
    ticker = models.ForeignKey('Ticker', on_delete = models.CASCADE,)

class Tweets (models.Model):
    """Tweets table"""
    tweet = models.TextField(default='tweet')
    date = models.DateTimeField()
    ticker = models.ForeignKey('Ticker', on_delete = models.CASCADE,)

class Stocks (models.Model):
    """Stocks prices table"""
    date = models.DateTimeField()
    ticker = models.ForeignKey('Ticker', on_delete= models.CASCADE)
    stock_price = models.FloatField(default=0.0)
    class Meta:# pylint: disable=too-few-public-methods
        """Sets of field names that, taken together, must be unique"""
        unique_together = (("date", "ticker"),)

class Predictionmodel (models.Model):
    """Predictions table"""
    date = models.DateTimeField()
    ticker = models.ForeignKey('Ticker', on_delete= models.CASCADE)
    news_sentiment = models.FloatField(default=0.0)
    tweet_sentiment = models.TextField(default='tweet_sentiment')
    stock_lstm = models.FloatField(default=0.0)
    stock_price_pred = models.FloatField(default=0.0)
    class Meta:# pylint: disable=too-few-public-methods
        """Sets of field names that, taken together, must be unique"""
        unique_together = (("date", "ticker"),)
