# Generated by Django 4.2.9 on 2024-01-24 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_techstack'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='techstack',
            field=models.ManyToManyField(to='management.techstack'),
        ),
    ]