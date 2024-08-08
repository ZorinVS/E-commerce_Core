from typing import List


class Product:
    """Класс для представления продукта."""

    # Атрибут на уровне класса для хранения экземпляров класса в виде списка
    all_products: List["Product"] = list()

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Dunder-метод для инициализации экземпляра класса Product."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.all_products.append(self)

    def __str__(self) -> str:
        """Dunder-метод для строкового отображения информации об объекте."""
        return f"{self.name}, {round(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> int:
        """Dunder-метод для сложения товаров и получения полной стоимости всех товаров на складе."""
        # if not isinstance(other, Product):
        #     raise ValueError("Складывать можно только экземпляры класса Product")
        return round(self.price * self.quantity + other.price * other.quantity)

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


class Category:
    """Класс для представления категории."""

    # Атрибуты на уровне класса для ведения подсчетов
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        """Dunder-метод для инициализации экземпляра класса Category."""
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Dunder-метод для строкового отображения информации об объекте."""
        total = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total} шт."

    def add_product(self, product: Product) -> None:
        """Метод для добавления продукта в экземпляр класса Category."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для получения списка продуктов в виде строк."""
        return "\n".join(str(product) for product in self.__products)

    @property
    def products_list(self) -> List[Product]:
        """Геттер для получения списка продуктов."""
        return self.__products


class CategoryProductsIterator:
    """Вспомогательный класс для итерации по товарам в категории."""

    def __init__(self, category: Category) -> None:
        """Dunder-метод для инициализации итератора с объектом категории."""
        self.__category = category
        self.__index = 0

    def __iter__(self) -> "CategoryProductsIterator":
        """Dunder-метод для возврата итератора."""
        return self

    def __next__(self) -> Product:
        """Dunder-метод для получения следующего товара в категории."""
        if self.__index < len(self.__category.products_list):
            product = self.__category.products_list[self.__index]
            self.__index += 1
            return product
        else:
            raise StopIteration
