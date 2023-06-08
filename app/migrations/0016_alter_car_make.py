# Generated by Django 4.2 on 2023-06-06 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_rename_on_auctiom_car_on_auction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.CharField(blank=True, choices=[('BMW', 'BMW'), ('Toyota', 'Toyota'), ('Ford', 'Ford'), ('Honda', 'Honda'), ('Jeep', 'Jeep')], max_length=100, null=True),
        ),
    ]