# Инструкция по созданию Excel отчета (Power Query)

## Шаг 1: Загрузка данных
1. Откройте Excel
2. Перейдите: Данные → Получить данные → Из текстового/CSV
3. Загрузите файлы:
   - Orders_Excel.csv
   - Customers.csv
   - Products.csv
   - OrderItems.csv
4. Для каждого файла выберите "Загрузить в..." → "Только создать подключение"

## Шаг 2: Объединение таблиц в Power Query
1. Данные → Объединить запросы
2. Свяжите таблицы:
   - Orders ↔ Customers по CustomerID
   - Orders ↔ OrderItems по OrderID
   - OrderItems ↔ Products по ProductID

## Шаг 3: Добавление вычисляемых столбцов
1. В Power Query Editor:
   - Добавить столбец → Пользовательский столбец
   - Revenue = [Price] * [Quantity] * (1 - [Discount]) - [DeliveryCost]
   - Month = Date.Month([OrderDate])

## Шаг 4: Создание таблиц
1. "Продажи по категориям":
   - Группировка по Category
   - Сумма Revenue, средний чек, количество клиентов

2. "Топ-5 товаров":
   - Сортировка по Revenue DESC
   - Взять первые 5 строк

3. "VIP-клиенты":
   - Фильтр CustomerSegment = "VIP"

4. "Новые клиенты":
   - Фильтр CustomerSegment = "Новый"

## Шаг 5: Визуализация
1. Сводные таблицы:
   - Динамика по месяцам: Month в строки, Revenue в значения
   - Выручка по регионам: Region в строки, Revenue в значения

2. Графики:
   - Круговая диаграмма: категории по Revenue
   - Столбчатая диаграмма: топ-5 товаров