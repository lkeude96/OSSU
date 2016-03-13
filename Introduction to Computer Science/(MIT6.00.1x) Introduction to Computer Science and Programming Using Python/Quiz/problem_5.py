def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    sum = 0
    for i in range(len(listA)):
        sum += listA[i] * listB[i]

    return sum
