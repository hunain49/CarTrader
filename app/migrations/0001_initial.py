# Generated by Django 3.1.1 on 2021-11-12 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(choices=[('BMW', 'BMW'), ('Toyota', 'Toyota'), ('Ford', 'Ford'), ('Honda', 'Honda')], max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('vin', models.CharField(blank=True, max_length=200)),
                ('mileage', models.CharField(blank=True, max_length=200)),
                ('body_style', models.CharField(choices=[('Coupe', 'Coupe'), ('Convertible', 'Convertible'), ('Sedan', 'Sedan'), ('Hatchback', 'Hatchback'), ('SUV/CUV', 'SUV/CUV'), ('Truck', 'Truck'), ('Van/Minivan', 'Van/Minivan'), ('Wagon', 'Wagon')], max_length=100)),
                ('engine', models.CharField(max_length=100)),
                ('drivetrain', models.CharField(choices=[('Rear-wheel', 'Rear-wheel'), ('Front-wheel', 'Front-wheel'), ('All-wheel', 'All-wheel')], max_length=100)),
                ('transmission', models.CharField(choices=[('Automatic', 'Automatic'), ('Manual', 'Manual'), ('Automatic-Menual', 'Automatic with Menual')], max_length=100)),
                ('transmission_speed', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)])),
                ('exterior_color', models.CharField(max_length=100)),
                ('interior_color', models.CharField(max_length=100)),
                ('title_status', models.CharField(max_length=100)),
                ('seller_type', models.CharField(choices=[('Dealer', 'Dealer'), ('Customer', 'Customer')], max_length=100)),
                ('highlight', models.TextField()),
                ('equipment', models.TextField()),
                ('modification', models.TextField()),
                ('known_flaw', models.TextField()),
                ('recent_service_history', models.TextField()),
                ('ownership_history', models.TextField()),
                ('seller_nore', models.CharField(max_length=300)),
                ('seller', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]