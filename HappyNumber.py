def SumOfDigits(num):
    num = str(num)
    count = 0
    for items in num:
        count = count + int(items) ** 2
    return count

def IsHappy(num):
    newnum = set()
    while num not in newnum:
        newnum.add(num)
        if SumOfDigits(num) == 1:
            return True
        else:
            num = SumOfDigits(num)
          
    return False


print IsHappy(91)
