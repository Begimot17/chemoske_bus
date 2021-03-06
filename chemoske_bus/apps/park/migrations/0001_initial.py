# Generated by Django 4.0.3 on 2022-06-07 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('routes', '__first__'),
        ('flights', '__first__'),
        ('drivers', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=100)),
                ('mileage', models.IntegerField()),
                ('num_of_flights_perform', models.IntegerField()),
                ('date_of_next', models.DateField()),
                ('date_of_last', models.DateField()),
                ('current_flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_flight', to='flights.trip')),
                ('driver_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_1', to='drivers.driver')),
                ('driver_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_2', to='drivers.driver')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_1', to='routes.route')),
            ],
        ),
    ]
