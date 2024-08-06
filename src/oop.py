from typing import List


class Product:
    """Класс для представления продукта."""

    # Атрибут на уровне класса для хранения экземпляров класса в виде списка
    all_products: List["Product"] = list()

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации экземпляра класса Product."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.all_products.append(self)

    @property
    def price(self) -> float:
        """Геттер для получения цены."""
        return self.__price

    @price.setter
    def price(self, amount: float) -> None:
        """Сеттер для установки цены."""
        if amount <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif amount < self.__price:
            difference = self.__price - amount
            confirmation = input(f"Вы уверены, что хотите снизить цену на {difference} руб? (y/n): ").lower()
            # self.__price = amount if confirmation == 'y' else print('Цена осталась прежней')
            if confirmation == "y":
                self.__price = amount
            else:
                print("Цена осталась прежней")
        else:
            self.__price = amount

    @classmethod
    def new_product(cls, product_dict: dict) -> "Product":
        """Класс-метод для создания нового продукта или обновления существующего."""
        name = product_dict.get("name", "")
        description = product_dict.get("description", "")
        price = product_dict.get("price", 0.0)
        quantity = product_dict.get("quantity", 0)

        # Проверка наличия такого же товара схожего по имени
        for product in Product.all_products:
            if name == product.name:
                # Обновление количества товара
                product.quantity += quantity
                # Обновление цены, если новая цена выше
                if price > product.price:
                    product.price = price
                return product

        # Создание нового товара, если не найдено совпадений
        return cls(name, description, price, quantity)


class Category:
    """Класс для представления категории."""

    # Атрибуты на уровне класса для ведения подсчетов
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        """Метод для инициализации экземпляра класса Category."""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Метод для добавления продукта в экземпляр класса Category."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для получения списка продуктов в виде строк."""
        return "\n".join(
            f"{product.name}, {round(product.price)} руб. Остаток: {product.quantity} шт."
            for product in self.__products
        )
