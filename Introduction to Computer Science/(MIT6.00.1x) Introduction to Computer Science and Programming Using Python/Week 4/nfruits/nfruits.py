def nfruits(initial_quantities, fruit_eaten):
    """

    Determine the maximum quantity out of the different types of fruits that is present with Python
    when he has reached the campus

    :param initial_quantities: non-empty dictionary containing type of fruit and its quantity initially
    :param fruit_eaten: string pattern of the fruits eaten
    :return:  maximum of the quantities of the fruits
    """
    for current_fruit in range(len(fruit_eaten)):
        for fruit in initial_quantities.keys():
            if fruit_eaten[current_fruit] == fruit:
                initial_quantities[fruit] -= 1
            elif current_fruit != len(fruit_eaten) - 1:
                initial_quantities[fruit] += 1

    max_quantity = 0;
    for fruit in initial_quantities.keys():
        if initial_quantities[fruit] > max_quantity:
            max_quantity = initial_quantities[fruit]

    return max_quantity
