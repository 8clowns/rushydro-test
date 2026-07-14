"""
Решение тестового задания для Rushydro
Python часть с использованием Polars

Задания:
1. Загрузка и первичный просмотр
2. Фильтрация (region = "Восточный" AND quantity > 10)
3. Объединение таблиц и добавление total_cost
4. Расчёт рабочих дней между датами
5. Агрегация по регионам
6. Вывод результатов
"""

import polars as pl
from datetime import datetime, timedelta
from pathlib import Path

# Создаем папку для результатов
output_dir = Path('output')
output_dir.mkdir(exist_ok=True)

print("="*70)
print("🐍 PYTHON РЕШЕНИЕ ТЕСТОВОГО ЗАДАНИЯ RUSHYDRO")
print("="*70)

# ============================================================
# ФУНКЦИЯ ДЛЯ РАСЧЕТА РАБОЧИХ ДНЕЙ (без выходных)
# ============================================================

def count_business_days(start_date, end_date):
    """
    Подсчет рабочих дней между датами (без учета выходных)
    Рабочие дни: понедельник-пятница (weekday 0-4)
    Праздничные дни НЕ учитываются (упрощенная версия)
    """
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    
    # Если даты одинаковые или start > end
    if start_date >= end_date:
        return 0
    
    # Считаем рабочие дни (пн-пт)
    business_days = 0
    current_date = start_date
    
    while current_date < end_date:
        # weekday(): 0=пн, 1=вт, 2=ср, 3=чт, 4=пт, 5=сб, 6=вс
        if current_date.weekday() < 5:
            business_days += 1
        current_date += timedelta(days=1)
    
    return business_days


# ============================================================
# ЗАДАНИЕ 1: ЗАГРУЗКА И ПЕРВИЧНЫЙ ПРОСМОТР
# ============================================================

print("\n" + "="*70)
print("ЗАДАНИЕ 1: ЗАГРУЗКА И ПЕРВИЧНЫЙ ПРОСМОТР ДАННЫХ")
print("="*70)

# Пути к файлам
orders_path = Path('data/python/orders_python.csv')
products_path = Path('data/python/product_info.csv')

# Проверка существования файлов
if not orders_path.exists():
    print(f"❌ Ошибка: Файл не найден - {orders_path}")
    print(f"   Текущая директория: {Path.cwd()}")
    print("   Убедитесь, что файлы лежат в: data/python/")
    exit(1)

if not products_path.exists():
    print(f"❌ Ошибка: Файл не найден - {products_path}")
    exit(1)

print(f"✅ Файлы найдены:")
print(f"   - {orders_path}")
print(f"   - {products_path}")

# Загружаем данные
orders_df = pl.read_csv(orders_path)
product_info_df = pl.read_csv(products_path)

print("\n📊 Таблица 'orders' (первые 5 строк):")
print(orders_df.head())

print("\n📊 Таблица 'product_info' (первые 5 строк):")
print(product_info_df.head())

print(f"\n📈 Информация о данных:")
print(f"  - Заказов: {orders_df.height}")
print(f"  - Товаров: {product_info_df.height}")
print(f"  - Уникальных регионов: {orders_df['region'].n_unique()}")
print(f"  - Уникальных категорий: {product_info_df['category'].n_unique()}")


# ============================================================
# ЗАДАНИЕ 2: ФИЛЬТРАЦИЯ
# ============================================================

print("\n" + "="*70)
print("ЗАДАНИЕ 2: ФИЛЬТРАЦИЯ (region = 'Восточный' AND quantity > 10)")
print("="*70)

filtered_orders = orders_df.filter(
    (pl.col('region') == 'Восточный') & 
    (pl.col('quantity') > 10)
)

print(f"\n✅ Количество отфильтрованных заказов: {filtered_orders.height}")
print("\n📋 Первые 5 отфильтрованных заказов:")
print(filtered_orders.head())


# ============================================================
# ЗАДАНИЕ 3: ОБЪЕДИНЕНИЕ ТАБЛИЦ
# ============================================================

print("\n" + "="*70)
print("ЗАДАНИЕ 3: ОБЪЕДИНЕНИЕ ТАБЛИЦ И ДОБАВЛЕНИЕ total_cost")
print("="*70)

# Соединяем таблицы по product_id (INNER JOIN)
joined_df = orders_df.join(
    product_info_df,
    on='product_id',
    how='inner'
)

# Добавляем столбец total_cost
joined_df = joined_df.with_columns(
    (pl.col('quantity') * pl.col('price')).alias('total_cost')
)

print("\n✅ Объединенная таблица (первые 5 строк):")
print(joined_df.select([
    'order_id', 'product_id', 'product_name', 
    'category', 'quantity', 'price', 'total_cost', 'region'
]).head())

print(f"\n📊 Размер объединенной таблицы: {joined_df.height} строк")
print(f"📊 Всего полей: {len(joined_df.columns)}")


# ============================================================
# ЗАДАНИЕ 4: РАСЧЁТ РАБОЧИХ ДНЕЙ
# ============================================================

print("\n" + "="*70)
print("ЗАДАНИЕ 4: РАСЧЁТ РАБОЧИХ ДНЕЙ МЕЖДУ ДАТАМИ")
print("="*70)

# Применяем функцию для расчета рабочих дней
joined_df = joined_df.with_columns(
    pl.struct(['order_date', 'delivery_date'])
    .map_elements(
        lambda row: count_business_days(row['order_date'], row['delivery_date']),
        return_dtype=pl.Int64
    )
    .alias('business_days')
)

print("\n📋 Данные с рабочими днями (первые 5 строк):")
print(joined_df.select([
    'order_id', 'order_date', 'delivery_date', 
    'business_days', 'region'
]).head())

