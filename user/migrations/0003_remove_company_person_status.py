# Generated by Django 3.0.5 on 2021-04-16 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='person_status',
        ),
    ]