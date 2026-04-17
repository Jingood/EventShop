import uuid
from django.db import models

class EventLog(models.Model):
    # 이벤트 타입
    EVENT_TYPES = [
        ('view', 'Item View'),
        ('search', 'Item Search'),
        ('purchase_normal', 'Normal Item Purchase'),
        ('purchase_limited', 'Limited Item Purchase')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # 공통 정형 필드
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    user_id = models.CharField(max_length=100, db_index=True)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES, db_index=True)

    # 가변 비정형 필드
    payload = models.JSONField(default=dict, blank=True)

    class Meta:
        db_table = 'event_logs'
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {self.event_type} by user:{self.user_id}"

