class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parks  = [[big, 0], [medium, 0], [small, 0]]


    def addCar(self, carType: int) -> bool:
        park = self.parks[carType - 1]
        if park[1] < park[0]:
            park[1] += 1
            return True
        return False



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)