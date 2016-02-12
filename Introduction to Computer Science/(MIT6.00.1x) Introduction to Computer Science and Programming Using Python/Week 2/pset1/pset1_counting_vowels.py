# Anything below here are for testing purpose only
s = 'azcbobobegghakl'


# End of testing stuff

def isvowel(char):
    """
    Checks if char is a vowel

    :param char: char to check if is a vowel
    :return: true if char is a vowel
    """
    return char in 'aeiou'


def countvowels(given_str):
    """
    Counts the vowels in a given string of lower case characters

    :param given_str: string to count vowels from.
    :return: number of vowels in given_str
    """
    number_of_vowels = 0

    for char in given_str:
        if isvowel(char):
            number_of_vowels += 1

    return number_of_vowels


print "Number of vowels: " + str(countvowels(s))
