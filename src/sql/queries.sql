-- ============================================
-- SQL РЕШЕНИЕ ТЕСТОВОГО ЗАДАНИЯ RUSHYDRO
-- База данных: data_sql/test.db
-- Таблицы: orders, customers
-- ============================================

-- Проверка структуры таблиц
-- SELECT sql FROM sqlite_master WHERE type='table';

-- ============================================
-- ЗАДАНИЕ 1: Общая выручка за 1 квартал 2024 года
-- ============================================
SELECT 
    '1. Общая выручка за 1 квартал 2024' AS Задание,
    ROUND(SUM(DeliveryCost), 2) AS total_revenue
FROM orders
WHERE strftime('%Y', OrderDate) = '2024' 
  AND CAST(strftime('%m', OrderDate) AS INTEGER) BETWEEN 1 AND 3
  AND Returned = 'completed';

-- ============================================
-- ЗАДАНИЕ 2: Топ-5 стран по количеству заказов
-- ============================================
SELECT 
    '2. Топ-5 стран по количеству заказов' AS Задание,
    Region AS Страна,
    COUNT(OrderID) AS Количество_заказов
FROM orders
GROUP BY Region
ORDER BY Количество_заказов DESC
LIMIT 5;

-- ============================================
-- ЗАДАНИЕ 3: Средний чек для завершенных заказов
-- ============================================
SELECT 
    '3. Средний чек для завершенных заказов' AS Задание,
    ROUND(AVG(DeliveryCost), 2) AS avg_check
FROM orders
WHERE Returned = 'completed';

-- ============================================
-- ЗАДАНИЕ 4: Новые покупатели за позапрошлый год (2023)
-- ============================================
SELECT 
    '4. Новые покупатели за 2023 год' AS Задание,
    COUNT(DISTINCT CustomerID) AS new_customers_count
FROM customers
WHERE strftime('%Y', JoinDate) = '2023';

-- ============================================
-- ЗАДАНИЕ 5: Выручка по неделям 2 квартала 2024
-- ============================================
SELECT 
    '5. Выручка по неделям 2 квартала 2024' AS Задание,
    strftime('%W', OrderDate) AS Номер_недели,
    ROUND(SUM(DeliveryCost), 2) AS weekly_revenue
FROM orders
WHERE strftime('%Y', OrderDate) = '2024' 
  AND CAST(strftime('%m', OrderDate) AS INTEGER) BETWEEN 4 AND 6
  AND Returned = 'completed'
GROUP BY Номер_недели
ORDER BY Номер_недели;

-- ============================================
-- ЗАДАНИЕ 6: Процент повторных покупателей
-- ============================================
WITH customer_orders AS (
    SELECT 
        CustomerID,
        COUNT(OrderID) AS order_count
    FROM orders
    GROUP BY CustomerID
)
SELECT 
    '6. Процент повторных покупателей' AS Задание,
    ROUND(
        100.0 * COUNT(CASE WHEN order_count >= 2 THEN 1 END) / COUNT(*), 
        2
    ) AS repeat_customer_percent
FROM customer_orders;

-- ============================================
-- ДОПОЛНИТЕЛЬНАЯ АНАЛИТИКА
-- ============================================

-- Выручка по месяцам
SELECT 
    strftime('%Y-%m', OrderDate) AS Месяц,
    COUNT(*) AS Заказов,
    ROUND(AVG(DeliveryCost), 2) AS Средний_чек,
    ROUND(SUM(DeliveryCost), 2) AS Выручка
FROM orders
WHERE Returned = 'completed'
GROUP BY Месяц
ORDER BY Месяц;

-- Статистика по регионам
SELECT 
    Region,
    COUNT(*) AS Заказов,
    ROUND(AVG(DeliveryCost), 2) AS Средний_чек,
    ROUND(SUM(DeliveryCost), 2) AS Выручка,
    ROUND(100.0 * SUM(CASE WHEN Returned = 'completed' THEN 1 ELSE 0 END) / COUNT(*), 2) AS Процент_завершенных
FROM orders
GROUP BY Region
ORDER BY Выручка DESC;