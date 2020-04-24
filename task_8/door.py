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


class FrontLeft(Door):
    pass


class FrontRight(Door):
    pass


class RearLeft(Door):
    pass


class RearRight(Door):
    pass


class Trunk(Door):
    pass


class DoorFactory:
    def __init__(self):
        self.__doors = {
            'front left': FrontLeft,
            'front right': FrontRight,
            'rear left': RearLeft,
            'rear right': RearRight,
            'trunk': Trunk
        }

    def create(self, doors_type):
        return self.__doors[doors_type]()
