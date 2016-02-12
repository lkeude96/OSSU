# Anything below here are for testing purpose only
s = 'azcbobobegghakl'


# End of testing stuff

def countbobs(given_str):
    """
    Counts the number of times 'bob' occurs in a given string

    :param given_str: string to count 'bob' from
    :return: number of times 'bob' occurs in given_str
    """
    number_of_bobs = 0

    for char_index in range(len(given_str)):
        if given_str[char_index: char_index+3] == 'bob':
            number_of_bobs += 1
    return number_of_bobs

print "Number of times bob occurs is:  " + str(countbobs(s))
