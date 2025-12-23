from django.urls import path
from .views import EventCreateView, AlertListView, AlertUpdateView, SignupView

urlpatterns = [
    path("auth/signup/", SignupView.as_view()),
    path('events/', EventCreateView.as_view()),
    path('alerts/', AlertListView.as_view()),
    path('alerts/<int:pk>/', AlertUpdateView.as_view()),
]
