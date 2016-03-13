def isPalindrome(aString):
    '''
    aString: a string
    '''
    # Your code here

    def isPal(aStr):
        if len(aStr) <= 1:
            return True
        return aStr[0] == aStr[-1] and isPal(aStr[1:-1])

    return isPal(aString.lower().replace(' ', ''))
