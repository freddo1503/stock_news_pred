# Generated by Django 4.0.1 on 2022-01-05 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postgres', '0002_tweets'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('stock_price', models.FloatField(default=0.0)),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postgres.ticker')),
            ],
            options={
                'unique_together': {('date', 'ticker')},
            },
        ),
        migrations.CreateModel(
            name='Predictionmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('news_sentiment', models.FloatField(default=0.0)),
                ('tweet_sentiment', models.TextField(default='tweet_sentiment')),
                ('stock_lstm', models.FloatField(default=0.0)),
                ('stock_price_pred', models.FloatField(default=0.0)),
                ('ticker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postgres.ticker')),
            ],
            options={
                'unique_together': {('date', 'ticker')},
            },
        ),
    ]
