class Transport: #superclass

    def __init__(self, name, weight, height, length, loading):
        self._name = name
        self._weight = weight
        self._height = height
        self._length = length
        self._loading = loading
        self._speed = 0

    def sayHello(self):
        print("Hello, I am ", self._name)

class Watercraft(Transport):

    def __init__(self, waterSpeedNominal, waterCarryingCapacity, name, weight, height, length, loading):
        Transport.__init__(self, name, weight, height, length, loading)
        self._waterSpeedNom = waterSpeedNominal
        self._waterCarCap = waterCarryingCapacity

    def sailing(self, distance):
        self._speed = self._waterSpeedNom * self._waterCarCap / self._loading
        print(self._name, " is sayling, current speed ", self._speed, " duration ", distance / self._speed)
        return distance/self._speed

class Vehicle(Transport):

    def __init__(self, landSpeedNominal, landCarryingCapacity, name, weight, height, length, loading):
        Transport.__init__(self, name, weight, height, length, loading)
        self._landSpeedNom = landSpeedNominal
        self._landCarCap = landCarryingCapacity

    def riding(self, distance):
        self._speed = self._landSpeedNom * self._landCarCap/self._loading
        print(self._name, " is riding, current speed ", self._speed, " duration ", distance/self._speed)
        return distance/self._speed

class Amfibia(Vehicle, Watercraft): #subclass

    def __init__(self, name, weight, height, length, loading, landSpeedNominal, landCarryingCapacity, waterSpeedNominal, waterCarryingCapacity):
        Vehicle.__init__(self, landSpeedNominal, landCarryingCapacity, name, weight, height, length, loading)
        Watercraft.__init__(self, waterSpeedNominal, waterCarryingCapacity, name, weight, height, length, loading)

    def __del__(self):
        print("An instance of class Amfibia ", self._name, " was destroyed")
    
    def run(self, route):
        print("Amfibia ", self._name, " started")
        totalTime = 0
        for i in range(len(route)):
            if route[i][0] == "land":
                totalTime = totalTime + self.riding(route[i][1])
            else:
                totalTime = totalTime + self.sailing(route[i][1])
        
        print("Amfibia ", self._name, " stoped")
        return totalTime

curRoute = [["land", 100], ["water", 3], ["land", 50], ["water", 2], ["land", 75]]
amf = Amfibia("Carol", 1500, 1, 3, 500, 100, 2000, 50, 500)
print("Time of trip ", amf.run(curRoute))
del amf
