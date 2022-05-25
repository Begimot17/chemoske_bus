# Generated by Django 4.0.3 on 2022-05-22 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('popularity', models.CharField(max_length=100)),
                ('occupancy', models.CharField(max_length=100)),
                ('profitability', models.CharField(max_length=100)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routes.route')),
            ],
        ),
    ]
