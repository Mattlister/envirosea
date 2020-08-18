# Generated by Django 3.0.8 on 2020-08-18 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_remove_booking_trips'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trips',
            options={},
        ),
        migrations.RemoveField(
            model_name='booking',
            name='bookings',
        ),
        migrations.AddField(
            model_name='booking',
            name='trips',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookings.Trips'),
        ),
        migrations.DeleteModel(
            name='Bookings',
        ),
    ]
