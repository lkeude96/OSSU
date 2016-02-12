import math


def polysum(n, s):
    """
    This function should sum the area and square of the perimeter of the regular polygon.
    The function returns the sum, rounded to 4 decimal places.

    :param n: number of sides
    :param s: length of each side
    :return: sum of the area and square of the perimeter of the polygon
    """
    area = (0.25 * n * math.pow(s, 2)) / (math.tan(math.pi / n))
    squared_perimeter = math.pow(n * s, 2)

    ans = area + squared_perimeter

    return round(ans, 4)
