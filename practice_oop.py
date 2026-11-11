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



Условие
Часть 1
Реализуйте иерархию транспортных средств (только через наследование):
• абстрактный класс Vehicle (наследник ABC) с абстрактным методом describe(self) -> str;
• подклассы по среде передвижения: GroundVehicle, WaterVehicle, AirVehicle;
• классы- конкретные транспортные средства: Car, Boat, Plane – в каждом переопределяется describe.
Вопрос: легко ли добавить новое транспортное средство наследованием?
Часть 2
Теперь добавьте тип привода: электрический, дизельный ДВС, гибридный.
Реализуйте через наследование от классов конкретных моделей (напр. ElectricCar, DieselCar, HybridCar и т.д.)
Добавьте назначение (гражданский / военный) (напр. ElectricCivilianCar, ElectricMilitaryCar и т.д.)
Вопрос: Сколько классов придется создать при 3 приводах, 2 назначениях, 3 видах транспорта?
Часть 3
Наследование не подходит для независимых свойств. Оно подходит для иерархии «является» (Car – это GroundVehicle), но не для «имеет/может» (машина имеет двигатель, самолет может стрелять)
Перепишите код:
• добавьте абстрактный класс двигатель, который будет отдельным объектом внутри транспортного средства. С абстрактными методами start -> str, fuel_type -> str
• добавьте классы конкретных двигателей: ElectricEngine, DieselEngine, HybridEngine
• Классы транспорта (Car, Ship, Plane) получают атрибут _engine: Engine через инициализатор.
• Двигатель должен инстанцироваться (создаваться) внутри транспорта или передаваться снаружи:
o если Car сам создает ElectricEngine() – это композиция (жесткая связь, двигатель не существует отдельно)
o если Car принимает Engine в инициализаторе – это агрегация (слабая связь, двигатель может быть общим или заменяемым)
• сделать так, чтобы можно было заменить двигатель у машины (добавить метод в класс)
Теперь количество классов: 3 (виды транспорта) + 3 (двигатели) = 6, а не 18. Добавление нового привода – это один новый класс, а не правка всей иерархии.
 
Часть 4
Реализуйте отдельный неабстрактный класс Fleet:
• хранит список транспортных средств (list[Vehicle]);
• транспорт создается снаружи и передается во флот – это агрегация (корабли живут сами по себе, флот их только группирует);
• методы: add(self, vehicle: Vehicle) -> None, print_all(self) -> list[str].
 
Теперь здесь Ship владеет двигателем (если запрограммировали через композицию), а Fleet агрегирует корабли (агрегация). Если флот удалить, корабли останутся.
 
Продемонстрировать:
• Реализованы: Vehicle, Engine (оба наследуются от ABC), минимум 3 модели транспорта, 3 двигателя, Fleet;
• Использованы: наследование (транспортное средство от Vehicle), композиция (_engine внутри машины, корабля и тд), агрегация (Fleet хранит список);
• Все классы используют __slots__;
• Аннотации типов везде;
• В демонстрации работоспособности: создание разного транспорта с разными двигателями, замена двигателя, добавление во флот, вывод описания.
 
Про лабораторную 3
 
В лабораторной №3 нельзя наследовать Logger под каждый способ вывода (ConsoleLogger, FileLogger, ConsoleFilteredLogger, ...). Нужно сделать Logger, который содержит списки фильтров, форматтеров и обработчиков, а сами они реализуют общие интерфейсы.
