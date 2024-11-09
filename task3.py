# Создайте классы для представления структуры магазина техники.

# Требования:

# Базовый класс Device, который будет представлять общие атрибуты
# для любой техники:

# атрибуты: brand, model, price.
# метод get_info(), который возвращает строку с кратким описанием устройства.
# Дочерние классы:

# Laptop с дополнительными атрибутами ram и storage.
# Smartphone с атрибутами camera_megapixels и battery_capacity.

# Каждый из классов должен переопределить метод get_info()
# для включения специфичной информации.
# Создайте класс Store, содержащий список устройств:

# Метод add_device(device), который добавляет устройство в магазин.
# Метод list_devices(), который выводит информацию обо всех устройствах.

class Device:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def get_info(self):
        return self.brand, self.model, self.price

class Laptop(Device):
    def __init__(self, brand, model, price, ram, storage):
        super().__init__(brand, model, price)
        self.ram = ram
        self.storage = storage

    def get_info(self):
        return self.brand, self.model, self.price, self.ram, self.storage

class Smartphone(Device):
    def __init__(self, brand, model, price, camera_megapixels, battery_capacity):
        super().__init__(brand, model, price)
        self.camera_megapixels = camera_megapixels
        self.battery_capacity = battery_capacity

    def get_info(self):
        return self.brand, self.model, self.price, self.camera_megapixels, self.battery_capacity

class Store:
    def __init__(self):
        self.lst = []
    def add_device(self, device):
        self.lst.append(device)

    def list_devices(self):
        for i in self.lst:
            print(list(i.get_info()))

laptop = Laptop("Lenovo", "V-777", 25000, "4gb", "S2200" )
laptop2 = Laptop("Asus", "V-117", 55000, "3gb", "S2700" )
print(laptop.get_info())
new_latop = Store()
new_latop.add_device(laptop)
new_latop.add_device(laptop2)
new_latop.list_devices()

smartphone1 = Smartphone('Androud', "Nokia", "G22", 10, 3000)
smartphone2 = Smartphone('Androud', "Realme", "10", 11, 3700)
new_latop2 = Store()
new_latop2.add_device(smartphone1)
new_latop2.add_device(smartphone2)
new_latop2.list_devices()