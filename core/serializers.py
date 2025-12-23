from rest_framework import serializers
from .models import Event, Alert


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['created_at']

    def create(self, validated_data):
        event = Event.objects.create(**validated_data)

        if event.severity in ['HIGH', 'CRITICAL']:
            Alert.objects.create(event=event)

        return event


class AlertSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = Alert
        fields = '__all__'
        read_only_fields = ['created_at']
