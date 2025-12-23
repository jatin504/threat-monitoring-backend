from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Event, Alert, UserProfile


class SignupSerializer(serializers.ModelSerializer):
    """
    Public signup API
    - Creates only ANALYST users
    - Admin is created via ENV bootstrap (safe)
    """

    class Meta:
        model = User
        fields = ("username", "password", "email")
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data.get("email", "")
        )

        # IMPORTANT: public signup → analyst only
        UserProfile.objects.create(user=user, role="ANALYST")
        return user



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
