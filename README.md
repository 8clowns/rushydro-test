# Решение тестового задания для Rushydro

## Структура проекта
Rushydro_test/
│
├── data/
│ ├── excel/
│ │ ├── Orders_Excel.csv
│ │ ├── Customers.csv
│ │ ├── Products.csv
│ │ └── OrderItems.csv
│ │
│ ├── python/
│ │ ├── orders_python.csv
│ │ └── product_info.csv
│ │
│ └── sql/
│ └── test.db
│
├── src/
│ ├── excel/
│ │ └── Rushydro_Analysis.xlsx
│ ├── python/
│ │ └── solution.py
│ └── sql/
│ └── queries.sql
│
├── output/
├── requirements.txt
├── .gitignore
└── README.md

text

## Запуск Python решения

### 1. Установка зависимостей

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
2. Запуск
bash
python src/python/solution.py
Содержание проекта
Excel (src/excel/Rushydro_Analysis.xlsx)
Витрина данных (Power Query)

Сводные таблицы

Круговая диаграмма (доля категорий)

Столбчатая диаграмма (топ-5 товаров)

SQL (src/sql/queries.sql)
6 запросов:

Общая выручка за 1 квартал 2024

Топ-5 стран по количеству заказов

Средний чек завершенных заказов

Новые покупатели за 2023 год

Выручка по неделям 2 квартала 2024

Процент повторных покупателей

Python (src/python/solution.py)
Загрузка и фильтрация данных

Объединение таблиц

Расчет рабочих дней

Агрегация по регионам

Визуализация (4 графика)
git add README.md
git commit -m "Обновлен README"
git push
