def test_product_init(products: tuple) -> None:
    """
    Тестирует корректность инициализации объектов класса Product.

    :param products: Картеж экземпляров класса Product.
    :return: None.
    """
    assert products[0].name == 'Samsung Galaxy S23 Ultra'
    assert products[0].description == '256GB, Серый цвет, 200MP камера'
    assert products[0].price == 180000.0
    assert products[0].quantity == 5


def test_category_init(categories: tuple, category_info: tuple, products: tuple) -> None:
    """
    Тестирует корректность инициализации объектов класса Category.

    :param categories: Картеж экземпляров класса Category.
    :param category_info: Картеж атрибутов экземпляра класса Category.
    :param products: Картеж экземпляров класса Product.
    :return: None.
    """
    assert categories[0].name == category_info[0]
    assert categories[0].description == category_info[1]
    assert len(categories[0].products) == len(products[:2])


def test_category_category_count(category_count: int) -> None:
    """
    Тестирует подсчет количества продуктов.

    :param category_count: Результат вызова метода category_count.
    :return: None.
    """
    assert category_count == 2


def test_product_count(product_count: int) -> None:
    """
    Тестирует подсчет количества категорий.

    :param product_count: Результат вызова метода product_count.
    :return: None.
    """
    assert product_count == 3
