def romanToInt(s:str)->int:
    res=0
    roman={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    for a,b in zip(s,s[1:]):

        if roman[a]<roman[b]:
            res-=roman[a]
        else:
            res+=roman[a]

    return res+roman[s[-1]]

print(romanToInt('III'))
print(romanToInt('MCDIV'))


def IntToRoman(num:int)->str:

    count=0
    value_symbol=[(1000, 'M'),(900, 'CM'),(500, 'D'),(400, 'CD'),(100, 'C'),(50, 'L'),(40, 'XL'),(10, 'X'),
                  (9, 'IX'),(5, 'V'),(4, 'IV'),(1, 'I')]
    res=[]

    for value, symbol in value_symbol:
        count=num//value
        res.append(symbol*count)
        num-=value*count

    return ''.join(res)

print(IntToRoman(3))
print(IntToRoman(1404))
print(IntToRoman(1994))
