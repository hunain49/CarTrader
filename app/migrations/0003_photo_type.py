# Generated by Django 3.1.1 on 2021-11-12 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211112_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='type',
            field=models.CharField(choices=[('Interior', 'Interior'), ('Exterior', 'Exterior')], default='Exterior', max_length=100),
        ),
    ]
