# E-commerce Core

## Описание

Этот проект представляет собой ядро для интернет-магазина, включающее описание основных сущностей, 
таких как продукты и категории, а также функционал для инициализации объектов из JSON-файла. 
На данном этапе система платежей не реализована, однако подготавливается все для того, чтобы появилось 
ядро, готовое для дальнейшего развития и создания интерфейсов — от сайта до телеграм-бота.

## Основные возможности

- Описание и создание объектов различных типов продуктов (например, смартфоны, трава газонная).
- Поддержка механизма наследования атрибутов и методов от абстрактного класса BaseProduct и класса-миксина PrintMixin при создании различных типов продуктов.
- Создание и управление категориями продуктов с наследованием от абстрактного класса BaseOrderCategoryProperties.
- Инициализация объектов из JSON-файла.
- Подсчет количества продуктов и категорий.
- Добавление новых продуктов в категории.
- Обновление существующих продуктов по цене и количеству.
- Итерация по товарам в категориях с использованием вспомогательного класса.
- Создание и управление заказами с проверкой наличия достаточного количества товара на складе.

## Функциональность

E-commerce Core включает следующие модули:

- main.py
- base_order_category_properties.py
- base_product.py
- category.py
- incorrect_product_quantity_error.py
- lawn_grass_product.py
- order.py
- print_mixin.py
- product.py
- smartphone_product.py
- utils.py

### Обзор функциональных модулей:

#### main.py

Основной модуль, обеспечивающий запуск приложения и демонстрацию работы с объектами.

#### base_order_category_properties.py

Модуль, содержащий абстрактный базовый класс для общих свойств классов Заказ и Категория.

- BaseOrderCategoryProperties: Абстрактный базовый класс, объединяющий общие свойства классов Заказ и Категория.
  - Атрибуты экземпляра:
    - `name`: Название категории или товара в заказе.
    - `description`: Описание категории или товара в заказе.
  - Методы:
    - `__init__`: Конструктор для инициализации экземпляра с общими свойствами.
    - `__str__`: Абстрактный метод для строкового отображения информации об объекте.

#### base_product.py

Модуль, содержащий абстрактный базовый класс для представления продукта.

- BaseProduct: Абстрактный базовый класс, предназначенный для создания и обновления продуктов.
  - Методы:
    - `new_product`: Абстрактный класс-метод, который используется для создания нового продукта или обновления существующего.

#### category.py

Модуль, содержащий класс для представления категорий.

- Category: Класс для представления категории.
  - Наследует: Атрибуты и методы от класса BaseOrderCategoryProperties.
  - Атрибуты на уровне класса:
    - `category_count`: Количество категорий.
    - `product_count`: Количество продуктов.
  - Атрибуты экземпляра:
    - `name`: Название категории.
    - `description`: Описание категории.
    - `products`: Список продуктов в категории (приватный).
  - Методы:
    - `__init__`: Конструктор для инициализации экземпляра категории.
    - `__str__`: Dunder-метод для строкового отображения информации об объекте.
    - `add_product`: Метод для добавления продукта в категорию. Если количество товара равно нулю, выбрасывается исключение IncorrectProductQuantityError. В случае успешного добавления выводится сообщение об успешном добавлении товара. В конце всегда выводится финальное сообщение о завершении обработки добавления.
    - `middle_price`: Метод для подсчета среднего ценника всех товаров в категории. Возвращает округленное среднее значение. Если в категории нет продуктов, возвращает 0.
  - Свойства:
    - `products`: Геттер для получения списка продуктов в виде строк.
    - `products_list`: Геттер для получения списка продуктов.

- CategoryProductsIterator: Вспомогательный класс для итерации по товарам в категории.
  - Атрибуты экземпляра:
    - `category`: Ссылка на объект категории, по товарам которой будет происходить итерация (приватный).
    - `index`: Текущий индекс итерации (приватный).
  - Методы:
    - `__init__`: Конструктор для инициализации итератора с объектом категории.
    - `__iter__`: Dunder-метод для возврата итератора.
    - `__next__`: Dunder-метод для перехода к следующему значению и его считывания.

#### incorrect_product_quantity_error.py

Модуль, содержащий класс для обработки исключений, связанных с некорректным количеством товара.

- IncorrectProductQuantityError: Класс исключения, который используется при попытке добавить товар с некорректным количеством.
  - Атрибуты экземпляра:
    - `message`: Сообщение об ошибке, переданное при вызове исключения. Если сообщение не передано, по умолчанию используется "Невозможно добавить товар с нулевым количеством".
  - Методы:
    - `__init__`: Инициализирует исключение с пользовательским сообщением или со значением по умолчанию.
    - `__str__`: Dunder-метод для строкового представления сообщения об ошибке.

#### lawn_grass_product.py

