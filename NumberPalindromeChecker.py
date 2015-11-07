
def NumberPalin(num):
    temp = num
    rev = 0
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    return  rev == temp

print NumberPalin(10101)