print(f"\n📊 Статистика рабочих дней доставки:")
print(f"  - Минимум: {joined_df['business_days'].min()}")
print(f"  - Максимум: {joined_df['business_days'].max()}")
print(f"  - Среднее: {joined_df['business_days'].mean():.2f}")


# ============================================================
# ЗАДАНИЕ 5: АГРЕГАЦИЯ ПО РЕГИОНАМ
# ============================================================

print("\n" + "="*70)
print("ЗАДАНИЕ 5: АГРЕГАЦИЯ ПО РЕГИОНАМ")
print("="*70)

region_stats = joined_df.group_by('region').agg([
    pl.col('business_days').mean().alias('avg_business_days_by_region'),
    pl.col('total_cost').sum().alias('total_sales_by_region'),
    pl.col('order_id').count().alias('order_count_by_region')
]).sort('avg_business_days_by_region', descending=True)

print("\n📊 Статистика по регионам (сортировка по убыванию рабочих дней):")
print(region_stats)


# ============================================================
# ЗАДАНИЕ 6: ВЫВОД РЕЗУЛЬТАТОВ
# ============================================================

print("\n" + "="*70)
print("ЗАДАНИЕ 6: ВЫВОД РЕЗУЛЬТАТОВ")
print("="*70)

# 6.1 Топ-5 товаров по выручке (дополнительный анализ)
print("\n🏆 ТОП-5 ТОВАРОВ ПО ВЫРУЧКЕ:")
top_products = joined_df.group_by(['product_id', 'product_name']).agg([
    pl.col('total_cost').sum().alias('total_sales'),
    pl.col('quantity').sum().alias('total_quantity')
]).sort('total_sales', descending=True).head(5)
print(top_products)

# 6.2 Статистика по категориям
print("\n📈 СТАТИСТИКА ПО КАТЕГОРИЯМ:")
category_stats = joined_df.group_by('category').agg([
    pl.col('total_cost').sum().alias('total_sales'),
    pl.col('quantity').sum().alias('total_quantity'),
    pl.col('order_id').count().alias('order_count')
]).sort('total_sales', descending=True)
print(category_stats)

# 6.3 ИТОГОВАЯ СТАТИСТИКА
print("\n📊 ИТОГОВАЯ СТАТИСТИКА:")
print(f"  - Всего обработано заказов: {joined_df.height}")
print(f"  - Общая выручка: {joined_df['total_cost'].sum():,.2f} руб.")
print(f"  - Средний чек: {joined_df['total_cost'].mean():,.2f} руб.")
print(f"  - Среднее время доставки (рабочие дни): {joined_df['business_days'].mean():.2f}")

print("\n🏆 ТОП-5 РЕГИОНОВ ПО ВЫРУЧКЕ:")
top_regions = region_stats.sort('total_sales_by_region', descending=True).head(5)
print(top_regions.select(['region', 'total_sales_by_region', 'order_count_by_region']))


# ============================================================
# СОХРАНЕНИЕ РЕЗУЛЬТАТОВ
# ============================================================

print("\n" + "="*70)
print("СОХРАНЕНИЕ РЕЗУЛЬТАТОВ")
print("="*70)

# Сохраняем все результаты в CSV
region_stats.write_csv('output/region_stats.csv')
top_products.write_csv('output/top_products.csv')
category_stats.write_csv('output/category_stats.csv')

print("\n✅ Все результаты сохранены в папку 'output/':")
print("   - region_stats.csv     - статистика по регионам (задание 5)")
print("   - top_products.csv     - топ-5 товаров по выручке")
print("   - category_stats.csv   - статистика по категориям")


# ============================================================
# ВЫВОД В УДОБНОМ ДЛЯ ЧТЕНИЯ ВИДЕ
# ============================================================

print("\n" + "="*70)
print("📊 ИТОГОВЫЕ ТАБЛИЦЫ В УДОБНОМ ВИДЕ")
print("="*70)

# Таблица 1: Агрегация по регионам (задание 5)
print("\n📋 ТАБЛИЦА 1: АГРЕГАЦИЯ ПО РЕГИОНАМ")
print("-" * 70)
print(f"{'Регион':<15} {'Ср. рабочие дни':>18} {'Выручка (руб.)':>20} {'Кол-во заказов':>15}")
print("-" * 70)
for row in region_stats.iter_rows():
    print(f"{row[0]:<15} {row[1]:>18.2f} {row[2]:>20,.2f} {row[3]:>15}")
print("-" * 70)

# Таблица 2: Топ-5 товаров
print("\n📋 ТАБЛИЦА 2: ТОП-5 ТОВАРОВ ПО ВЫРУЧКЕ")
print("-" * 70)
print(f"{'Товар':<25} {'Выручка (руб.)':>25} {'Кол-во':>10}")
print("-" * 70)
for row in top_products.iter_rows():
    print(f"{row[1][:24]:<25} {row[2]:>25,.2f} {row[3]:>10}")
print("-" * 70)

# Таблица 3: Статистика по категориям
print("\n📋 ТАБЛИЦА 3: СТАТИСТИКА ПО КАТЕГОРИЯМ")
print("-" * 70)
print(f"{'Категория':<15} {'Выручка (руб.)':>20} {'Кол-во товаров':>15} {'Заказов':>10}")
print("-" * 70)
for row in category_stats.iter_rows():
    print(f"{row[0][:14]:<15} {row[1]:>20,.2f} {row[2]:>15} {row[3]:>10}")
print("-" * 70)


# ============================================================
# ЗАВЕРШЕНИЕ
# ============================================================

print("\n" + "="*70)
print("✅ СКРИПТ УСПЕШНО ВЫПОЛНЕН!")
print("="*70)
print("\n📁 Результаты сохранены в папке 'output/'")
print("📊 Графики можно создать отдельно при необходимости")