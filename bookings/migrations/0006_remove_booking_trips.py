# Generated by Django 3.0.8 on 2020-08-18 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_booking_bookings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='trips',
        ),
    ]
