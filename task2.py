import os
import warnings
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
from colorama import init, Fore
import time

# Ініціалізація colorama для кольорового виведення на екран
init(autoreset=True)

# Функція для очищення екрану перед виконанням програми
def clear_screen():
    if os.name == 'nt':  # Для Windows
        os.system('cls')
    else:  # Для Linux або macOS
        os.system('clear')

# Подавлення попереджень від PuLP, щоб уникнути зайвих повідомлень
warnings.filterwarnings('ignore', category=UserWarning, message="Spaces are not permitted in the name")

# Очистка екрану при запуску програми
clear_screen()

# Опис задачі з візуалізацією
print(Fore.GREEN + "Задача: Обчислення визначеного інтеграла методом Монте-Карло")
print(Fore.YELLOW + "\nУмови:")
print(Fore.WHITE + "Ця програма обчислює значення визначеного інтегралу для обраної функції методом Монте-Карло.")
print("Метод Монте-Карло використовує випадкові точки для оцінки площі під графіком функції.")
print("Ми також порівняємо результат, отриманий методом Монте-Карло, з точним значенням інтегралу, обчисленим за допомогою функції quad.")
print("\nОсновні етапи виконання:")
print("1. Обчислення значення інтегралу методом Монте-Карло.")
print("2. Перевірка точності результатів шляхом порівняння з точним значенням інтеграла.")
print("3. Візуалізація результатів та графік функції.")
print("4. Порівняння точності та часу виконання різних методів.")
print("\nМета задачі: перевірити точність методу Монте-Карло та оцінити його ефективність для чисельного інтегрування.")

# Функція для обчислення інтегралу за допомогою методу Монте-Карло
def monte_carlo_integral(func, a, b, num_samples=10000):
    """
    Обчислення інтегралу методом Монте-Карло.
    
    :param func: функція для інтегрування
    :param a: нижня межа інтегрування
    :param b: верхня межа інтегрування
    :param num_samples: кількість випадкових точок
    :return: наближене значення інтегралу
    """
    # Генерація випадкових точок у межах [a, b]
    x_random = np.random.uniform(a, b, num_samples)  # Рандомні точки по осі x
    y_random = np.random.uniform(0, max(func(x_random)), num_samples)  # Рандомні точки по осі y
    
    # Підрахунок кількості точок, які знаходяться під графіком функції
    under_curve = np.sum(y_random <= func(x_random))  # Підраховуємо, скільки точок потрапляє під графік
    
    # Обчислення площі під графіком як площі прямокутника * частка точок під графіком
    area = (b - a) * max(func(x_random)) * under_curve / num_samples
    return area

# Функція для обчислення точного значення інтегралу за допомогою функції quad з бібліотеки scipy
def exact_integral(func, a, b):
    """
    Обчислення точного значення інтегралу за допомогою функції quad.
    
    :param func: функція для інтегрування
    :param a: нижня межа інтегрування
    :param b: верхня межа інтегрування
    :return: точне значення інтегралу
    """
    result, _ = quad(func, a, b)  # Використовуємо функцію quad для обчислення точного інтегралу
    return result

# Функція, для якої обчислюється інтеграл (наприклад, x^2)
def func(x):
    """
    Функція для інтегрування: x^2
    
    :param x: значення змінної x
    :return: значення функції x^2
    """
    return x**2

# Параметри інтеграції
a = 0  # Нижня межа інтегрування
b = 2  # Верхня межа інтегрування
num_samples = 10000  # Кількість випадкових точок для методу Монте-Карло

# Час виконання методу Монте-Карло
start_time = time.time()  # Початок вимірювання часу
monte_carlo_result = monte_carlo_integral(func, a, b, num_samples)
monte_carlo_time = time.time() - start_time  # Час виконання методу Монте-Карло

# Час виконання точного інтегралу за допомогою quad
start_time = time.time()  # Початок вимірювання часу для точного інтегралу
num_runs = 1000  # Кількість прогонів для вимірювання стабільності часу
for _ in range(num_runs):
    exact_result = exact_integral(func, a, b)
