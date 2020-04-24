from Lesson_1.task_8.car_with_central_lock import CarWithCentralLock, Fiat
from Lesson_1.task_8.central_lock import CentralLock
from Lesson_1.task_8.mismatched_door_adapter import DoorFactory as DoorFactoryFromMismatchedDoor

if __name__ == '__main__':
    door_factory = DoorFactoryFromMismatchedDoor()
    central_lock = CentralLock()
    fiat = CarWithCentralLock(Fiat('panda', 5, door_factory, 'niebieski'), central_lock)

    fiat.doors()
    print('--------')

    fiat.lock('front left')
    print('-----FIRST UNLOCK------')
    fiat.unlock('front left')
    print('-----SECOND UNLOCK------')
    fiat.unlock('front left')
    print('-----------')