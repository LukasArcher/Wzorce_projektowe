class MismatchedDoorAdapter:
    def __init__(self):
        self.mismatched_door = MismatchedDoor()
        self._locked = self.mismatched_door.is_locked

    @property
    def is_locked(self):
        return self.mismatched_door.is_locked

    @property
    def locked_status(self):
        return 'locked' if self._locked else 'unlocked'

    def lock(self):
        return self.mismatched_door.lock_the_mismatched__door()

    def unlock(self):
        return self.mismatched_door.unlock_the_mismatched_door()


class MismatchedDoor:
    def __init__(self):
        self._is_locked = False

    @property
    def is_locked(self):
        return self._is_locked

    def lock_the_mismatched__door(self):
        self._is_locked = True

    def unlock_the_mismatched_door(self):
        self._is_locked = False


class FrontLeft(MismatchedDoorAdapter):
    pass


class FrontRight(MismatchedDoorAdapter):
    pass


class RearLeft(MismatchedDoorAdapter):
    pass


class RearRight(MismatchedDoorAdapter):
    pass


class Trunk(MismatchedDoorAdapter):
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