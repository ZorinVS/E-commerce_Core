from typing import List


class Product:
    """Класс для представления продукта."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод для инициализации экземпляра класса Product."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категории."""

    name: str
    description: str
    products: list
    category_count: int
    product_count: int

    # Переменные на уровне класса для ведения подсчетов
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        """Метод для инициализации экземпляра класса Category."""
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
