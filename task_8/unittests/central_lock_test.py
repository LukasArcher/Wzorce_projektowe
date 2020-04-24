import unittest

from unittest.mock import Mock
from Lesson_1.task_8.central_lock import CentralLock


class CentralLockTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.central_lock = CentralLock()

    def test_central_lock(self):
        mock_door = Mock()
        assert self.central_lock.register('lock', 'front left', mock_door) is None
        assert self.central_lock.register('unlock', 'front left', mock_door) is None
        assert self.central_lock.lock() is None
        assert self.central_lock.unlock() is None
        assert self.central_lock.unregister('lock', 'front left') is None


if __name__ == '__main__':
    unittest.main()

