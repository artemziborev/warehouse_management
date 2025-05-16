
# Warehouse Management System (WMS)

## 📋 Описание
Система управления складом (WMS) на основе **Clean Architecture** с использованием **SQLAlchemy**. Проект включает:
- Модели данных (продукты, заказы, ячейки склада)
- Use Cases для обработки основных бизнес-процессов
- Полноценные репозитории и Unit of Work
- Автоматические тесты и линтинг

---

## 📂 Структура проекта

```
project/
├── app/
│   ├── main.py
│   └── adapters/
│       ├── unit_of_work.py
│       └── repositories/
│           ├── product_repository.py
│           ├── order_repository.py
│           └── warehouse_cell_repository.py
├── domain/
│   ├── entities/
│   │   ├── product.py
│   │   ├── order.py
│   │   ├── warehouse_cell.py
│   │   └── value_objects.py
│   ├── repositories/
│   │   └── interfaces/
│   │       ├── base_repository.py
│   │       ├── product_repository.py
│   │       ├── order_repository.py
│   │       └── warehouse_cell_repository.py
│   ├── exceptions.py
│   └── unit_of_work.py
├── framework_drivers/
│   └── orm/
│       ├── base.py
│       ├── product_orm.py
│       ├── order_orm.py
│       └── warehouse_cell_orm.py
├── use_cases/
│   ├── create_product.py
│   ├── create_order.py
│   ├── receive_goods.py
│   ├── ship_order.py
│   └── inventory_management.py
├── tests/
│   ├── conftest.py
│   ├── test_entities/
│   ├── test_repositories/
│   └── test_use_cases/
├── .github/
│   └── workflows/
│       ├── tests.yml
│       └── lint.yml
├── requirements.txt
├── dev-requirements.txt
├── .pylintrc
└── README.md
```

---

## 🚀 Установка

### Клонирование репозитория
```bash
git clone
cd project
```

### Установка зависимостей
**Production:**
```bash
pip install -r requirements.txt
```

**Development:**
```bash
pip install -r dev-requirements.txt
```

---

## 🧪 Запуск тестов

```bash
pytest --disable-warnings --cov=use_cases --cov=app --cov=domain --cov=framework_drivers
```

---

## 📝 Линтинг

```bash
pylint app/ domain/ framework_drivers/ use_cases/
```

---

## 📦 Основные компоненты

- **Product** — товары, включая название, описание, цену и количество
- **Order** — заказы, содержащие продукты
- **WarehouseCell** — ячейки для хранения товаров

---

## 💡 Используемые технологии

- **SQLAlchemy** для работы с базой данных
- **Pytest** для тестирования
- **Pylint** для статического анализа кода

---

## 🌱 Планы развития

- Поддержка распределенных складов
- Интеграция с внешними системами управления заказами (OMS)
- Расширенные сценарии обработки заказов
- Поддержка различных типов ячеек хранения

---

## 📄 Лицензия

Проект распространяется под лицензией MIT. Подробности см. в файле **LICENSE**.
