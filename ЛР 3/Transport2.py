from Transport1 import Transport
from Transport1 import ArithmeticSequence as arSeq
import collections.abc

testSeq = arSeq()

print(isinstance(testSeq, collections.abc.Container))
print(isinstance(testSeq, collections.abc.Sequence))


class ModernCar(Transport):
    def upgrade(self, x):
        pass
    pass

mc = ModernCar("ModernCar_instance", 100, 200, 300, 400)
mc.sayHello()