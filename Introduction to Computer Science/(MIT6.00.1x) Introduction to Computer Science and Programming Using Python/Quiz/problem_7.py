def f(a, b):
    return a > b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here

    tD1 = {}
    tD2 = {}

    for key in d1.keys():
        if key in d2.keys():
            tD1[key] = f(d1[key], d2[key])
        else:
            tD2[key] = d1[key]
    for key in d2.keys():
        if key not in d1.keys():
            tD2[key] = d2[key]

    return (tD1,tD2,)
