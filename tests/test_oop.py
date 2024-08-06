from unittest.mock import patch

from src.oop import Category, Product


def test_product_init(products: tuple) -> None:
    """
    Тестирует корректность инициализации объектов класса Product.

    :param products: Картеж экземпляров класса Product.
    :return: None.
    """
    assert products[0].name == "Samsung Galaxy S23 Ultra"
    assert products[0].description == "256GB, Серый цвет, 200MP камера"
    assert products[0].price == 180000.0  # Тест price-геттера
    assert products[0].quantity == 5


def test_category_init(categories: tuple, category_info: tuple, products: tuple) -> None:
    """
    Тестирует корректность инициализации объектов класса Category.

    :param categories: Картеж экземпляров класса Category.
    :param category_info: Картеж атрибутов экземпляра класса Category.
    :param products: Картеж экземпляров класса Product.
    :return: None.
    """
    products_str = "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт.\n" "Iphone 15, 210000 руб. Остаток: 8 шт."

    assert categories[0].name == category_info[0]
    assert categories[0].description == category_info[1]
    assert categories[0].products == products_str  # Тест products-геттера


def test_category_category_count(category_count: int) -> None:
    """
    Тестирует подсчет количества продуктов.

    :param category_count: Результат вызова метода category_count.
    :return: None.
    """
    assert category_count == 2


def test_category_product_count(product_count: int) -> None:
    """
    Тестирует подсчет количества категорий.

    :param product_count: Результат вызова метода product_count.
    :return: None.
    """
    assert product_count == 3


def test_category_add_product(categories: tuple, products: tuple) -> None:
    """
    Тестирует метод add_product.

    :param categories: Картеж экземпляров класса Category.
    :param products: Картеж экземпляров класса Product.
    :return: None.
    """
    categories[0].add_product(products[2])
    assert Category.product_count == 4


def test_new_product(product_dict: tuple) -> None:
    """
    Тестирует создание нового товара.

    :param product_dict: Картеж со словарями для создания товаров.
    :return: None.
    """
    product4 = Product.new_product(product_dict[0])

    assert product4.name == product_dict[0]["name"]
    assert product4.description == product_dict[0]["description"]
    assert product4.price == product_dict[0]["price"]  # 10_000
    assert product4.quantity == product_dict[0]["quantity"]  # Количество: 1


def test_new_product_update_quantity(product_dict: tuple) -> None:
    """
    Тестирует создание такого же товара с обновлением количества товара.

    :param product_dict: Картеж со словарями для создания товаров.
    :return: None.
    """
    product5 = Product.new_product(product_dict[0])

    assert product5.name == product_dict[0]["name"]
    assert product5.description == product_dict[0]["description"]
    assert product5.price == product_dict[0]["price"]  # 10_000
    assert product5.quantity == 2  # Количество: 2


def test_new_product_update_price_and_quantity(product_dict: tuple) -> None:
    """
    Тестирует создание такого же товара с обновлением и цены и количества товара.

    :param product_dict: Картеж со словарями для создания товаров.
    :return: None.
    """
    product6 = Product.new_product(product_dict[1])

    assert product6.name == product_dict[1]["name"]
    assert product6.description == product_dict[1]["description"]
    assert product6.price == product_dict[1]["price"]  # 20_000
    assert product6.quantity == 3  # Количество: 3


def test_new_product_update_only_quantity(product_dict: tuple) -> None:
    """
    Тестирует создание такого же товара (с меньшей стоимостью) с обновлением количества товара.

    :param product_dict: Картеж со словарями для создания товаров.
    :return: None.
    """
    product6 = Product.new_product(product_dict[2])  # product_dict[2]['price'] = 5_000

    assert product6.name == product_dict[2]["name"]
    assert product6.description == product_dict[2]["description"]
    assert product6.price == 20_000  # 20_000
    assert product6.quantity == 4  # Количество: 3


def test_product_set_higher_price(products: tuple) -> None:
    """
    Тестирует price-сеттер на установке большей цены.

    :param products: Картеж с товарами.
    :return: None.
    """
    product = products[0]
    assert product.price == 180_000  # Цена до использования сеттера

    product.price = 200_000
    assert product.price == 200_000


def test_product_set_lower_price(products: tuple) -> None:
    """
    Тестирует price-сеттер на установке меньшей цены.

    :param products: Картеж с товарами.
    :return: None.
    """
    product = products[0]
    assert product.price == 200_000  # Цена до использования сеттера

    # Установка меньшей цены
    with patch("builtins.input", return_value="y"):
        product.price = 100_000

    assert product.price == 100_000  # Цена после использования сеттера

    # Отказ при установке меньшей цены
    with patch("builtins.input", return_value="n"):
        product.price = 50_000

    assert product.price == 100_000  # Цена после использования сеттера


def test_product_set_negative_price(products: tuple) -> None:
    """
    Тестирует price-сеттер на установке отрицательной цены.

    :param products: Картеж с товарами.
    :return: None.
    """
    product = products[0]
    assert product.price == 100_000  # Цена до использования сеттера

    product.price = -10
    assert product.price == 100_000
