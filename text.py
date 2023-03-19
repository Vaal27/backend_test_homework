from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для вычисления'
                ' квадратного корня из заданного числа')


def calculate_square_root(Number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number: float):
    """Отсеиваем 0 и отрицательные числа."""
    if your_number >= 0:
        answer: float = calculate_square_root(your_number)
        print(f'Мы вычислили квадратный корень из {your_number}. '
              f'Это будет: {answer}')


print(message)
calc(25.5)
