from re import sub, search
from math import ceil, floor

from aux import throw_error

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
    _to_roman_ind = [1,4,5,9,10,40,50,90,100,400,500,900,1000,
                    4000, 5000, 9000, 10000, 50000, 100000, 500000, 1000000]
    _to_roman = {
        1     : 'i'  ,
        4     : 'iv' ,
        5     : 'v'  ,
        9     : 'ix' ,
        10    : 'x'  ,
        40    : 'xl' ,
        50    : 'l'  ,
        90    : 'xc' ,
        100   : 'c'  ,
        400   : 'cd' ,
        500   : 'd'  ,
        900   : 'cm' ,
        1000  : 'm'  ,
        4000  : 'mv|',
        5000  : 'v|',
        9000  : 'mx|',
        10000 : 'x|',
        50000 : 'l|',
        100000: 'c|',
        500000: 'd|',
        1000000 : 'm|'
    }
    
    pos = len(_to_roman_ind) - 1
    num = int(x[0])
    res = ""
    while num:
        while(num < _to_roman_ind[pos]):
            pos -=1
        res += _to_roman[_to_roman_ind[pos]]
        num -= _to_roman_ind[pos]
    return res

def roman(x):
    if type(x) is dict:
        tmp = {}
        for elem in x:
            tmp[elem] = roman(x[elem])
        return tmp
    elif type(x) is list:
        tmp = []
        for i in range(len(x)):
            tmp.append(roman(x[i]))
        return tmp
    elif type(x) is str or int:
        return sub(r"[1-9]\d*", handle_roman, x)
    else:
        return x

def left(value, size, left, right):
    res = ""
    total = len(value)
    ptr = 0
    round = 0
    # if left:  size -= len(left)
    # if right: size -= len(right)

    while ptr < total:
        round = 0
        if left: res += left

        while round < size and ptr < total:
            if value[ptr] == '\n':
                ptr += 1
                break
            else:
                res += value[ptr]
                ptr += 1
                round += 1
        
        if round < size: res += " " * (size - round)

        if right: res += right

        if ptr < total: res += '\n'
    return res
    
def center(x, n, l, r):
    res = ""
    while (len(x) > 0):
        if l:
            res += l

        m = search(r'\n', x)
        n_pos = n + 1 #Caso nao exista \n o n_pos não é necessário logo é smepre maior que tam_disp
        if m:
            n_pos = int(m.span()[1])
        tam_disp = n# - len(l) - len(r)

        if n_pos > tam_disp:
            length = len(x[:tam_disp])
        else:
            length = len(x[:n_pos-1])
        numSpaces = (n - length) / 2
        res += ceil(numSpaces) * " "

        if n_pos > tam_disp:
            res += x[:tam_disp]
            x = x[tam_disp:]
        else:
            res += x[:n_pos-1]
            x = x[n_pos:]
                
        res += floor(numSpaces) * " "
        if r:
            res += r
        if tam_disp < n_pos and len(x) > 0:
            res += '\n'

    return res

def right(value, size, left, right):
    res = ""
    total = len(value)
    ptr = 0
    round = 0
    # if left:  size -= len(left)
    # if right: size -= len(right)
    tmp = ""
    while ptr < total:
        round = 0
        if left: res += left

        tmp = ""
        while round < size and ptr < total:
            if value[ptr] == '\n':
                ptr += 1
                break
            else:
                tmp += value[ptr]
                ptr += 1
                round += 1
        
        if round < size: res += " " * (size - round)

        res += tmp

        if right: res += right

        if ptr < total: res += '\n'
    return res

def myupper(x):
    if type(x) is dict:
        tmp = {}
        for elem in x:
            tmp[elem] = myupper(x[elem])
        return tmp
    elif type(x) is list:
        tmp = []
        for i in range(len(x)):
            tmp.append(myupper(x[i]))
        return x
    elif type(x) is str:
        return x.upper()
    else:
        return x

def mylower(x):
    if type(x) is dict:
        tmp = {}
        for elem in x:
            tmp[elem] = mylower(x[elem])
        return tmp
    elif type(x) is list:
        tmp = []
        for i in range(len(x)):
            tmp.append(mylower(x[i]))
        return tmp
    elif type(x) is str:
        return x.lower()
    else:
        return x
class Pipe:
    _pipes = {
        'pairs'     : lambda x : pairs(x),
        'uppercase' : lambda x : myupper(x),
        'lowercase' : lambda x : mylower(x),
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
                    return Pipe._pipes[self.id](x,a,b,c)
                else:
                    if self.id == 'left' or self.id == 'center':
                        return Pipe._pipes[self.id](x,a,b,"")
                    else:
                        return Pipe._pipes[self.id](x,a,"",b)
            else:
                return Pipe._pipes[self.id](x)
        else:
            throw_error(f"Pipe \"{self.id}\" não definido", True)