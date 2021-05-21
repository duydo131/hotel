# Generated by Django 3.1.7 on 2021-05-21 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_rating_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='address',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='clean',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='comfortable',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='convenirent',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='staff',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='wifi_free',
            field=models.FloatField(default=0),
        ),
    ]
