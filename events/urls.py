from django.urls import path
from .views import EventLogCreateView

urlpatterns = [
    path('', EventLogCreateView.as_view(), name='event-create'),
]