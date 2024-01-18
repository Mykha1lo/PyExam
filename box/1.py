import math
from abc import ABC, abstractmethod

# Абстрактний клас Box (коробка) є базовим класом для об'єктів Cube і Cylinder.
class Box(ABC):
    @abstractmethod
    def calculate_volume(self):
        # Абстрактний метод для обчислення об'єму. Має бути реалізований в кожному конкретному підкласі.
        pass

    @abstractmethod
    def calculate_surface_area(self):
        # Абстрактний метод для обчислення площі поверхні. Має бути реалізований в кожному конкретному підкласі.
        pass

# Клас Cube (куб), який успадковує від Box.
class Cube(Box):
    def __init__(self, side_length):
        # Конструктор ініціалізує довжину сторони куба та встановлює висоту на None для уніфікації інтерфейсу.
        if side_length < 0:
            raise ValueError("Side length must be non-negative.")
        self.side_length = side_length
        self.height = None  # Додаємо поле height для уніфікації інтерфейсу.

    def calculate_volume(self):
        # Метод для обчислення об'єму куба.
        return self.side_length ** 3

    def calculate_surface_area(self):
        # Метод для обчислення площі поверхні куба.
        return 6 * self.side_length ** 2

# Клас Cylinder (циліндр), який успадковує від Box.
class Cylinder(Box):
    def __init__(self, radius, height):
        # Конструктор ініціалізує радіус та висоту циліндра, перевіряючи, чи вони не від'ємні.
        if radius < 0:
            raise ValueError("Radius must be non-negative.")
        if height < 0:
            raise ValueError("Height must be non-negative.")
        self.radius = radius
        self.height = height

    def calculate_volume(self):
        # Метод для обчислення об'єму циліндра.
        return math.pi * self.radius ** 2 * self.height

    def calculate_surface_area(self):
        # Метод для обчислення площі поверхні циліндра.
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * self.radius ** 2

# Список box_list для зберігання об'єктів типу Box.
box_list = []

# Функція для виведення інформації про об'єкт Box.
def print_box_info(box):
    # Виводимо тип фігури, довжину сторони (або радіус), висоту, об'єм та площу поверхні.
    print(f"Type: {type(box).__name__}")
    print(f"Side length: {box.side_length if isinstance(box, Cube) else box.radius}")
    print(f"Height: {box.height if isinstance(box, Cylinder) else None}")
    print(f"Volume: {box.calculate_volume()}")
    print(f"Surface area: {box.calculate_surface_area()}")

# Функція для збереження інформації про об'єкти у CSV-файлі.
def save_box_list(box_list, filename):
    with open(filename, "w") as file:
        for box in box_list:
            # Записуємо дані у форматі CSV (Comma-Separated Values).
            file.write(f"{type(box).__name__},{box.side_length if isinstance(box, Cube) else box.radius},{box.height if isinstance(box, Cylinder) else None},{box.calculate_volume()},{box.calculate_surface_area()}\n")

# Функція для введення параметрів куба з клавіатури.
def input_cube_params():
    # Вводимо довжину сторони куба, перевіряючи, чи введено коректне числове значення.
    side_length = float(input("Enter the side length of the cube: "))
    return Cube(side_length)

# Функція для введення параметрів циліндра з клавіатури.
def input_cylinder_params():
    # Вводимо радіус і висоту циліндра, перевіряючи, чи введено коректне числове значення.
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    return Cylinder(radius, height)

# Основна частина програми.
if __name__ == "__main__":
    # Введення параметрів для об'єктів Cube та Cylinder.
    cube = input_cube_params()
    cylinder = input_cylinder_params()

    # Додаємо об'єкти до списку box_list.
    box_list.append(cube)
    box_list.append(cylinder)

    # Виводимо інформацію про об'єкти.
    print_box_info(cube)
    print_box_info(cylinder)

    # Зберігаємо інформацію у CSV-файлі.
    save_box_list(box_list, "box_data.csv")