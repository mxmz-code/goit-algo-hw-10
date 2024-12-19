import os
import warnings
from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD
import matplotlib.pyplot as plt
from colorama import init, Fore, Back

# Ініціалізація colorama для кольорового виведення на екран
init(autoreset=True)

# Функція для очищення екрану перед виконанням програми
def clear_screen():
    if os.name == 'nt':  # Для Windows
        os.system('cls')
    else:  # Для Linux або macOS
        os.system('clear')

# Подавлення попереджень від PuLP
warnings.filterwarnings('ignore', category=UserWarning, message="Spaces are not permitted in the name")

# Очистка екрану при запуску програми
clear_screen()

# Опис задачі з візуалізацією
print(Fore.GREEN + "Задача: Оптимізація виробництва напоїв")
print(Fore.YELLOW + "\nУмови:")
print(Fore.WHITE + "Компанія виробляє два види напоїв: Лимонад і Фруктовий сік.")
print("Для виробництва використовуються наступні інгредієнти та обмежені ресурси:")
print(Fore.WHITE + "1. Лимонад виготовляється з Води, Цукру та Лимонного соку.")
print("2. Фруктовий сік виготовляється з Фруктового пюре та Води.")
print("\nОбмеження ресурсів:")
print("1. 100 одиниць Води.")
print("2. 50 одиниць Цукру.")
print("3. 30 одиниць Лимонного соку.")
print("4. 40 одиниць Фруктового пюре.")
print("\nМета: максимізувати кількість вироблених напоїв, дотримуючись обмежень на ресурси.\n")

# Створення лінійної задачі
model = LpProblem("Оптимізація виробництва", LpMaximize)

# Створення змінних для кількості вироблених напоїв
lemonade = LpVariable('Лимонад', lowBound=0, cat='Continuous')  # кількість Лимонаду
juice = LpVariable('Фруктовий_сік', lowBound=0, cat='Continuous')  # кількість Фруктового соку

# Обмеження на ресурси
water_limit = 100  # обмеження на воду
sugar_limit = 50   # обмеження на цукор
lemon_limit = 30   # обмеження на лимонний сік
puree_limit = 40   # обмеження на фруктове пюре

# Додавання обмежень на ресурси
model += 2 * lemonade + 1 * juice <= water_limit  # Вода
model += 1 * lemonade <= sugar_limit             # Цукор
model += 1 * lemonade <= lemon_limit             # Лимонний сік
model += 2 * juice <= puree_limit                # Фруктове пюре

# Мета - максимізувати загальну кількість продуктів
model += lemonade + juice  # Загальна кількість

# Розв'язок задачі без виведення інформації про процес
model.solve(PULP_CBC_CMD(msg=False))

# Виведення результатів
print(Fore.GREEN + "\nРозв'язок задачі:")
print(Fore.CYAN + f"Кількість Лимонаду: {lemonade.varValue:.2f}")
print(Fore.CYAN + f"Кількість Фруктового соку: {juice.varValue:.2f}")
print(Fore.YELLOW + f"Загальна кількість продуктів: {lemonade.varValue + juice.varValue:.2f}")
print("\nРесурси, які залишилися:")
print(Fore.WHITE + f"Вода залишилась: {water_limit - (2 * lemonade.varValue + juice.varValue):.2f}")
print(f"Цукор залишився: {sugar_limit - lemonade.varValue:.2f}")
print(f"Лимонний сік залишився: {lemon_limit - lemonade.varValue:.2f}")
print(f"Фруктове пюре залишилось: {puree_limit - (2 * juice.varValue):.2f}")

# Псевдографіка для використаних і залишкових ресурсів
def print_bar(label, used, remaining, total):
    """
    Функція для виведення псевдографіки, що показує, скільки точок використано в методі Монте-Карло.
    
    :param label: Назва параметра (наприклад, "Вода")
    :param used: Кількість використаних точок
    :param remaining: Кількість залишкових точок
    :param total: Загальна кількість точок
    """
    bar_used = int(used / total * 50)  # Розмір бару для використаних точок
    bar_remaining = 50 - bar_used      # Розмір бару для залишкових точок
    print(f"{label}:")
    print(Fore.BLUE + '|' + '█' * bar_used + ' ' * bar_remaining + '|', f"({used}/{total} використано)")
    print(Fore.RED + '|' + ' ' * bar_used + '█' * bar_remaining + '|', f"({remaining}/{total} залишилось)\n")

# Використання псевдографіки для всіх ресурсів
print_bar("Вода", 2 * lemonade.varValue + juice.varValue, water_limit - (2 * lemonade.varValue + juice.varValue), water_limit)
print_bar("Цукор", lemonade.varValue, sugar_limit - lemonade.varValue, sugar_limit)
print_bar("Лимонний сік", lemonade.varValue, lemon_limit - lemonade.varValue, lemon_limit)
print_bar("Фруктове пюре", 2 * juice.varValue, puree_limit - (2 * juice.varValue), puree_limit)

# Візуалізація використаних ресурсів
resources_used = {
    "Вода": 2 * lemonade.varValue + juice.varValue,
    "Цукор": lemonade.varValue,
    "Лимонний сік": lemonade.varValue,
    "Фруктове пюре": 2 * juice.varValue
}

resources_remaining = {
    "Вода": water_limit - resources_used["Вода"],
    "Цукор": sugar_limit - resources_used["Цукор"],
    "Лимонний сік": lemon_limit - resources_used["Лимонний сік"],
    "Фруктове пюре": puree_limit - resources_used["Фруктове пюре"]
}

# Підготовка даних для побудови графіка
labels = list(resources_used.keys())
used = list(resources_used.values())
remaining = list(resources_remaining.values())

x = range(len(labels))

# Побудова бар-графіка для візуалізації
plt.bar(x, used, width=0.4, label='Використано', color='b', align='center')
plt.bar(x, remaining, width=0.4, label='Залишилось', color='r', align='edge')

plt.xlabel('Ресурси')
plt.ylabel('Кількість')
plt.title('Використання та залишки ресурсів')
plt.xticks(x, labels)
plt.legend()

plt.show()

# Висновки
print(Fore.GREEN + "\nВисновки:")
print(Fore.CYAN + "1. Оптимальне виробництво включає 30 одиниць Лимонаду та 20 одиниць Фруктового соку.")
print(Fore.CYAN + "2. В результаті використано 80 одиниць Води, 30 одиниць Цукру, 30 одиниць Лимонного соку та 40 одиниць Фруктового пюре.")
print(Fore.YELLOW + "3. В результаті використання обмежених ресурсів залишилось 20 одиниць Води та 20 одиниць Цукру.")
print("4. Лимонний сік та фруктове пюре повністю використано, що вказує на максимальне використання цих ресурсів.")
print(Fore.GREEN + "5. Таким чином, задача оптимізації виробництва була вирішена, і ресурси були розподілені найбільш ефективно.")
