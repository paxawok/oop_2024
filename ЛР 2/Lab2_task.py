class Gun:
    """ Клас для представлення гармати"""
    def __init__(self, name, distance):
        """
        name - ім'я гармати
        distance - відстань вистрілу
        """
        self._name = name
        self._distance = distance

    def fire(self):
        """
        стріляємо
        """
        print(f"Гармата {self._name} вистрілила на відстань {self._distance} м.")


class Tank:
    def __init__(self, name, gun, speed):
        """
        name - ім'я танка
        gun - вид гармати для танка
        це екземпляр класу Gun, який ми при ініціалізації передаємо як параметр
        Композиція
        speed - швидкість танка
        """
        self._name = name
        self._gun = gun
        self._speed = speed
        print(f"\n---> Створено {self._name}. Вид гармати - {self._gun._name}, відстань стрільби - {self._gun._distance}.")

    def fire(self):
        """
        Викликаємо постріл
        """
        self._gun.fire()
    
    def move(self):
        print(f"\n---> {self._name} рухається зі швидкістю {self._speed} км/год.")

class LightTank(Tank):
    def __init__(self):
        light_gun = Gun("Light Cannon \"Легка\"", 3000)
        Tank.__init__(self, "Танк Легкий", light_gun, 60)
    
    def camouflage(self):
        self._speed += 5
        print(f"{self._name} застосовує камуфляж і приховується від ворожих очей.")


class MediumTank(Tank):
    def __init__(self):
        medium_gun = Gun("Medium Cannon \"Середня\"", 3800)
        Tank.__init__(self, "Танк Середній", medium_gun, 45)
    
    def rapid_fire(self):
        self._gun._distance += 200
        print(f"{self._name} використовує швидку вогневу підготовку для стрільби.")

class HeavyTank(Tank):
    def __init__(self):
        heavy_gun = Gun("Heavy Cannon \"Важка\"", 4200)
        Tank.__init__(self, "Танк Важкий", heavy_gun, 25)
    
    def deploy_minefield(self):
        self._speed += 5
        print(f"{self._name} розгортає мінне поле, ускладнюючи прохід ворожій техніці.")


def menu():
    print("\n1. Створити легкий танк")
    print("2. Створити середній танк")
    print("3. Створити важкий танк")
    print("4. Стріляти танком")
    print("5. Рухатися танком")
    print("6. Викликати особливий метод")
    print("7. Вийти\n")

def create_tank(tank_type):
    if tank_type == 1:
        return LightTank()
    elif tank_type == 2:
        return MediumTank()
    elif tank_type == 3:
        return HeavyTank()
    else:
        print("Невірний вибір")
        return None

def shoot(tank):
    if tank is not None:
        tank.fire()

def move(tank):
    if tank is not None:
        tank.move()

def special(tank):
    if isinstance(tank, HeavyTank):
        tank.deploy_minefield()
    elif isinstance(tank, MediumTank):
        tank.rapid_fire()
    elif isinstance(tank, LightTank):
        tank.camouflage()
    else:
        print("Виникла помилка. Перевірте, будь ласка, введені дані.")

def main():
    tank = None
    while True:
        menu()
        choice = int(input("Введіть вибір: \n"))
        match choice:
            case 1:
                tank = create_tank(1)
            case 2:
                tank = create_tank(2)
            case 3:
                tank = create_tank(3)
            case 4:
                shoot(tank)
            case 5:
                move(tank)
            case 6:
                special(tank)
            case 7:
                del tank
                break

if __name__ == "__main__":
    main()