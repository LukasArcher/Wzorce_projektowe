from Lesson_1.task_8.central_lock import CentralLock
from Lesson_1.task_8.door import DoorFactory


class Car:
    _possible_doors = ('front left', 'front right', 'rear left', 'rear right', 'trunk')

    def __init__(self, brand, model, number_of_doors, door: DoorFactory, color):
        self._Car__doors = None
        self.__brand = brand
        self.__model = model
        self.__number_of_doors = number_of_doors
        self.__color = color
        self.door_factory = door

        self.__doors = {self._possible_doors[i]: self.door_factory.create(self._possible_doors[i])
                        for i in range(number_of_doors - 1)}
        self.__doors.update({self._possible_doors[-1]: self.door_factory.create('trunk')})

    def lock(self, door_name):
        """Klasa zyskała metodę do zamykania drzwi."""
        self.__doors[door_name].lock()
        print(f'Door: {door_name} {self.__doors[door_name].locked_status}')

    def unlock(self, door_name):
        """Klasa zyskała metodę do otwierania drzwi."""
        self.__doors[door_name].unlock()
        print(f'Door: {door_name} {self.__doors[door_name].locked_status}')

    def doors(self):
        for door_name, door in self.__doors.items():
            print(f'{door_name}: {id(door)}')

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def number_of_doors(self):
        return self.__number_of_doors

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


class CarWithCentralLock(Car):
    """Wzorzec dekorator poprzez udekorowanie klasy inną klasą."""

    def __init__(self, car: Car, central_lock: CentralLock):
        super().__init__(car.brand, car.model, car.number_of_doors, car.door_factory, car.color)
        self.car = car
        self.central_lock = central_lock
        self.unlock_signal = False

        for door_name, door in self.car._Car__doors.items():
            self.central_lock.register('lock', door_name, door)

    def doors(self) -> None:
        self.car.doors()

    def lock(self, *args, **kwargs) -> None:
        self.central_lock.lock()
        self.unlock_signal = False

    def unlock(self, *args, **kwargs) -> None:
        self.register()
        self.central_lock.unlock()
        self.unregister()

    def register(self) -> None:
        if not self.unlock_signal:
            self.central_lock.register('unlock', 'front left', self.car._Car__doors['front left'])

        elif self.unlock_signal:
            door_list = []
            for door_name, door in self.car._Car__doors.items():
                door_list.append([door_name, door])
            for door_num in range(1, len(door_list)):
                self.central_lock.register('unlock', door_list[door_num][0], door_list[door_num][1])

    def unregister(self) -> None:
        if not self.unlock_signal:
            self.unlock_signal = True
            self.central_lock.unregister('unlock', 'front left')

        elif self.unlock_signal:
            self.unlock_signal = False
            door_list = []
            for door_name in self.car._Car__doors.keys():
                door_list.append(door_name)
            for door_num in range(1, len(door_list)):
                self.central_lock.unregister('unlock', door_list[door_num])


class Fiat(Car):
    def __init__(self, *args, **kwargs):
        super(Fiat, self).__init__('Fiat', *args, **kwargs)


class Audi(Car):
    def __init__(self, *args, **kwargs):
        super(Audi, self).__init__('Audi', *args, **kwargs)


class Rover(Car):
    def __init__(self, *args, **kwargs):
        super(Rover, self).__init__('Rover', *args, **kwargs)