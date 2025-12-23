from rest_framework import generics, filters
from .models import Event, Alert
from .permission import IsAnalystReadOnly, IsAdmin
from .serializers import EventSerializer, AlertSerializer


# Event Ingestion
class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdmin]


# Alert List & Filter
class AlertListView(generics.ListAPIView):
    queryset = Alert.objects.select_related('event')
    serializer_class = AlertSerializer
    permission_classes = [IsAnalystReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['status', 'event__severity']


# Update Alert Status
class AlertUpdateView(generics.UpdateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [IsAdmin]
