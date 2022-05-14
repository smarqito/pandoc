from re import sub
from math import ceil, floor

def pairs(x):
    res = []
    if type(x) is list:
        ind = 1
        for elem in x:
            res.append({ ind : elem})
            ind += 1 
    elif type(x) is dict:
         for key in x:
            value = x[key]
            if type(value) is dict:
                value = pairs(x[key])
            res.append({key : value})
    return res
    
def reverse(x):
    return x[::-1]
def first(x):
    return x[0]
def last(x):
    return x[-1]
def rest(x):
    return x[1:]
def allbutlast(x):
    return x[:-1]
def chomp(x):
    return sub(r"\n+", "\n", x)
def nowrap(x):
    return x
def alpha(x):
    return sub(r"(2[0-6]|1\d|[1-9])", lambda m : chr(96+int(m[0])), x)

def handle_roman(x) -> str:
    _to_roman_ind = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    _to_roman = {
        1     : 'I'  ,
        4     : 'IV' ,
        5     : 'V'  ,
        9     : 'IX' ,
        10    : 'X'  ,
        40    : 'XL' ,
        50    : 'L'  ,
        90    : 'XC' ,
        100   : 'C'  ,
        400   : 'CD' ,
        500   : 'D'  ,
        900   : 'CM' ,
        1000  : 'M'  
    }
    
    pos = 12
    num = int(x)
    res = ""
    while num:
        while(num < _to_roman_ind[pos]):
            pos -=1
        res += _to_roman[pos]
        num -= _to_roman_ind[pos]
    return res

def roman(x):
    return sub(r"\d+", handle_roman, x)        

def left(x, n, l, r):
    res = ""
    tam = 0
    if l:
        res += l
        tam += len(l)
    res += x
    tam += len(x)
    if r:
        res += (n-tam-len(r)) * " "
        res += r
    else: 
        res += (n-tam) * " "
    return res
    
def center(x, n, l, r):
    res = ""
    tam = 0
    if l:
        res += l
        tam += len(l)
    if r:
        numSpaces = (n - tam - len(x) - len(r)) / 2
        res += ceil(numSpaces) * " "
        res += x
        res += floor(numSpaces) * " "
        res += r
    else:
        numSpaces = (n - tam - len(x)) / 2
        res += ceil(numSpaces) * " "
        res += x
        res += floor(numSpaces) * " "
    return res

def right(x, n, l, r):
    res = ""
    tam = 0
    if l:
        res += l
        tam += len(l)
    if r:
        res += (n-tam-len(r)) * " "
        res += x
        res += r
    else:
        res += (n-tam) * " "
        res += x
    return res


class Pipe:
    _pipes = {
        'pairs'     : lambda x : pairs(x),
        'uppercase' : lambda x : x.upper(),
        'lowercase' : lambda x : x.lower(),
        'length'    : lambda x : len(x),
        'reverse'   : lambda x : reverse(x),
        'first'     : lambda x : first(x),
        'last'      : lambda x : last(x),
        'rest'      : lambda x : rest(x),
        'allbutlast': lambda x : allbutlast(x),
        'chomp'     : lambda x : chomp(x),
        'nowrap'    : lambda x : nowrap(x),
        'alpha'     : lambda x : alpha(x),
        'roman'     : lambda x : roman(x),
        'left'      : lambda x, n, l, r : left(x, n, l, r),
        'center'    : lambda x, n, l, r : center(x, n, l, r),
        'right'     : lambda x, n, l, r : right(x, n, l, r)
    }
    def __init__(self, id, args=None) -> None:
        self.id = id
        self.args = args

    def apply(self, x):
        if self.id in Pipe._pipes:
            if self.args:
                a, b, c = self.args
                if c:
                    return Pipe._pipes[self.id](a,b,c,x)
                else:
                    return Pipe._pipes[self.id](a,b,x)
            else:
                return Pipe._pipes[self.id](x)
        else:
            print(f"Pipe \"{self.id}\" não definido")
            exit()


