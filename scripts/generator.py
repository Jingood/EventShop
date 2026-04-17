import requests
import random
import time
import uuid
import json

API_URL = "http://localhost:8000/api/events/"

# 가상 유저 풀 생성
USER_IDS = [str(uuid.uuid4()) for _ in range(100)]

# 이벤트 타입 및 가중치 설정
EVENT_CONFIG = {
    'view': {'weight': 50, 'payload_keys': ['item_id']},
    'search': {'weight': 30, 'payload_keys': ['keyword']},
    'purchase_normal': {'weight': 15, 'payload_keys': ['item_id', 'price']},
    'purchase_limited': {'weight': 5, 'payload_keys': ['item_id', 'price', 'limited_id']}
}

# 데이터 소스
KEYWORDS = ['운동화', '반팔 티셔츠', '데님 팬츠', '바람막이', '한정판 조던', '에코백']
ITEM_IDS = list(range(1001, 1100))

def generate_payload(event_type):
    """
    이벤트 타입에 맞는 상세 데이터를 생성
    """
    if event_type == 'view':
        return {'item_id': random.choice(ITEM_IDS)}
    elif event_type == 'search':
        return {'keyword': random.choice(KEYWORDS)}
    elif event_type == 'purchase_normal':
        return {
            'item_id': random.choice(ITEM_IDS),
            'price': random.randint(10, 200) * 1000
        }
    elif event_type == 'purchase_limited':
        return {
            'item_id': random.randint(5000, 5010),
            'price': random.randint(200, 500) * 1000,
            'limited_id': f"LTD-{random.randint(1, 5)}"
        }
    return {}

def send_event():
    """
    무작위 이벤트를 생성하여 API로 전송
    """
    event_type = random.choices(
        list(EVENT_CONFIG.keys()),
        weights=[c['weight'] for c in EVENT_CONFIG.values()]
    )[0]

    data = {
        "user_id": random.choice(USER_IDS),
        "event_type": event_type,
        "payload": generate_payload(event_type)
    }

    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 201:
            print(f"[Success] {event_type} 이벤트 저장 완료 (User: {data['user_id'][:8]})")
        else:
            print(f"[Error] API 에러 {response.status_code}: {response.text}")
    except requests.exceptions.ConnectionError as e:
        print(f"[Connection Error] 서버와 연결할 수 없습니다, {e}")


if __name__ == "__main__":
    print("Event Generator Started...")
    while True:
        send_event()
        time.sleep(random.uniform(0.1, 2.0))
