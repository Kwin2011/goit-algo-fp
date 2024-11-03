"""
Симуляція платформи для визначення рівня генетичної спорідненості користувачів
на основі результатів тесту ДНК. Для знаходження найближчих родичів використано
алгоритм Дейкстри. Кількість тестових зразків (користувачів) можна ввести вручну,
або ж програма автоматично згенерує кількість від 5 до 20.
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
import heapq
from itertools import combinations

# Функція для введення кількості ДНК-зразків (користувачів)
def get_sample_count():
    try:
        input_count = input("Введіть кількість зразків ДНК (натисніть Enter для випадкового числа між 5 і 20): ")
        if input_count.strip() == "":
            return random.randint(5, 20)
        sample_count = int(input_count)
        if 5 <= sample_count <= 20:
            return sample_count
        else:
            print("Введіть число від 5 до 20.")
            return get_sample_count()
    except ValueError:
        print("Некоректне введення. Введіть число від 5 до 20.")
        return get_sample_count()

# Функція для моделювання зв'язків між користувачами на основі генетичного тесту
def generate_genetic_connections(users):
    relationships = []
    for user_a, user_b in combinations(users, 2):
        genetic_similarity = random.randint(1, 100)  # Менше значення - ближчі родичі
        relationships.append((user_a, user_b, genetic_similarity))
    return relationships

# Створення графа, де вузли - користувачі, а ребра - родинні зв'язки
def build_genetic_graph(users, relationships):
    genetic_graph = nx.DiGraph()
    genetic_graph.add_nodes_from(users)

    for user_a, user_b, closeness in relationships:
        genetic_graph.add_edge(user_a, user_b, weight=closeness)
        genetic_graph.add_edge(user_b, user_a, weight=closeness)  # Двосторонній зв'язок
    
    return genetic_graph

# Візуалізація графа з відображенням рівня спорідненості
def display_genetic_graph(graph):
    plt.figure(figsize=(10, 10))
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color="lightblue", 
            node_size=800, font_size=10, font_weight="bold", edge_color="gray", arrows=True)
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title("Граф спорідненості користувачів")
    plt.show()

# Алгоритм Дейкстри для знаходження найближчих родичів кожного користувача
def find_closest_relatives(graph, start_user):
    min_heap = [(0, start_user)]
    shortest_distances = {user: float('inf') for user in graph.nodes}
    shortest_distances[start_user] = 0
    
    while min_heap:
        current_dist, current_user = heapq.heappop(min_heap)
        
        if current_dist > shortest_distances[current_user]:
            continue
        
        for relative in graph.neighbors(current_user):
            closeness = graph[current_user][relative]['weight']
            distance = current_dist + closeness
            
            if distance < shortest_distances[relative]:
                shortest_distances[relative] = distance
                heapq.heappush(min_heap, (distance, relative))
    
    return shortest_distances

# Отримуємо кількість зразків та імітуємо генетичні зв'язки
sample_count = get_sample_count()
user_samples = [f'User_{i}' for i in range(1, sample_count + 1)]

# Генеруємо випадкові зв'язки між зразками
genetic_relationships = generate_genetic_connections(user_samples)

# Будуємо граф з випадковими рівнями спорідненості
genetic_graph = build_genetic_graph(user_samples, genetic_relationships)

# Візуалізуємо отриманий граф
display_genetic_graph(genetic_graph)

# Знаходимо найближчих родичів для кожного користувача
closest_relatives = {}
for user in genetic_graph.nodes:
    closest_relatives[user] = find_closest_relatives(genetic_graph, user)

# Вивід результатів: найближчі родичі для кожного користувача
print("Найближчі родичі для кожного користувача (менше значення - ближчий родич):")
for user, relatives in closest_relatives.items():
    print(f"Для {user}:")
    for relative, closeness in relatives.items():
        print(f"  до {relative} - рівень спорідненості: {closeness}")
    print()