quad_time = (time.time() - start_time) / num_runs  # Середній час на один прогін для точного інтегралу

# Виведення результатів
print(f"\nРезультат методу Монте-Карло: {monte_carlo_result:.6f}")
print(f"Точне значення інтегралу (функція quad): {exact_result:.6f}")
print(f"Абсолютна похибка: {abs(monte_carlo_result - exact_result):.6f}")

# Відсоток похибки
percentage_error = (abs(monte_carlo_result - exact_result) / exact_result) * 100
print(f"Відсоток похибки: {percentage_error:.6f}%")

# Висновки:
print("\nВисновки:")
print("1. Метод Монте-Карло дав наближене значення інтегралу.")
print(f"2. Точне значення інтегралу з використанням quad: {exact_result:.6f}.")
print("3. Абсолютна похибка між результатами: ", abs(monte_carlo_result - exact_result))
print(f"4. Відсоток похибки: {percentage_error:.6f}%")
print(f"5. Час виконання методу Монте-Карло: {monte_carlo_time:.6f} секунд")
print(f"6. Час виконання точного інтегралу (quad): {quad_time:.6f} секунд")
print("7. В результаті порівняльного аналізу можна оцінити точність методу Монте-Карло в цій задачі.")
print("8. Визначено, що метод Монте-Карло є ефективним для чисельного інтегрування, хоча точність залежить від кількості випадкових точок.\n")

# Псевдографіка для показу кількості точок
def print_bar(label, used, total):
    """
    Функція для виведення псевдографіки, що показує, скільки точок використано в методі Монте-Карло.
    
    :param label: Назва параметра (наприклад, "Випадкові точки")
    :param used: Кількість використаних точок
    :param total: Загальна кількість точок
    """
    bar_used = int(used / total * 50)  # Розмір бару для використаних точок
    bar_remaining = 50 - bar_used      # Розмір бару для залишкових точок
    print(f"{label}:")
    print(Fore.BLUE + '|' + '█' * bar_used + ' ' * bar_remaining + '|', f"({used}/{total} використано)")
    print(Fore.RED + '|' + ' ' * bar_used + '█' * bar_remaining + '|', f"({total-used}/{total} залишилось)\n")

# Використання псевдографіки для випадкових точок
print_bar("Випадкові точки", num_samples, num_samples)

# Візуалізація
x_values = np.linspace(a, b, 1000)
y_values = func(x_values)

# Випадкові точки для Монте-Карло
x_random = np.random.uniform(a, b, num_samples)
y_random = np.random.uniform(0, max(y_values), num_samples)

# Побудова графіку функції та випадкових точок
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label="f(x) = x^2", color='blue')
plt.scatter(x_random, y_random, color='red', s=1, label="Випадкові точки")
plt.fill_between(x_values, 0, y_values, alpha=0.3, color='blue', label="Площа під графіком")
plt.legend()
plt.title("Метод Монте-Карло для знаходження інтегралу")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

# Аналіз похибки для різної кількості точок
points_list = [100, 1000, 10000, 100000]
errors = []
for points in points_list:
    result = monte_carlo_integral(func, a, b, points)
    error = abs(result - exact_integral(func, a, b))
    errors.append(error)

# Побудова графіку похибки для різних кількостей точок
plt.plot(points_list, errors, marker='o')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Кількість точок (log scale)')
plt.ylabel('Похибка (log scale)')
plt.title('Порівняння похибки для різних кількостей точок')
plt.show()

# Статистичний аналіз похибки
errors = []
for i in range(100):
    monte_carlo_result = monte_carlo_integral(func, a, b, num_samples)
    error = abs(monte_carlo_result - exact_result)
    errors.append(error)

# Обчислення середнього та стандартного відхилення похибки
mean_error = np.mean(errors)
std_dev_error = np.std(errors)

# Виведення статистики похибки
print(f"Середня похибка: {mean_error:.6f}")
print(f"Стандартне відхилення похибки: {std_dev_error:.6f}")

# Завершення програми
print("\nПрограма завершена.")
