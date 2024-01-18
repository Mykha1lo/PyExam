import numpy as np
import statistics

class StatisticalCalculator:
    def __init__(self):
        # Конструктор класу, ініціалізує порожній список для зберігання введених даних.
        self.data = []

    def input_data(self):
        try:
            # Метод для введення даних користувачем. Запитує користувача ввести ряд чисел, розділених пробілами, та зберігає їх у вигляді списку чисел.
            data_str = input("Введіть набір чисел, розділених пробілами: ")
            self.data = [float(x) for x in data_str.split()]
        except ValueError:
            # Обробка помилок при некоректному вводі (наприклад, введення нечислових значень).
            print("Некоректний ввід. Будь ласка, введіть числові значення.")

    def calculate_mean(self):
        # Метод для обчислення середнього значення чисел у введеному наборі.
        if not self.data:
            return None
        return np.mean(self.data)

    def calculate_median(self):
        # Метод для обчислення медіани чисел у введеному наборі.
        if not self.data:
            return None
        return np.median(self.data)

    def calculate_std_deviation(self):
        # Метод для обчислення стандартного відхилення чисел у введеному наборі.
        if not self.data:
            return None
        return np.std(self.data)

    def calculate_min_value(self):
        # Метод для знаходження мінімального значення у введеному наборі.
        if not self.data:
            return None
        return min(self.data)

    def calculate_max_value(self):
        # Метод для знаходження максимального значення у введеному наборі.
        if not self.data:
            return None
        return max(self.data)

    def perform_statistical_analysis(self):
        # Метод, який викликається для виконання всього статистичного аналізу.
        self.input_data()

        mean = self.calculate_mean()
        median = self.calculate_median()
        std_deviation = self.calculate_std_deviation()
        min_value = self.calculate_min_value()
        max_value = self.calculate_max_value()

        # Виведення результатів статистичного аналізу.
        print(f"Середнє значення: {mean}")
        print(f"Медіана: {median}")
        print(f"Стандартне відхилення: {std_deviation}")
        print(f"Мінімальне значення: {min_value}")
        print(f"Максимальне значення: {max_value}")

# Приклад використання:
calculator = StatisticalCalculator()
calculator.perform_statistical_analysis()
