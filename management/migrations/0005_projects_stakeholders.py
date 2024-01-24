# Generated by Django 4.2.9 on 2024-01-24 06:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0004_alter_projects_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='stakeholders',
            field=models.ManyToManyField(related_name='project', to=settings.AUTH_USER_MODEL),
        ),
    ]
