import pytest

from src.oop import Category, Product

product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

category1 = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [product1, product2],
)
category2 = Category(
    "Телевизоры",
    "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    [product3],
)


@pytest.fixture
def products() -> tuple:
    """
    Фикстура, использующаяся для тестирования классов Product и Category.

    :return: Картеж экземпляров класса Product.
    """
    return product1, product2, product3


@pytest.fixture
def categories() -> tuple:
    """
    Фикстура, использующаяся для тестирования класса Category.

    :return: Картеж экземпляров класса Category.
    """
    return category1, category2


@pytest.fixture
def category_info() -> tuple:
    """
    Фикстура, использующаяся для тестирования класса Category.

    :return: Картеж атрибутов экземпляра класса Category.
    """
    return (
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    )


@pytest.fixture
def category_count() -> int:
    """
    Фикстура, возвращающая результат вызова метода category_count.

    :return: Результат вызова метода category_count.
    """
    return Category.category_count


@pytest.fixture
def product_count() -> int:
    """
    Фикстура, возвращающая результат вызова метода product_count.

    :return: Результат вызова метода product_count.
    """
    return Category.product_count


@pytest.fixture
def to_json() -> tuple:
    """
    Фикстура для тестирования функции make_the_python_objects_from_json.

    :return: Картеж данных для тестирования функции.
    """
    return (
        [
            {
                "name": "Смартфоны",
                "description": "Смартфоны, как средство не только коммуникации,\
                но и получение дополнительных функций для удобства жизни",
                "products": [
                    {
                        "name": "Samsung Galaxy C23 Ultra",
                        "description": "256GB, Серый цвет, 200MP камера",
                        "price": 180000.0,
                        "quantity": 5,
                    },
                    {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
                    {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
                ],
            },
            {
                "name": "Телевизоры",
                "description": "Современный телевизор, который позволяет наслаждаться просмотром,\
                станет вашим другом и помощником",
                "products": [
                    {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
                ],
            },
        ],
        [{"description": "test"}],
        [{"name": "test", "description": "test", "products": [{"description": "test"}]}],
    )


@pytest.fixture
def product_dict() -> tuple:
    return (
        {"name": "Phone", "description": "Some description", "price": 10000, "quantity": 1},
        {"name": "Phone", "description": "Some description", "price": 20000, "quantity": 1},
        {"name": "Phone", "description": "Some description", "price": 5000, "quantity": 1},
    )


# @pytest.fixture
# def new_product() -> Product:
#     return
