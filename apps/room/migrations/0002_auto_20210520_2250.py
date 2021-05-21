# Generated by Django 3.1.7 on 2021-05-20 15:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='price_now',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='RoomService',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('room', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='service', to='room.room')),
                ('services', models.ManyToManyField(blank=True, null=True, related_name='services', to='room.Service')),
            ],
            options={
                'db_table': 'room_service',
            },
        ),
    ]
