# Case-study #9
# Developers: Sedelnikova P., Simonov A., Fedotova M.
#
import turtle
import math


def get_num_hexagons() -> int:
    """
    Get the number of hexagons from user input with validation.

    Returns:
        int: Number of hexagons per row (between 4 and 20)
    """
    while True:
        try:
            n = int(input("Пожалуйста, введите количество шестиугольников,
            располагаемых в ряд: "))
            if 4 <= n <= 20:
                return n
            else:
                print("Оно должно быть от 4 до 20.")
        except ValueError:
            print("Оно должно быть от 4 до 20.")


def get_color_choice() -> str:
    """
    Get color choice from user input with validation.

    Returns:
        str: Turtle color string for the selected color
    """
    valid_colors = ['красный', 'синий', 'зеленый', 'желтый',
    'оранжевый', 'пурпурный', 'розовый']
    color_map = {
        'красный': 'red',
        'синий': 'blue',
        'зеленый': 'green',
        'желтый': 'yellow',
        'оранжевый': 'orange',
        'пурпурный': 'purple',
        'розовый': 'pink'
    }

    print("Допустимые цвета заливки:")
    for color in valid_colors:
        print(color)

    while True:
        color_input = input("Пожалуйста, введите цвет: ").strip().lower()
        if color_input in valid_colors:
            return color_map[color_input]
        else:
            print(f"'{color_input}' не является верным значением.")


def draw_hexagon(x: float, y: float, side_len: float, color: str) -> None:
    """
    Draw a hexagon centered at position (x, y).

    Args:
        x: X coordinate of hexagon center
        y: Y coordinate of hexagon center
        side_len: Length of each side of the hexagon
        color: Fill color for the hexagon
    """
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()

    turtle.fillcolor(color)
    turtle.begin_fill()

    for i in range(6):
        turtle.forward(side_len)
        turtle.right(60)

    turtle.end_fill()


def main() -> None:
    """Main function to draw the hexagon pattern."""
    # Set up the turtle window.
    turtle.setup(500, 500)
    turtle.tracer(0, 0)

    screen = turtle.Screen()
    screen.tracer(0)
    turtle.hideturtle()

    # Get user input.
    print("Выбор первого цвета:")
    color1 = get_color_choice()

    print("Выбор второго цвета:")
    color2 = get_color_choice()

    n = get_num_hexagons()

    # Calculate side length to fit in window.
    side_len = min(500 / (n * math.sqrt(2.2)), 500 / (n * 1))

    # Calculate total dimensions and starting position.
    total_width = n * math.sqrt(2.6) * side_len
    total_height = n * 1.97 * side_len
    start_x = -total_width / 2 + math.sqrt(3) * side_len / 2
    start_y = total_height / 2 - 1.5 * side_len / 2

    # Draw the hexagon pattern.
    for row in range(n):
        for col in range(n):
            x = start_x + col * math.sqrt(2.2) * side_len

            if col % 2 == 0:
                y = start_y - row * 1.75 * side_len
            else:
                y = start_y - row * 1.75 * side_len - 0.85 * side_len

            if (row - col // 2) % 2 == 0:
                current_color = color1
            else:
                current_color = color2

            draw_hexagon(x, y, side_len, current_color)

        screen.update()

    # Final display.
    screen.update()
    turtle.done()


if __name__ == "__main__":
    main()
