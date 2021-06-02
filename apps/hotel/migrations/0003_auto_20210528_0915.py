# Generated by Django 3.1.7 on 2021-05-28 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20210527_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='fax',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, unique=True),
        ),
    ]