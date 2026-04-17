-- 1. 이벤트 타입별 트래픽 분포
SELECT
    event_type,
    COUNT(id) AS total_events,
    ROUND(COUNT(id) * 100.0 / (SELECT COUNT(*) FROM event_logs), 2) AS per
FROM event_logs
GROUP BY event_type
ORDER BY total_events DESC;


-- 2. 일반 구매 vs 한정판 구매 매출 비교
SELECT
    event_type,
    COUNT(id) AS purchase_count,
    SUM((payload->>'price')::numeric) AS total_revenue,
    ROUND(AVG((payload->>'price')::numeric), 0) AS avg_price
FROM event_logs
WHERE event_type IN ('purchase_normal', 'purchase_limited')
GROUP BY event_type;


-- 3. 실시간 인기 검색어 Top 5
SELECT
    payload->>'keyword' AS search_keyword,
    COUNT(id) AS search_count
FROM event_logs
WHERE event_type = 'search'
GROUP BY payload->>'keyword'
ORDER BY search_count DESC
LIMIT 5;