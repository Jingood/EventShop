from rest_framework import generics
from .models import EventLog
from .serializers import EventLogSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Events'], summary="이벤트 로그 수집 API")
class EventLogCreateView(generics.CreateAPIView):
    """
    웹 서비스에서 발생하는 이벤트를 수집하여 저장합니다.
    """
    queryset = EventLog.objects.all()
    serializer_class = EventLogSerializer
