from abc import ABC, abstractmethod


class Cars(ABC):
    def __init__(self, model, color, doors):
        self.brand_name = None
        self.model = model
        self.color = color
        self.doors = doors

    @abstractmethod
    def brand(self):
        pass

    @abstractmethod
    def model_name(self):
        pass

    def introduce_car(self):
        pass


class Skoda(Cars):
    def __init__(self, model, color, doors):
        super().__init__(model, color, doors)
        self.brand_name = 'Skoda'

    def brand(self):
        print("Mercedes")

    def model_name(self):
        return self.model

    def indroduce_car(self):
        print(f"Brand: {self.brand_name}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Doors: {self.doors}")

class Ford(Cars):
    def __init__(self, model, color, doors):
        super().__init__(model, color, doors)
        self.brand_name = 'Ford'

    def brand(self):
        print("Ford")

    def model_name(self):
        return self.model

    def indroduce_car(self):
        print(f"Brand: {self.brand_name}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Doors: {self.doors}")

class Polonez(Cars):
    def __init__(self, model, color, doors):
        super().__init__(model, color, doors)
        self.brand_name = 'Polonez'

    def brand(self):
        print("Polonez")

    def model_name(self):
        return self.model

    def indroduce_car(self):
        print(f"Brand: {self.brand_name}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Doors: {self.doors}")


if __name__ == '__main__':
    skoda = Skoda('Fabia', 'red', 4)
    polonez = Polonez("The best shit ever", "white", 3)
    ford = Ford("Escort", 'pink', 4)

    skoda.indroduce_car()
    print('-----')
    polonez.indroduce_car()
    print('-----')
    ford.indroduce_car()
    print("-----")
    print(skoda.model_name())
