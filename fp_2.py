import turtle
import math


def draw_pythagoras_tree(t, depth, branch_length, angle=45):
    """Рекурсивно будує дерево Піфагора з використанням turtle graphics.
    
    Параметри:
    t -- об'єкт черепашки для малювання
    depth -- глибина рекурсії, визначає кількість рівнів дерева
    branch_length -- довжина поточної гілки
    angle -- кут розгалуження (за замовчуванням 45 градусів)
    """
    if depth == 0:
        # Малюємо кінцеву гілку
        t.forward(branch_length)
        t.backward(branch_length)
    else:
        # Основна гілка
        t.forward(branch_length)
        current_position = t.position()
        current_heading = t.heading()

        # Ліва гілка
        t.left(angle)
        draw_pythagoras_tree(t, depth - 1, branch_length * math.sqrt(2) / 2, angle)
        
        # Повертаємося до основи
        t.setposition(current_position)
        t.setheading(current_heading)
        
        # Права гілка
        t.right(angle)
        draw_pythagoras_tree(t, depth - 1, branch_length * math.sqrt(2) / 2, angle)
        
        # Повертаємося до основи
        t.setposition(current_position)
        t.setheading(current_heading)

def draw_tree(depth, branch_length=100):
    """Ініціалізує вікно та малює дерево Піфагора на основі вказаної глибини."""
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість малювання
    t.penup()
    t.goto(0, -window.window_height() // 3)
    t.pendown()
    t.left(90)  # Направляємо черепашку вертикально вгору

    draw_pythagoras_tree(t, depth, branch_length)

    window.mainloop()

# Отримуємо рівень рекурсії від користувача
try:
    user_input = int(input("Введіть додатнє ціле число для рівня рекурсії дерева Піфагора: "))
    if user_input < 0:
        raise ValueError("Рівень рекурсії не може бути від'ємним.")
except ValueError as error:
    print(f"Помилка: {error}")
else:
    draw_tree(user_input)
