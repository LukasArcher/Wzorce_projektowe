import unittest

from Lesson_1.task_8.door import Door, DoorFactory, FrontLeft


class DoorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.door = Door()
        self.door_factory = DoorFactory()

    def test_is_locked(self):
        assert self.door.is_locked is False

    def test_locked_status(self):
        assert self.door.locked_status == 'unlocked'

    def test_lock(self):
        assert self.door.lock() is None

    def test_unlock(self):
        assert self.door.unlock() is None

    def test_create(self):
        self.assertIsInstance(self.door_factory.create('front left'), FrontLeft)


if __name__ == '__main__':
    unittest.main()