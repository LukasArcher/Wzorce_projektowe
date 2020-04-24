from unittest import TestCase, main as mytest
from unittest.mock import Mock
from Lesson_1.task_8.car_with_central_lock import Fiat, CarWithCentralLock, Car, Audi, Rover


class CarTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.mock_door_factory = Mock()
        cls.mock_central_lock = Mock()
        cls.car = Car("Fiat", "Panda", 3, cls.mock_door_factory, 'blue')
        cls.car_with_cl = CarWithCentralLock(cls.car, cls.mock_central_lock)

    def test_doors(self):
        assert self.car_with_cl.doors() is None

    def test_lock(self):
        assert self.car_with_cl.lock() is None
        assert self.car.lock('trunk') is None

    def test_unlock(self):
        assert self.car_with_cl.unlock() is None
        assert self.car.unlock('trunk') is None

        self.car_with_cl.unlock_signal = True
        assert self.car_with_cl.unlock() is None

    def test_register(self):
        assert self.car_with_cl.register() is None

    def test_unregister(self):
        assert self.car_with_cl.unregister() is None

    def test_fiat(self):
        self.fiat = Fiat("Panda", 3, self.mock_door_factory, 'red')
        self.assertIsInstance(self.fiat, Car)

    def test_audi(self):
        self.audi = Audi("A8", 3, self.mock_door_factory, 'black')
        self.assertIsInstance(self.audi, Car)

    def test_rover(self):
        self.rover = Rover("75", 3, self.mock_door_factory, 'white')
        self.assertIsInstance(self.rover, Car)

    def test_color_setter(self):
        self.car.color = 'purple'
        assert self.car.color == "purple"


if __name__ == '__main__':
    mytest()
