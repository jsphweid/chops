class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.counts = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.counts[carType]:
            self.counts[carType] -= 1
            return True
        return False

