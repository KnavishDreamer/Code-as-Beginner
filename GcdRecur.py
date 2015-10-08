def gcdRecur(a, b):
    '''(int, int) -> (int)
    Returns the positive integer which is Greatest Common Divisor of a and b.
    '''
    # Your code here
    if a == b:
        return a

    else:
        if a < b:
            return gcdRecur(a, b - a)
        elif b < a:
            return gcdRecur(a - b, b)

#print gcdRecur(13, 26)      