Модуль, содержащий класс для представления травы газонной.

- LawnGrass: Класс для представления травы газонной.
  - Наследует: Все атрибуты и методы от класса Product.
  - Дополнительные атрибуты экземпляра:
    - `country`: Страна-производитель.
    - `germination_period`: Срок прорастания.
    - `color`: Цвет.
  - Методы:
    - `__init__`: Конструктор для инициализации экземпляра класса LawnGrass, расширяет базовый конструктор класса Product, добавляя специфические для газонной травы атрибуты (country, germination_period, color).
    - `__add__`: Dunder-метод для сложения двух объектов класса LawnGrass, возвращает полную стоимость всех товаров газонной травы на складе. Если другой объект не является экземпляром класса LawnGrass, выбрасывается ошибка типа (TypeError).

#### order.py

Модуль, содержащий класс для представления заказа на покупку товара.

- Order: Класс для представления заказа.
  - Наследует: Атрибуты и методы от класса BaseOrderCategoryProperties.
  - Атрибуты экземпляра:
    - `product`: Продукт, на который оформлен заказ.
    - `name`: Название продукта.
    - `description`: Описание продукта.
    - `quantity`: Количество купленного товара.
    - `total_price`: Итоговая стоимость заказа.
  - Методы:
    - `__init__`: Конструктор для создания экземпляра заказа. Проверяет, чтобы количество товара в заказе не было равно нулю и чтобы заказанное количество не превышало доступное на складе. Если количество товара равно нулю или превышает доступное, выбрасывается исключение IncorrectProductQuantityError. В случае успешного оформления заказа, количество товара на складе уменьшается, и выводится сообщение об успешном добавлении товара в заказ. В конце всегда выводится финальное сообщение о завершении обработки заказа.
    - `__str__`: Dunder-метод для строкового отображения информации о заказе, включая количество, описание товара и итоговую стоимость.

#### print_mixin.py

Модуль, содержащий класс-миксин для печати информации об объекте при его создании.

- PrintMixin: Класс-миксин, добавляющий функциональность автоматической печати информации об объекте при его инициализации.
  - Методы:
    - `__init__`: Выводит в консоль информацию о создании объекта, вызывая метод repr.
    - `__repr__`: Возвращает строковое представление объекта, включающее имя класса и значения атрибутов name, description, price, quantity.

#### product.py

Модуль, содержащий класс для представления продуктов.

- Product: Класс для представления продукта.
  - Наследует: Атрибуты и методы от классов BaseProduct и PrintMixin.
  - Атрибуты на уровне класса:
    - `all_products`: Список всех продуктов.
  - Атрибуты экземпляра: 
    - `name`: Название продукта.
    - `description`: Описание продукта.
    - `price`: Цена продукта (приватный).
    - `quantity`: Количество продукта.
  - Методы:
    - `__init__`: Конструктор для инициализации экземпляра продукта. Если количество продукта равно нулю, выбрасывается исключение ValueError с сообщением "Товар с нулевым количеством не может быть добавлен". После инициализации экземпляр добавляется в список all_products.
    - `__str__`: Dunder-метод для строкового представления объекта продукта, возвращает строку с названием, ценой и количеством продукта.
    - `__add__`: Dunder-метод для сложения товаров и получения полной стоимости всех товаров на складе.
    - `new_product`: Класс-метод для создания нового продукта или обновления существующего. Если продукт с таким же названием уже существует, обновляет его количество и цену (если новая цена выше).
  - Свойства:
    - `price`: Геттер и сеттер для работы с ценой продукта.

#### smartphone_product.py

Модуль, содержащий класс для представления смартфона.

- Smartphone: Класс для представления смартфона.
  - Наследует: Все атрибуты и методы от класса Product.
  - Дополнительные атрибуты экземпляра:
    - `efficiency`: Производительность смартфона.
    - `model`: Модель смартфона.
    - `memory`: Объем встроенной памяти смартфона.
    - `color`: Цвет смартфона.
  - Методы:
    - `__init__`: Конструктор для инициализации экземпляра класса Smartphone, расширяет базовый конструктор класса Product, добавляя специфические для смартфона атрибуты (efficiency, model, memory, color).
    - `__add__`: Dunder-метод для сложения двух объектов класса Smartphone, возвращает полную стоимость всех смартфонов на складе. Если другой объект не является экземпляром класса Smartphone, выбрасывается ошибка типа (TypeError).

#### utils.py

Модуль, содержащий утилитарную функцию для работы с JSON-файлом.

- `make_the_python_objects_from_json`: Функция для создания объектов из JSON-файла.
  - Параметры: `file_path` (путь до JSON-файла, опционально).
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
- test_category.py
- test_lawn_grass_product.py
- test_order
- test_print_mixin.py
- test_product.py
- test_smartphone_product.py
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
