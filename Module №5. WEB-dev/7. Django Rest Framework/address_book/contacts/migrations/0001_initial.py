# Generated by Django 4.2.7 on 2023-11-01 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('street', models.CharField(max_length=30)),
                ('url', models.URLField(unique=True)),
                ('phone', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='contacts/')),
            ],
            options={
                'unique_together': {('first_name', 'last_name')},
            },
        ),
    ]
