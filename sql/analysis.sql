-- 统计每个用户的总操作次数
SELECT user_id, COUNT(*) AS total_actions
FROM logs
GROUP BY user_id;

-- 统计每个用户访问过的页面数量
SELECT user_id, COUNT(DISTINCT page) AS unique_pages
FROM logs
GROUP BY user_id;

-- 识别高频操作用户
SELECT user_id, COUNT(*) AS total_actions
FROM logs
GROUP BY user_id
HAVING COUNT(*) >= 8;

-- 统计每个用户的点击次数
SELECT user_id, COUNT(*) AS click_count
FROM logs
WHERE action = 'click'
GROUP BY user_id;