class Length:
    """Клас для репрезентації мір довжини та дій над ними."""

    # Статичнi зміннi, константи
    VALUE_ERROR = "Неправильний формат данних."
    DIV_BY_ZERO = "Ділення на нуль не підтримується."
    DEFAULT_UNIT_SYMBOL = "m"

    instances = []

    unit_symbols = {
        "km":1000,
        "m": 1.0,
        "dm": 0.1,
        "cm": 0.01,
        "mm": 0.001
    }

    def convert(length, to_unit):
        """
        Конвертація довжини

        параметр length: значення довжини, яку конвертуємо
        параметр to_unit: значення міри довжини до якої конвертуємо
        return: нове значення довжини в потрібній мірі довжині
        """
        try:
            from_unit = length.unit
            factor = Length.unit_symbols[from_unit] / Length.unit_symbols[to_unit]
            return Length(length.value * factor, length.precision, to_unit)
        except ValueError:
            print(f"Помилка: {Length.VALUE_ERROR}")

    

    def __init__(self, value, precision=2, unit=None):
        """
        Ініціалізація  

        параметр value: значення для довжини
        параметр precision: число знаків після коми
        параметр unit: символьне позначення довжини (по дефолту m - метри)
        """
        self._value = round(value, precision)
        self._precision = precision
        self._unit = unit if unit else Length.DEFAULT_UNIT_SYMBOL
        Length.instances.append(self)

    def deleteObject(self):
        """
        Видалення об'єктів

        Після виклику даного метода об'єкт вилучається зі списку instance, куди додається при ініціалізації.
        """
        try:
            Length.instances.remove(self)
        except ValueError:
            print(f"Помилка: {Length.VALUE_ERROR}\n{self} не існує в списку екземплярів.")
        
    @staticmethod
    def print_instances():
        """
        Вивід об'єктів, що існують

        Після виклику даного метода об'єкти, що існують, виводяться на екран.
        """
        print("\nІснуючі об'єкти:")
        
        if not Length.instances:
            print("Пусто")
        else:
            for instance in Length.instances:
                print("| ", instance)
            
        

    """
    @property - геттер; можемо звертатися length.value щоб отримати значення замість length._value
    @variable.setter - сеттер; можемо задавати значення
    """
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = round(new_value, self.precision)

    @property
    def precision(self):
        return self._precision

    @precision.setter
    def precision(self, new_precision):
        self._precision = new_precision

    @property
    def unit(self):
        return self._unit
    
    @unit.setter
    def unit(self, new_unit):
        self._unit = new_unit

    def __add__(self, other):
        try:
            if not isinstance (other, (int, float)):
                raise ValueError(Length.VALUE_ERROR)
            self.value += other
            return self
        except ValueError as e:
            print("Помилка:", e)

    def __mul__(self, other):
        try:
            if not isinstance (other, (int, float)):
                raise ValueError(Length.VALUE_ERROR)
            self.value *= other
            return self
        except ValueError as e:
            print("Помилка:", e)

    def __sub__(self, other):
        try:
            if not isinstance (other, (int, float)):
                raise ValueError(Length.VALUE_ERROR)
            self.value -= other
            return self
        except ValueError as e:
            print("Помилка:", e)

    def __truediv__(self, other):
        try:
            if other == 0:
                raise ValueError(Length.DIV_BY_ZERO)
            elif not isinstance (other, (int, float)):
                raise ValueError(Length.VALUE_ERROR)
            self.value /= other
            return self
        except ValueError as e:
            print("Помилка:", e)

    # дозволяє виводити через print() значення, а не адресу
    def __str__(self):
        return f"{self.value:.{self.precision}f} {self.unit}"

def main():

    while (True):
        print("\n|-----МЕНЮ-----|\n")
        print("1 ---> Створення об'єкта")
        print("2 ---> Виведення списку об'єктів, що існують")
        print("3 ---> Операції ДВМД")
        print("4 ---> Зміна міри довжини об'єкта")       
        print("5 ---> Видалення об'єктa")
        print("6 ---> Exit\n")
        x = input("Обрати: ")

        match x:
            case "1":
                """1. Створюю об'єкт, вводячи всі дані з клавіатури"""

                value = float(input("Введіть довжину: "))
                precision = int(input("Введіть кількість знаків після коми: "))
                unit = input("\n km - кілометри,\n m - метри,\n dm - дециметри,\n cm - сантиметри,\n mm - міліметри,\n\nВведіть міру довжини: ")
                new_object_0 = Length(value, precision, unit)
                print(new_object_0)

                """2. Створюю об'єкт просто отримуючи значення довжини"""

                value = float(input("\nВведіть довжину: "))
                new_object_1 = Length(value)                # Повинен бути об'єкт Value.00 m
                print(new_object_1)

            case "2":
                Length.print_instances()

            case "3":
                
                print(f"\nОперація додавання: {new_object_0} + 90 = ", end='')
                new_object_0 + 90
                print(new_object_0)

                print(f"Операція додавання з помилкою: {new_object_0} + 9О = ", end='')
                new_object_0 + "9О"
                print(new_object_0)

                print(f"\nОперація віднімання: {new_object_0} - 90 = ", end='')
                new_object_0 - 90
                print(new_object_0)

                print(f"Операція віднімання з помилкою: {new_object_0} + 9O = ", end='')
                new_object_0 - "9О"
                print(new_object_0)

                print(f"\nОперація множення: {new_object_0} * 9 = ", end='')
                new_object_0 * 9
                print(new_object_0)

                print(f"Операція множення з помилкою: {new_object_0} * ч = ", end='')
                new_object_0 * "ч"
                print(new_object_0)

                print(f"\nОперація ділення: {new_object_0} / 90 = ", end='')
                new_object_0 / 90
                print(new_object_0)

                print(f"Операція ділення на нуль: {new_object_0} / 0 = ", end='')
                new_object_0 / 0
                print(new_object_0)

                print(f"Операція ділення з помилкою: {new_object_0} / ц = ", end='')
                new_object_0 / "ц"
                print(new_object_0)

            case "4":
                new_unit = input(f"\nВведіть нову міру довжини для {new_object_0}: ")
                new_object_0_unit = Length.convert(new_object_0, new_unit)
                print(new_object_0_unit)

            case "5":
                Length.print_instances()
                print(f"\nВидалимо {new_object_0}: ")
                new_object_0.deleteObject()
                Length.print_instances()

            case "6":
                break
                

if __name__ == "__main__":
    main()