# Generated by Django 3.1.7 on 2021-05-25 09:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comfortable', models.IntegerField()),
                ('address', models.IntegerField()),
                ('wifi_free', models.IntegerField()),
                ('staff', models.IntegerField()),
                ('convenirent', models.IntegerField()),
                ('clean', models.IntegerField()),
                ('content', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'feedback',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('discount', models.BigIntegerField(blank=True, null=True)),
                ('totalAmount', models.BigIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'rent',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='RentDetail',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('price', models.BigIntegerField(blank=True, null=True)),
                ('voucher', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='rents.rent')),
            ],
            options={
                'db_table': 'rent_detail',
                'ordering': ['created_at'],
            },
        ),
    ]
