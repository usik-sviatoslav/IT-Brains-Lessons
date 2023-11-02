from django.urls import path
from contacts.views import ContactList, ContactDetailView


urlpatterns = [
    path('', ContactList.as_view(), name='contact_list'),
    path('contact/<int:pk>', ContactDetailView.as_view(), name='contact_detail')
]

