#Хід роботи
class Animal:
    kind = "warm-blooded"
    __counter = 0

    def __init__(self, name, speed):
        self.__name = name
        self.speed = speed
        Animal.__counter += 1
        #print(self.__name, ": now ", Animal.__counter, " animal exist")
        Animal.__printAmount(self.__name)
    
    def __del__(self):
        Animal.__counter -= 1
        #print("Now ", Animal.__counter, " animals left")
        Animal.__printAmount(self.__name)
    
    def __sayHello(self):
        print("Hello, I am ", self.__name, " my speed is ", self.speed)
    
    def speedUp(self, delta):
        self.speed = self.speed + delta

    def speedDown(self, delta):
        if (self.speed >= delta):
            self.speed = self.speed - delta
    
    def stop(self):
        self.speed = 0
    
    def getName(self):
        return self.__name
    
    @staticmethod
    def __printAmount(startMess):
        print(startMess, ": now ", Animal.__counter, " animals exist.")

#Створення екземплярів класу

an1 = Animal("Kitty", 1)
an2 = Animal("Puppy", 2)
an3 = Animal("Big dog", 5)

an3._Animal__sayHello()
an3.speedUp(20)

 
print(an1._Animal__name)
print(an1.getName())
print(an1._Animal__counter)
print(an1.__dict__)

del an1
del an2
del an3



