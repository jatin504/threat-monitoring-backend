from django.contrib import admin
from .models import UserProfile, Event, Alert


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'source_name', 'event_type', 'severity', 'created_at')
    list_filter = ('severity', 'event_type')
    search_fields = ('source_name', 'event_type')


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'status', 'created_at')
    list_filter = ('status',)