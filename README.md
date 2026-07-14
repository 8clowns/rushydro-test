
# 📁 Структура проекта

```text
.
├── data/
│   ├── excel/
│   │   ├── customers.csv
│   │   ├── orderitems.csv
│   │   ├── Orders_Excel.csv
│   │   └── products.csv
│   │
│   ├── python/
│   │   ├── orders_python.csv
│   │   └── product_info.csv
│   │
│   └── sql/
│       └── test.db
│
├── output/
│   ├── category_stats.csv
│   ├── region_stats.csv
│   └── top_products.csv
│
├── src/
│   ├── excel/
│   │   └── Rushydro_Analysis.xlsx
│   │
│   ├── python/
│   │   └── solution.py
│   │
│   └── sql/
│       └── queries.sql
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📂 Описание папок

## `data/`

Исходные данные проекта.

### `data/excel/`

CSV-файлы, используемые для анализа в Microsoft Excel.

- `customers.csv` — информация о клиентах
- `orderitems.csv` — позиции заказов
- `Orders_Excel.csv` — заказы
- `products.csv` — каталог товаров

### `data/python/`

Набор данных для анализа в Python.

- `orders_python.csv`
- `product_info.csv`

### `data/sql/`

SQLite база данных.

- `test.db`

---

## `src/`

Исходный код проекта.

### `src/excel/`

Файл с выполненным анализом и визуализацией.

- `Rushydro_Analysis.xlsx`

### `src/python/`

Python-скрипт для обработки данных.

- `solution.py`

### `src/sql/`

SQL-запросы для анализа данных.

- `queries.sql`

---

## `output/`

Результаты работы Python-скриптов.

| Файл | Описание |
|-------|----------|
| `category_stats.csv` | Статистика по категориям |
| `region_stats.csv` | Статистика по регионам |
| `top_products.csv` | Наиболее продаваемые товары |

---

# 🛠 Используемые технологии

- Python 3.x
- Pandas
- SQLite
- Microsoft Excel
- CSV

---

---

# 👨‍💻 Автор

**Rushydro**

GitHub: https://github.com/your-username
