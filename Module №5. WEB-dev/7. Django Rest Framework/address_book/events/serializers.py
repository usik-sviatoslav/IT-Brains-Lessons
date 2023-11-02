from rest_framework import serializers

from contacts.serializers import ContactSerializer
from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)

    class Meta:
        model = Event
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if 'contacts' in data:
            fields = ['first_name', 'last_name', 'phone']

            data['contacts'] = [
                {key: value for key, value in contact.items() if key in fields}
                for contact in data['contacts']
            ]
        return data
