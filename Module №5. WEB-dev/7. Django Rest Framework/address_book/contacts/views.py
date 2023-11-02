from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from contacts.models import Contact
from contacts.serializers import ContactSerializer


class ContactList(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
