d1 = {
    0 :'',
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen'
    }

d2 = {
    2:'twenty',
    3:'thirty',
    4:'forty',
    5:'fifty',
    6:'sixty',
    7:'seventy',
    8:'eighty',
    9:'ninety'
    }

d3 = {
    1:'onehundred',
    2:'twohundred',
    3:'threehundred',
    4:'fourhundred',
    5:'fivehundred',
    6:'sixhundred',
    7:'sevenhundred',
    8:'eighthundred',
    9:'ninehundred'
    }
def GetNumbers(n):
    if n == 0:
        return ('')
    if n > 0 and n < 20:
        return ((d1[n]))
#print GetNumbers(7)
    elif n >= 20 and n < 100:
        get_word = d2[n // 10] + d1[n % 10]
        return ((get_word))
    
#print GetNumbers(77)
    elif n >= 100 and n < 1000:
        if n % 100 == 0:
            return d3[n // 100]
        else:
            required = n - (n // 100)* 100
            #print "required", required
            #ourfun = d3(n)
            #print "ourfun", ourfun
            #web = GetNumbers(required)
            #print "web", web
            return (d3[n // 100])+'and'+ (GetNumbers(required))
    elif n == 1000:
        return ('onethousand')


     
count = 0
for i in range(1,1001):
   count = count + len(GetNumbers(i))
print count


        
        
        
        
        
    
