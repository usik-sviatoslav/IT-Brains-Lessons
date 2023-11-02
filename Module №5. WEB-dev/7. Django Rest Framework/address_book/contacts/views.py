from rest_framework.viewsets import ModelViewSet

from contacts.models import Contact
from contacts.serializers import ContactSerializer


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    search_fields = ['first_name', 'last_name', 'country', 'city', 'street', 'phone']
