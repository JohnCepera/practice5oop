from abc import ABC, abstractmethod

class Engine(ABC):
    __slots__ = ()

    @abstractmethod
    def start(self) -> str:
        pass

    @abstractmethod
    def fuel_type(self) -> str:
        pass

class ElectricEngine(Engine):
    __slots__ = ()

    def start(self) -> str:
        return "Электродвигатель бесшумно запускается."

    def fuel_type(self) -> str:
        return "Электричество"

class DieselEngine(Engine):
    __slots__ = ()

    def start(self) -> str:
        return "Дизельный ДВС заводится с характерным рокотом."

    def fuel_type(self) -> str:
        return "Дизельное топливо"

class HybridEngine(Engine):
    __slots__ = ()

    def start(self) -> str:
        return "Гибридная система оптимизирует запуск (электро + ДВС)."

    def fuel_type(self) -> str:
        return "Бензин / Электричество"

class Vehicle(ABC):
    __slots__ = ('_engine',)

    def __init__(self, engine: Engine) -> None:
        self._engine: Engine = engine

    @abstractmethod
    def describe(self) -> str:
        pass

    def change_engine(self, new_engine: Engine) -> None:
        self._engine = new_engine

class GroundVehicle(Vehicle):
    __slots__ = ()

class WaterVehicle(Vehicle):
    __slots__ = ()

class AirVehicle(Vehicle):
    __slots__ = ()

class Car(GroundVehicle):
    __slots__ = ()

    def describe(self) -> str:
        return f"Автомобиль. Тип топлива: {self._engine.fuel_type()}. Статус: {self._engine.start()}"

class Boat(WaterVehicle):
    __slots__ = ()

    def describe(self) -> str:
        return f"Лодка/Корабль. Тип топлива: {self._engine.fuel_type()}. Статус: {self._engine.start()}"

class Plane(AirVehicle):
    __slots__ = ()

    def describe(self) -> str:
        return f"Самолет. Тип топлива: {self._engine.fuel_type()}. Статус: {self._engine.start()}"

class Fleet:
    __slots__ = ('_vehicles',)

    def __init__(self) -> None:
        self._vehicles: list[Vehicle] = []

    def add(self, vehicle: Vehicle) -> None:
        self._vehicles.append(vehicle)

    def print_all(self) -> list[str]:
        descriptions = [v.describe() for v in self._vehicles]
        return descriptions

if __name__ == "__main__":
    print("--- Демонстрация работы ---")
    
    # Создание двигателей
    electric = ElectricEngine()
    diesel = DieselEngine()
    hybrid = HybridEngine()
    
    # Создание транспорта (Агрегация: двигатели передаются извне)
    tesla = Car(electric)
    bmw = Car(diesel)
    prius = Car(hybrid)
    
    cargo_ship = Boat(diesel)
    fighter_jet = Plane(hybrid)
    
    # Создание флота и добавление транспорта
    my_fleet = Fleet()
    my_fleet.add(tesla)
    my_fleet.add(cargo_ship)
    my_fleet.add(fighter_jet)
    
    print("Состав флота изначально:")
    for desc in my_fleet.print_all():
        print(f"- {desc}")
        
    print("
--- Замена двигателя ---")
    print(f"До замены: {tesla.describe()}")
    # Меняем электромотор Теслы на дизель (для демонстрации метода замены)
    tesla.change_engine(diesel)
    print(f"После замены на дизель: {tesla.describe()}")
