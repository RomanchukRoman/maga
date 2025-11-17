class Vehicle:
    'Базовый класс транспортных средств'
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f'{self.year} {self.brand} {self.model}'

class Car(Vehicle):
    'Класс машин, наследующий базовый'
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def display_info(self):
        base_info = super().display_info()
        return f'{base_info} {self.num_doors} двери'

class Motorcycle(Vehicle):
    'Класс мотоциклов, наследующий базовый'
    def __init__(self, brand, model, year, engine_volume):
        super().__init__(brand, model, year)
        self.engine_volume = engine_volume

    def display_info(self):
        base_info = super().display_info()
        return f'{base_info} объем двигателя: {self.engine_volume}'

# Пример использования
machine = Vehicle("Toyota", "Camry", 2020)
car = Car("Toyota", "Camry", 2020, 4)
motorcycle = Motorcycle("Honda", "CB500", 2021, 471)

print(machine.display_info())
print(car.display_info())
print(motorcycle.display_info())