import copy


class Door:
    pass


class Car:
    def __init__(self, brand, model, number_of_doors, color, door: Door):
        self.__brand = brand
        self.__model = model
        self.__number_of_doors = number_of_doors
        self.__color = color

        self.__doors = [copy.copy(door) for _ in range(number_of_doors - 1)]
        self.__doors.append(door)

    def doors(self):
        for door in self.__doors:
            print(id(door))

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


class Fiat(Car):
    def __init__(self, model, number_of_doors, color, door):
        super(Fiat, self).__init__('Fiat', model, number_of_doors, color, door)


if __name__ == '__main__':
    user_door = Door()
    fiat = Fiat('panda', 5, 'niebieski', user_door)
    fiat.color = "blue"
    print(fiat.color)
    print(fiat.brand)

    print(vars(fiat))
    fiat.doors()
