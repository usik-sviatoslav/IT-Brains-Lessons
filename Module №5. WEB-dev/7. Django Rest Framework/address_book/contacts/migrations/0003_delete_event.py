# Generated by Django 4.2.7 on 2023-11-02 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_event'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
    ]
