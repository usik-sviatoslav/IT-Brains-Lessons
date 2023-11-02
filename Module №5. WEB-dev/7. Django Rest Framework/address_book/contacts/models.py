from django.db import models


class ContactManger(models.Manager):
    pass


class Contact(models.Model):
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    url = models.URLField(max_length=200, unique=True)
    phone = models.CharField(max_length=30)
    image = models.ImageField(upload_to='contacts/', null=True, blank=True)

    class Meta:
        unique_together = ['first_name', 'last_name']

    objects = ContactManger()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
