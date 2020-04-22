import copy


class Door:
    def __init__(self):
        self._locked = False

    @property
    def is_locked(self):
        return self._locked

    @property
    def locked_status(self):
        return 'locked' if self._locked else 'unlocked'

    def lock(self):
        self._locked = True

    def unlock(self):
        self._locked = False


class CentralLock:
    def __init__(self):
        self.subscribers = {event: {} for event in ('lock', 'unlock')}

    def register(self, event: str, door_name: str, door: Door):
        self.subscribers[event].update({door_name: door})

    def unregister(self, event: str, door_name: str):
        del self.subscribers[event][door_name]

    def lock(self):
        for door_name, door in self.subscribers['lock'].items():
            door.lock()
            print(f'Door: {door_name} {door.locked_status}')

    def unlock(self):
        for door_name, door in self.subscribers['unlock'].items():
            door.unlock()
            print(f'Door: {door_name} {door.locked_status}')


class Car:
    _possible_doors = ('front left', 'front right', 'rear left', 'rear right', 'trunk')

    def __init__(self, brand, model, number_of_doors, door: Door, color):
        self.__brand = brand
        self.__model = model
        self.__number_of_doors = number_of_doors
        self.__color = color

        self.__doors = {self._possible_doors[i]: copy.copy(door) for i in range(number_of_doors - 1)}
        self.__doors.update({self._possible_doors[-1]: door})

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
        self.car = car
        self.central_lock = central_lock
        self.unlock_signal = False

        for door_name, door in self.car._Car__doors.items():
            self.central_lock.register('lock', door_name, door)

    def doors(self):
        self.car.doors()

    def lock(self, *args, **kwargs):
        self.central_lock.lock()
        self.unlock_signal = False

    def unlock(self, *args, **kwargs):
        if not self.unlock_signal:
            self.central_lock.register('unlock', 'front left', self.car._Car__doors['front left'])
            self.central_lock.unlock()
            self.unlock_signal = True
            self.central_lock.unregister('unlock', 'front left')

        elif self.unlock_signal:
            door_list = []
            for door_name, door in self.car._Car__doors.items():
                door_list.append([door_name, door])
            for door_num in range(1, len(door_list)):
                self.central_lock.register('unlock', door_list[door_num][0], door_list[door_num][1])
            self.central_lock.unlock()
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


if __name__ == '__main__':
    door = Door()
    central_lock = CentralLock()
    fiat = CarWithCentralLock(Fiat('panda', 3, door, 'niebieski'), central_lock)

    fiat.doors()

    fiat.lock('front left')
    print('-----FIRST UNLOCK------')
    fiat.unlock('front left')
    print('-----SECOND UNLOCK------')
    fiat.unlock('front left')
    print('-----------')
    fiat.lock('front left')
    print('-----FIRST UNLOCK------')
    fiat.unlock('front left')
    print('-----------')
    fiat.lock('front left')
    print('-----FIRST UNLOCK------')
    fiat.unlock('front left')