import numpy as np
import matplotlib.pyplot as plt

# Функція для отримання кількості кидків
def get_roll_count():
    while True:
        try:
            roll_count = int(input("Please enter the number of dice rolls: "))
            if roll_count > 0:
                return roll_count
            else:
                print("The number of rolls must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

# Отримуємо кількість кидків від користувача
roll_count = get_roll_count()

# Генеруємо результати кидків
first_die = np.random.randint(1, 7, roll_count)
second_die = np.random.randint(1, 7, roll_count)
totals = first_die + second_die

# Підрахунок частоти випадання кожної суми
frequency_counts = {i: 0 for i in range(2, 13)}
for total in totals:
    frequency_counts[total] += 1

# Обчислення ймовірності для кожної суми
probabilities = {k: v / roll_count for k, v in frequency_counts.items()}

# Виведення результатів у табличному форматі
print("Sum | Probability (Monte Carlo) | Theoretical Probability")
print("-------------------------------------------------------")
theoretical_probs = ["2.78%", "5.56%", "8.33%", "11.11%", "13.89%", "16.67%", "13.89%", "11.11%", "8.33%", "5.56%", "2.78%"]
for i, (sum_value, probability) in enumerate(probabilities.items(), start=2):
    print(f" {sum_value:>3}  |    {probability * 100:>5.2f}%             | {theoretical_probs[i - 2]}")

# Створення графіку
plt.figure(figsize=(10, 6))
plt.bar(probabilities.keys(), probabilities.values(), alpha=0.7, label="Monte Carlo")
plt.plot(range(2, 13), [2.78 / 100, 5.56 / 100, 8.33 / 100, 11.11 / 100, 13.89 / 100, 16.67 / 100, 13.89 / 100, 11.11 / 100, 8.33 / 100, 5.56 / 100, 2.78 / 100],
         marker='o', color='red', linestyle='--', label="Theoretical Probability")
plt.xlabel("Sum")
plt.ylabel("Probability")
plt.title("Probability of Each Sum for Two Dice Rolls (Monte Carlo Method)")
plt.legend()
plt.show()
