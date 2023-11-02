from datetime import datetime
from django.db import models

from contacts.models import Contact


class EventManager(models.Manager):
    pass


class Event(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    date_time: datetime = models.DateTimeField()
    location = models.CharField(max_length=200, null=True, blank=True)
    contacts = models.ManyToManyField(Contact, related_name='event_contacts')

    class Meta:
        ordering = ['date_time']

    objects = EventManager()

    def __str__(self):
        date_time = self.date_time.strftime('%d.%m.%Y, %H:%M')
        return f'{date_time} {self.title}'
