from django.urls import path
from .views import EventCreateView, AlertListView, AlertUpdateView


urlpatterns = [
    path('events/', EventCreateView.as_view()),
    path('alerts/', AlertListView.as_view()),
    path('alerts/<int:pk>/', AlertUpdateView.as_view()),
]
