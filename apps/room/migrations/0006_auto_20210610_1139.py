# Generated by Django 3.1.7 on 2021-06-10 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0005_auto_20210610_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(default='none', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
