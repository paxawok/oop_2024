from abc import ABCMeta
from abc import abstractmethod
import collections.abc

class Transport(metaclass=ABCMeta):

    def __init__(self, name, weight, height, length, loading):
        self._name = name
        self._weight = weight
        self._length = length
        self._height = height
        self._loading = loading
        self._speed = 0
    
    def sayHello(self):
        print("Hello, I am ", self._name)

    @abstractmethod
    def upgrade(self, x):
        pass

class ArithmeticSequence():

    def __isint (self, num):
        try:
            int(num)
            return True
        except ValueError:
            return False
    
    def __init__(self, base=0, step=1):
        self.base = base
        self.step = step
        self.curLen = 1
        self.maxLen = 100
    
    def __getitem__(self, key):
        if (not(self.__isint(key)) or (key < 0)):
            raise TypeError("Key must be 0 or positive integer")
        if (key > self.curLen):
            raise IndexError("Index out of range")
        return self.base + (key-1) * self.step
    
    def __len__(self):
        return self.curLen
    
    def __contains__(self, num):
        check = (num-self.base) % self.step
        if (check == 0) and (self.curLen >= ((num - self.base) // self.step + 1)):
            return True
        else:
            return False
    
    def index(self, num):
        check = (num - self.base) % self.step
        if (check != 0) or (self.curLen < ((nem - self.base) // self.step + 1)):
            raise ValueError("Is not in ArithmeticSequence")
        return (num - self.base) // self.step + 1
    
    def count(self, num):
        check - (num - self.base) % self.step
        if (check == 0) and (self.curLen >= ((num - self.base) // self.step + 1)):
            return 1
        else:
            return 0
    
    def increaseTo(self, count):
        if (count <= self.curLen):
            return
        if (count < self.maxLen):
            self.curLen = count
        else:
            self.curLen = self.maxLen
    
    def decreaseTo(self, count):
        if (count >= self.curLen):
            return
        if (count < 0):
            self.curLen = 0
        else:
            self.curLen = count

collections.abc.Sequence.register(ArithmeticSequence)