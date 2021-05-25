# Generated by Django 3.1.7 on 2021-05-24 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rents', '0005_auto_20210521_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentdetail',
            name='feedback',
        ),
        migrations.AddField(
            model_name='rent',
            name='feedback',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='rent', to='rents.feedback'),
        ),
    ]