# Generated by Django 3.1.7 on 2021-05-20 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='hotel',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel'),
        ),
    ]
