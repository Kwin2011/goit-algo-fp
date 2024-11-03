import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from time import sleep

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.color = "#000000"  # Початковий темний колір
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, visited_nodes=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    
    if visited_nodes:
        for idx, node in enumerate(visited_nodes):
            node.color = generate_color(idx, len(visited_nodes))  # Оновлення кольору відповідно до порядку обходу
    
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def generate_color(index, total_nodes):
    # Градація кольорів від темного до світлого відтінку
    color_value = int(255 * index / (total_nodes - 1))
    hex_color = "#{:02x}{:02x}FF".format(color_value, color_value)  # Генеруємо градацію синього кольору
    return hex_color

def bfs(root):
    queue = [root]
    visited_nodes = []
    while queue:
        current_node = queue.pop(0)
        visited_nodes.append(current_node)
        draw_tree(root, visited_nodes)  # Відображення кожного кроку BFS
        sleep(0.5)  # Пауза для візуалізації
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

def dfs(root):
    stack = [root]
    visited_nodes = []
    while stack:
        current_node = stack.pop()
        visited_nodes.append(current_node)
        draw_tree(root, visited_nodes)  # Відображення кожного кроку DFS
        sleep(0.5)  # Пауза для візуалізації
        # Додаємо правий вузол першим, щоб лівий оброблявся першим (LIFO)
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

# Приклад дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Виконання обходу в ширину
print("Обхід в ширину (BFS):")
bfs(root)

# Виконання обходу в глибину
print("Обхід в глибину (DFS):")
dfs(root)
