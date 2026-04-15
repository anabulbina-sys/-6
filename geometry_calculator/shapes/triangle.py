import math

def area(a, b, c):
    """Площадь треугольника по формуле Герона"""
    p = (a + b + c) / 2  # Полупериметр
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def inscribed_circle_radius(a, b, c):
    """Радиус вписанной окружности: r = S / p"""
    S = area(a, b, c)
    p = (a + b + c) / 2
    return S / p

def circumscribed_circle_radius(a, b, c):
    """Радиус описанной окружности: R = (a * b * c) / (4 * S)"""
    S = area(a, b, c)
    return (a * b * c) / (4 * S)