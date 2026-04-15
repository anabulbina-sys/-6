import math

def area(a, b):
    """Площадь прямоугольника: S = a * b"""
    return a * b

def inscribed_circle_radius(a, b):
    """
    Радиус вписанной окружности прямоугольника.
    В прямоугольник можно вписать окружность, только если это квадрат (a = b).
    Для квадрата: r = a / 2
    """
    if a == b:
        return a / 2
    else:
        return None  # В прямоугольник нельзя вписать окружность

def circumscribed_circle_radius(a, b):
    """
    Радиус описанной окружности прямоугольника.
    R = √(a² + b²) / 2 (половина диагонали)
    """
    return math.sqrt(a**2 + b**2) / 2