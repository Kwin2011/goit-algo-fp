# Доступні продукти з вартістю і калорійністю
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Жадібний алгоритм
def greedy_algorithm(items, budget):
    # Сортування елементів за співвідношенням калорій до вартості в порядку спадання
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    total_calories = 0
    total_cost = 0
    chosen_items = []

    for item, details in sorted_items:
        if total_cost + details["cost"] <= budget:
            chosen_items.append(item)
            total_calories += details["calories"]
            total_cost += details["cost"]

    return chosen_items, total_calories, total_cost

# Алгоритм динамічного програмування
def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    # Ініціалізація таблиці для зберігання максимальних калорій для кожного бюджету
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    # Заповнення таблиці динамічного програмування
    for i in range(1, n + 1):
        item = item_names[i - 1]
        cost = items[item]["cost"]
        calories = items[item]["calories"]
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]

    # Визначення обраних елементів
    total_calories = dp[n][budget]
    chosen_items = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:  # Якщо значення змінилось, то предмет вибраний
            item = item_names[i - 1]
            chosen_items.append(item)
            b -= items[item]["cost"]

    chosen_items.reverse()  # Порядок вибору предметів
    total_cost = sum(items[item]["cost"] for item in chosen_items)
    return chosen_items, total_calories, total_cost

# Вхідний бюджет
budget = 100

# Результати жадібного алгоритму
greedy_items, greedy_calories, greedy_cost = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_items)
print("Загальна калорійність:", greedy_calories)
print("Загальна вартість:", greedy_cost)

# Результати динамічного програмування
dp_items, dp_calories, dp_cost = dynamic_programming(items, budget)
print("\nДинамічне програмування:")
print("Вибрані страви:", dp_items)
print("Загальна калорійність:", dp_calories)
print("Загальна вартість:", dp_cost)
