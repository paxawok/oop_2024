from abc import ABC, abstractmethod
import collections 

class Passenger:
    """Клас для представлення пасажира"""
    def __init__(self, name):
        """
        name - ім'я пасажира
        """
        self.name = name

class Wagon(ABC):
    """Клас для вагонів потяга, абстрактний"""
    def __init__(self, wagon_number, wagon_type):
        """wagon_number - номер вагона"""
        self._wagon_number = wagon_number
        self._passengers = collections.OrderedDict()
        self._wagon_type = wagon_type
    
    @property
    def wagon_number(self):
        return self._wagon_number

    @abstractmethod
    def add_passenger(self, passenger):
        pass

    @abstractmethod
    def remove_passenger(self, passenger):
        pass

    def __str__(self):
        return f"Вагон {self.wagon_number} ({self.wagon_type})"

class CoupeWagon(Wagon):
    """Клас для представлення купейного вагона"""
    def __init__(self, wagon_number, wagon_type = "K"):
        super().__init__(wagon_number, wagon_type = "K")

    def add_passenger(self, passenger):
        """
        Додає пасажира до вагона
        """
        if len(self._passengers) < 18:
            self._passengers[len(self._passengers)] = passenger
        else:
            raise ValueError(f"Вагон {self._wagon_number} переповнений")

    def remove_passenger(self, passenger):
        """
        Видаляє пасажира з вагона
        """
        for key, value in self._passengers.items():
            if value == passenger:
                del self._passengers[key]
                break

class PlackartWagon(Wagon):
    """Клас для представлення плацкартного вагона"""
    def __init__(self, wagon_number, wagon_type = "П"):
        super().__init__(wagon_number, wagon_type = "П")

    def add_passenger(self, passenger):
        """
        Додає пасажира до вагона
        """
        if len(self._passengers) < 54:
            self._passengers[len(self._passengers)] = passenger
        else:
            raise ValueError(f"Вагон {self._wagon_number} переповнений")

    def remove_passenger(self, passenger):
        """
        Видаляє пасажира з вагона
        """
        for key, value in self._passengers.items():
            if value == passenger:
                del self._passengers[key]
                break
class Train(object):
    """Клас для представлення потяга"""
    def __init__(self):
        self._wagons = []

    def add_wagon(self, wagon):
        """
        Додає вагон до потяга
        """
        self._wagons.append(wagon)

    def remove_wagon(self, wagon):
        """
        Видаляє вагон з потяга
        """
        if wagon in self._wagons:
            self._wagons.remove(wagon)

    def add_passenger(self, wagon_number, passenger, seat):
        """
        Додає пасажира до вагона за номером і місцем
        """
        wagon = next((wagon for wagon in self._wagons if wagon.wagon_number == wagon_number), None)
        if wagon is not None:
            wagon.add_passenger(passenger)
        else:
            raise ValueError(f"Вагон {wagon_number} не знайдено")

    def remove_passenger(self, wagon_number, passenger):
        """
        Видаляє пасажира з вагона за номером вагона і пасажиром
        """
        wagon = next((wagon for wagon in self._wagons if wagon.wagon_number == wagon_number), None)
        if wagon is not None:
            wagon.remove_passenger(passenger)
        else:
            raise ValueError(f"Вагон {wagon_number} не знайдено")

    def __str__(self):
        result = ""
        for wagon in self._wagons:
            result += str(wagon) + "\n"
        return result


train = Train()
train.add_wagon(CoupeWagon(1))
train.add_wagon(PlackartWagon(2))
train.add_wagon(CoupeWagon(3))

train.add_passenger(1, Passenger("Іван"), 2)
train.add_passenger(3, Passenger("Петро"), 12)

print(train)

train.remove_passenger(1, Passenger("Іван"))
train.remove_passenger(3, Passenger("Петро"))

print(train)