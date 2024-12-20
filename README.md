
# Домашнє завдання до теми "Лінійне програмування та рандомізовані алгоритми" (goit-algo-hw-10)

Цей репозитарій містить два Python-скрипти, які виконують розв'язок задач, пов'язаних із лінійним програмуванням і рандомізованими алгоритмами:

- **Завдання 1:** Оптимізація виробництва напоїв методом лінійного програмування.
- **Завдання 2:** Обчислення визначеного інтегралу методом Монте-Карло.

Репозитарій доступний за посиланням: [goit-algo-hw-10](https://github.com/mxmz-code/goit-algo-hw-10)

## Зміст

1. [Залежності](#залежності)
2. [Завдання 1: Оптимізація виробництва напоїв](#завдання-1-оптимізація-виробництва-напоїв)
3. [Завдання 2: Обчислення визначеного інтегралу методом Монте-Карло](#завдання-2-обчислення-визначеного-інтегралу-методом-монте-карло)
4. [Як запустити скрипти](#як-запустити-скрипти)
5. [Висновки](#висновки)

---

## Залежності

Для запуску скриптів потрібно встановити наступні бібліотеки:

1. **PuLP** — бібліотека для лінійного програмування.
   ```bash
   pip install pulp
   ```
2. **SciPy** — бібліотека для чисельних методів і точного обчислення інтегралів.
   ```bash
   pip install scipy
   ```
3. **NumPy** — бібліотека для роботи з масивами та математичними функціями.
   ```bash
   pip install numpy
   ```
4. **Matplotlib** — бібліотека для візуалізації даних (графіків).
   ```bash
   pip install matplotlib
   ```
5. **colorama** — бібліотека для кольорового виведення в термінал.
   ```bash
   pip install colorama
   ```

---

## Завдання 1: Оптимізація виробництва напоїв

### Логіка задачі:

У цій задачі розглядається оптимізація виробництва двох видів напоїв: **Лимонаду** та **Фруктового соку**. Для цього використовуються ресурси:
- Вода
- Цукор
- Лимонний сік
- Фруктове пюре

Мета — максимізувати кількість вироблених напоїв при обмежених ресурсах. Для цього був застосований метод лінійного програмування за допомогою бібліотеки **PuLP**, яка дозволяє розв'язувати задачі лінійного програмування.

### Кроки розв'язку:

1. **Опис функції та обмежень:**
   - Лимонад виготовляється з води, цукру та лимонного соку.
   - Фруктовий сік виготовляється з фруктового пюре та води.
   - Обмеження на ресурси:
     - 100 одиниць води
     - 50 одиниць цукру
     - 30 одиниць лимонного соку
     - 40 одиниць фруктового пюре
     
2. **Реалізація лінійної задачі:**
   - Задача формулюється як задача лінійного програмування, де ми максимізуємо кількість вироблених напоїв за умови обмеження на ресурси.
   - Моделювання задачі відбувається через визначення змінних для кожного продукту (лимонад, фруктовий сік) та їх обмеження.

3. **Рішення задачі:**
   - Програма використовує бібліотеку **PuLP** для вирішення задачі лінійного програмування і пошуку оптимального рішення.
   - Результат: кількість кожного напою, що потрібно виготовити, та залишки ресурсів.

### Результати:
- Виготовити 30 одиниць Лимонаду та 20 одиниць Фруктового соку.
- 20 одиниць води та 20 одиниць цукру залишаються після виробництва.
- Лимонний сік і фруктове пюре повністю використано.

### Додатковий функціонал:
- **Псевдографіка:** для наочного відображення використаних і залишкових ресурсів.
- **Візуалізація:** графік, що показує використання ресурсів та площу під графіком виробництва.

---

## Завдання 2: Обчислення визначеного інтегралу методом Монте-Карло

### Логіка задачі:

У другій задачі використовується метод Монте-Карло для обчислення визначеного інтегралу функції \(f(x)\) на відрізку \([a, b]\). Цей метод полягає в тому, що випадковим чином генеруються точки в межах інтегрування, і на основі кількості точок, що потрапляють під графік функції, обчислюється площа під графіком (тобто значення інтегралу).

### Кроки розв'язку:

1. **Метод Монте-Карло:**
   - Випадкові точки генеруються у межах заданого інтервалу \([a, b]\).
   - Для кожної точки перевіряється, чи знаходиться вона під графіком функції.
   - На основі цього розраховується площа під графіком, що є наближеним значенням інтегралу.

2. **Порівняння результатів:**
   - Точне значення інтегралу порівнюється з результатом, отриманим методом Монте-Карло, через функцію **quad** з бібліотеки **SciPy**.
   - Визначається абсолютна похибка та відсоток похибки для оцінки точності методу.

3. **Візуалізація:**
   - Побудовано графік функції разом з випадковими точками, які використовуються для оцінки площі під графіком.
   - Виведено графік похибки для різної кількості точок, щоб оцінити стабільність методу Монте-Карло.

### Результати:
- Порівняння результатів Монте-Карло і точного інтегралу показало похибку близько 0.006 (відсоток похибки: 0.23%).
- Виконано аналіз похибки для різної кількості точок і порівняння з точним значенням інтегралу.

### Додатковий функціонал:
- **Псевдографіка для випадкових точок:** наочне відображення кількості точок, що потрапляють під графік.
- **Аналіз похибки для різної кількості точок:** побудова графіка, що показує, як точність змінюється при збільшенні кількості точок.
- **Статистичний аналіз:** обчислення середньої похибки та стандартного відхилення для кількох прогонів методу Монте-Карло.

---

## Як запустити скрипти

1. Клонувати репозитарій:
   ```bash
   git clone https://github.com/mxmz-code/goit-algo-hw-10.git
   cd goit-algo-hw-10
   ```

2. Встановити всі залежності:
   ```bash
   pip install -r requirements.txt
   ```

3. Запустити скрипти:
   Для першого завдання:
   ```bash
   python task1.py
   ```

   Для другого завдання:
   ```bash
   python task2.py
   ```

## Висновки

- **Завдання 1:** Метод лінійного програмування за допомогою **PuLP** ефективно вирішує задачу оптимізації виробництва, даючи точні результати та дозволяючи наочно показати залишки ресурсів.
- **Завдання 2:** Метод Монте-Карло для обчислення визначеного інтегралу є ефективним, але його точність залежить від кількості точок. Порівняння з точним значенням дає змогу оцінити ефективність цього методу.

