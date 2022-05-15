from re import sub, search
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
        1000  : 'm'  
    }
    
    pos = 12
    num = int(x[0])
    print("numero",num)
    res = ""
    while num:
        while(num < _to_roman_ind[pos]):
            pos -=1
        res += _to_roman[_to_roman_ind[pos]]
        num -= _to_roman_ind[pos]
    return res

def roman(x):
    return sub(r"[1-9]\d*", handle_roman, x)        

def left(x, n, l, r):
    res = ""
    tam = 0
    while (len(x) > 0):
        tam = 0
        if l:
            res += l
            tam += len(l)

        m = search(r'\n', x)
        n_pos = n + 1 #Caso nao exista \n o n_pos não é necessário logo é smepre maior que tam_disp
        if m:
            n_pos = int(m.span()[1])
        tam_disp = n - len(l) - len(r)

        if n_pos > tam_disp:
            res += x[:tam_disp]
            tam += len(x[:tam_disp])
            x = x[tam_disp:]
        else:
            res += x[:n_pos-1]
            tam += len(x[:n_pos-1])
            x = x[n_pos:]
        if r:
            if len(x) == 0:
                res += (n-tam-len(r)) * " "
            elif n_pos < tam_disp:
                res += (tam_disp - n_pos + 1) * " "
            res += r
        if tam_disp < n_pos and len(x) > 0:
            res += '\n'
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
        tam_disp = n - len(l) - len(r)

        if n_pos > tam_disp:
            length = len(x[:tam_disp])
        else:
            length = len(x[:n_pos-1])
        numSpaces = (n - len(l) - length - len(r)) / 2
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

def right(x, n, l, r):
    res = ""
    while(len(x) > 0):
        if l:
            res += l

        m = search(r'\n', x)
        n_pos = n + 1 #Caso nao exista \n o n_pos não é necessário logo é smepre maior que tam_disp
        if m:
            n_pos = int(m.span()[1])
        tam_disp = n - len(l) - len(r)

        if n_pos > tam_disp:
            length = len(x[:tam_disp])
        else:
            length = len(x[:n_pos-1])

        res += (n-length- len(l) -len(r)) * " "

        if n_pos > tam_disp:
            res += x[:tam_disp]
            x = x[tam_disp:]
        else:
            res += x[:n_pos-1]
            x = x[n_pos:]

        if r:
            res += r
        if tam_disp < n_pos:
            res += '\n'
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
                    return Pipe._pipes[self.id](x,a,b,c)
                else:
                    if self.id == 'left' or self.id == 'center':
                        return Pipe._pipes[self.id](x,a,b,"")
                    else:
                        return Pipe._pipes[self.id](x,a,"",b)
            else:
                return Pipe._pipes[self.id](x)
        else:
            print(f"Pipe \"{self.id}\" não definido")
            exit()


