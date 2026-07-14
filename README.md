# Решение тестового задания для Rushydro

## 📁 Структура проекта
Rushydro_test/
│
├── 📁 data/
│ ├── 📁 excel/ # Данные для Excel части
│ │ ├── Orders_Excel.csv
│ │ ├── Customers.csv
│ │ ├── Products.csv
│ │ └── OrderItems.csv
│ │
│ ├── 📁 python/ # Данные для Python части
│ │ ├── orders_python.csv
│ │ └── product_info.csv
│ │
│ └── 📁 sql/ # SQLite база данных
│ └── test.db
│
├── 📁 src/ # Исходный код
│ ├── 📁 excel/
│ │ └── Rushydro_Analysis.xlsx # Готовый Excel отчет
│ ├── 📁 python/
│ │ └── solution.py # Полное Python решение
│ └── 📁 sql/
│ └── queries.sql # SQL запросы (6 заданий)
│
├── 📁 output/ # Результаты (создается автоматически)
├── requirements.txt # Зависимости Python
├── .gitignore
└── README.md

text

---

## 🚀 Запуск Python решения

### 1. Установка зависимостей

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# или
source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt
2. Запуск
bash
python src/python/solution.py
Результаты появятся в папке output/.

📊 Содержание проекта
Excel (src/excel/Rushydro_Analysis.xlsx)
Готовый Excel файл с выполненным заданием:

Витрина данных (Power Query)

Сводные таблицы (динамика по месяцам, выручка по регионам)

Круговая диаграмма (доля категорий)

Столбчатая диаграмма (топ-5 товаров)

SQL (src/sql/queries.sql)
6 запросов к SQLite базе данных:

Общая выручка за 1 квартал 2024

Топ-5 стран по количеству заказов

Средний чек завершенных заказов

Новые покупатели за 2023 год

Выручка по неделям 2 квартала 2024

Процент повторных покупателей

Python (src/python/solution.py)
Анализ данных с использованием Polars:

Загрузка и фильтрация данных

Объединение таблиц

Расчет рабочих дней

Агрегация по регионам

Визуализация (4 графика)