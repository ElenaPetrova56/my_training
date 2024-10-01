class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                products = file.read()
            return products.strip()
        except FileNotFoundError:
            return "Файл не найден"

    def add(self, *products):
        existing_products = {product.split(', ')[0] for product in self.get_products().splitlines() if product}

        for product in products:
            if product.name in existing_products:
                print(f"Продукт {product.name} уже есть в магазине")
            else:
                with open(self.__file_name, 'a') as file:
                    file.write(str(product) + '\n')


# Пример использования
if __name__ == "__main__":
    # Создаем несколько продуктов
    potato = Product('Potato', 50.0, 'Vegetables')
    apple = Product('Apple', 30.0, 'Fruits')
    banana = Product('Banana', 20.0, 'Fruits')

    # Создаем магазин
    shop = Shop()

    # Добавляем продукты в магазин
    shop.add(potato, apple)

    # Пытаемся добавить тот же продукт снова
    shop.add(potato)

    # Выводим продукты из магазина
    print("Товары в магазине:")
    print(shop.get_products())
