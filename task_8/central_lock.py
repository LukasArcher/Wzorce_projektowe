from Lesson_1.task_8.mismatched_door_adapter import DoorFactory


class CentralLock:
    def __init__(self):
        self.subscribers = {event: {} for event in ('lock', 'unlock')}

    def register(self, event: str, door_name: str, door: DoorFactory) -> None:
        self.subscribers[event].update({door_name: door})

    def unregister(self, event: str, door_name: str) -> None:
        del self.subscribers[event][door_name]

    def lock(self) -> None:
        for door_name, door in self.subscribers['lock'].items():
            door.lock()
            print(f'Door: {door_name} {door.locked_status}')

    def unlock(self) -> None:
        for door_name, door in self.subscribers['unlock'].items():
            door.unlock()
            print(f'Door: {door_name} {door.locked_status}')