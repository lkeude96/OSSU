# Anything below here are for testing purpose only
s = "salad water hamburger salad hamburger"


# End of testing stuff

def item_order(order):
    """
    Counts the number of each item
    :param order: string to count items from
    :return: a consolidated version of the list
    """
    unique = "salad hamburger water"
    consolidated_order = ""
    for wordIndex in range(len(unique.split())):
        word = unique.split()[wordIndex]
        if wordIndex > 0:
            consolidated_order += " "
        consolidated_order += word +":"+str(order.count(word))
    return consolidated_order
