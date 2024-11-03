import random

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """Додає новий вузол із даними у кінець списку."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def display(self):
        """Виводить значення всіх елементів списку."""
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

    def reverse(self):
        """Реверсує порядок елементів у списку."""
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def insertion_sort(self):
        """Сортує елементи списку методом вставки."""
        sorted_list = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            sorted_list = self._insert_sorted(sorted_list, current_node)
            current_node = next_node
        self.head = sorted_list

    def _insert_sorted(self, sorted_head, node_to_insert):
        """Вставляє новий вузол у вже відсортований список."""
        if not sorted_head or node_to_insert.value < sorted_head.value:
            node_to_insert.next = sorted_head
            sorted_head = node_to_insert
        else:
            current_node = sorted_head
            while current_node.next and current_node.next.value < node_to_insert.value:
                current_node = current_node.next
            node_to_insert.next = current_node.next
            current_node.next = node_to_insert
        return sorted_head

    @staticmethod
    def merge_sorted_lists(list1, list2):
        """Об’єднує два відсортовані списки в один."""
        merged_list = LinkedList()
        node1, node2 = list1.head, list2.head

        while node1 and node2:
            if node1.value <= node2.value:
                merged_list.append(node1.value)
                node1 = node1.next
            else:
                merged_list.append(node2.value)
                node2 = node2.next

        while node1:
            merged_list.append(node1.value)
            node1 = node1.next

        while node2:
            merged_list.append(node2.value)
            node2 = node2.next

        return merged_list

# Генеруємо список із 10 унікальними випадковими числами в діапазоні 1-100
linked_list = LinkedList()
unique_values = random.sample(range(1, 101), 10)

for value in unique_values:
    linked_list.append(value)

print("Initial list:")
linked_list.display()

# Реверсуємо список
linked_list.reverse()
print("\nList after reversing:")
linked_list.display()

# Сортуємо список
linked_list.insertion_sort()
print("\nList after sorting:")
linked_list.display()