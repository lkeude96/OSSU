def ndigits(x):
    """
    Counts the number of digits in x

    :param x: positive or negative integer to count digits from
    :return: number of digits in x
    """
    if abs(x) < 10:
        return 1

    return 1 + ndigits(abs(x)/10)
