from modules.Elem import Elem
from re import findall, search

class Var(Elem):
    def __init__(self, keyword : ..., dict):
        super().__init__()
        self.value = dict.get(keyword, None)
        self.id = keyword
    
    def nextValue(self, keyword):
        if self.value:
            self.value = self.value.get(keyword, None)

        self.id += f'.{keyword}'
    
    def getType(self):
        return type(self.value)

    def getValue(self) -> ...:
        return self.value
    
    def getKeyword(self):
        return self.id

    def pp(self):
        if not self.value:
            print(f"erro: {self.id} nao existe!!")
            exit()
        print(self.value, end="")

    def pp_dict(self, var):
        if search(r"^it\.?", self.getKeyword()):
            f = findall(r"(?:\.(?:(\w+))+)", self.getKeyword())
        if f is not None:
            newVar = var
            for match in f:
                newVar = newVar.get(match, None)
                if not newVar:
                    print(f"erro: {self.getKeyword()} nao existe!!")
                    exit()
            print(newVar, end="")
        elif not self.value:
            print(f"erro: {self.id} nao existe!!")
            exit()
        else:
            print(self.value, end="")

    def pp_list(self, var, cond):
        if not self.value:
            print(f"erro: {self.id} nao existe!!")
            exit()
        elif self.getKeyword() == cond:
            print(var, end="")
        else:
            print(self.value, end="")