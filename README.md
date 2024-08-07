# E-commerce Core

## Описание

Этот проект представляет собой ядро для интернет-магазина, включающее описание основных сущностей, 
таких как продукты и категории, а также функционал для инициализации объектов из JSON-файла. 
На данном этапе система платежей не реализована, однако подготавливается все для того, чтобы появилось 
ядро, готовое для дальнейшего развития и создания интерфейсов — от сайта до телеграм-бота.

## Основные возможности

- Описание и создание объектов продуктов и категорий.
- Инициализация объектов из JSON-файла.
- Подсчет количества продуктов и категорий.
- Добавление новых продуктов в категории.
- Обновление существующих продуктов по цене и количеству.

## Функциональность

E-commerce Core включает следующие модули:

- main.py
- oop.py
- utils.py

### Обзор функциональных модулей:

#### main.py

Основной модуль, обеспечивающий запуск приложения и демонстрацию работы с объектами.

#### oop.py

Модуль, содержащий классы для представления продуктов и категорий.

- Product: Класс для представления продукта.
  - Атрибуты: 
    - name: Название продукта.
    - description: Описание продукта.
    - price: Цена продукта (приватный).
    - quantity: Количество продукта.
  - Методы:
    - init: Инициализация экземпляра продукта.
    - new_product: Класс-метод для создания нового продукта или обновления существующего.
  - Свойства:
    - price: Геттер и сеттер для работы с ценой продукта.
  - Классовые переменные:
    - all_products: Список всех продуктов.

- Category: Класс для представления категории.
  - Атрибуты:
    - name: Название категории.
    - description: Описание категории.
    - products: Список продуктов в категории (приватный).
  - Методы:
    - init: Инициализация экземпляра категории.
    - add_product: Метод для добавления продукта в категорию.
  - Свойства:
    - products: Геттер для получения списка продуктов в виде строк.
  - Классовые переменные:
    - category_count: Количество категорий.
    - product_count: Количество продуктов.

#### utils.py

Модуль, содержащий утилитарную функцию для работы с JSON-файлом.

- make_the_python_objects_from_json: Функция для создания объектов из JSON-файла.
  - Параметры: file_path (путь до JSON-файла, опционально).
  - Возвращает: картеж списков объектов категорий и продуктов.

## Зависимости

- Python 3.12
- flake8 7.1.0
- isort 5.13.2
- black 24.8.0
- mypy 1.11.1
- pytest 8.3.2
- pytest-cov 5.0.0

## Установка

1. Клонируйте репозиторий:
```bash
git clone git@github.com:ZorinVS/E-commerce_Core.git
```
2. Установите зависимости:
```bash
poetry install
```

## Тестирование проекта

Тестирование проекта проводится с использованием пакета tests, который включает следующие файлы:

- init.py
- conftest.py
- test_oop.py
- test_utils.py

### Есть два способа выполнить тестирование проекта:
1. Используя терминал PyCharm:
```bash
pytest tests
```
2. Используя функциональность PyCharm:
- Откройте окно **Edit Configurations**.
- Выберите **pytest**.
- Укажите директорию, содержащую тесты, и директорию проекта.
- Подтвердите изменения, нажав **Apply** и **OK**.
- Запустите **pytest in tests**

## Документация

Для получения дополнительной информации, пожалуйста, свяжитесь с...

## Лицензия

Этот проект лицензирован в соответствии с условиями [MIT License](LICENSE).
