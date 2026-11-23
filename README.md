# librarycatalog

Консольная утилита на Python: пакет с реализацией алгоритмов, структур данных, генераторов тестовых наборов и бенчмарка

## Возможности

- Вычисление чисел Фибоначчи (итеративно и рекурсивно)
- Очередь FIFO с обработкой исключений на пустой структуре
- Сортировки: вставками (квадратичная) и слиянием (эффективная)
- Генерация тестовых данных (случайные, отсортированные, обратные и др.) с поддержкой seed
- Замер времени (бенчмарк) с выводом в Markdown-таблицу

## Установка

```bash
pip install -e .
```

## Использование

```bash
python -m algotool fib --n 100 --impl iterative
python -m algotool fib --n 10 --impl recursive
python -m algotool queue-demo
python -m algotool sort --input 3,1,2,-5,0 --algo merge
python -m algotool gen --type random --n 20 --seed 42
python -m algotool bench --sizes 100000,1000000 --out report.md
```

## Структура

```
lab_04/
  pyproject.toml
  README.md
  .gitignore
  src/algotool/
    __init__.py
    __main__.py
    errors.py
    fib.py
    queue_ds.py
    sort.py
    generators.py
    benchmark.py
  tests/
    test_fib.py
    test_queue.py
    test_sort.py
    test_generators.py
    test_benchmark.py
    test_cli.py
```

## Тесты и линтер

```bash
python -m pytest
ruff check .
```