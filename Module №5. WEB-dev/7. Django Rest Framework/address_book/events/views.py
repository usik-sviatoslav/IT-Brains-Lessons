from rest_framework.viewsets import ModelViewSet

from events.models import Event
from events.serializers import EventSerializer


class EventViewSet(ModelViewSet):
    queryset = Event.objects.prefetch_related('contacts').all()
    serializer_class = EventSerializer
    search_fields = ['title', 'description', 'date_time']
