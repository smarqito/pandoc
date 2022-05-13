def pairs(x):
    return x
def rest(x):
    return x
def reverse(x):
    return x
def first(x):
    return x
def last(x):
    return x
def rest(x):
    return x
def allbutlast(x):
    return x
def chomp(x):
    return x
def nowrap(x):
    return x
def alpha(x):
    return x
def roman(x):
    return x
def left(x):
    return x
def center(x,):
    return x
def right(x):
    return x
def allbutlast(x):
    return x

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
        'left'      : lambda n, x, value : left(n, x, value),
        'center'    : lambda n, x, value : center(n, x, value),
        'right'     : lambda n, x, y, value : right(n, x, y, value)
    }
    def __init__(self, id, args=None) -> None:
        self.id = id
        self.args = args

    def apply(self, x):
        if self.id in Pipe._pipes:
            if self.args:
                a, b, c = self.args
                if c:
                    Pipe._pipes[self.id](a,b,c,x)
                else:
                    Pipe._pipes[self.id](a,b,x)
            else:
                Pipe._pipes[self.id](x)
        else:
            print(f"Pipe \"{self.id}\" não definido")
            exit()


