from modules.Elem import Elem
from re import findall, search

class Var(Elem):
    def __init__(self, keyword : ..., dict):
        super().__init__()
        if type(dict) is not str:
            self.value = dict.get(keyword, None)
        else:
            self.value = dict
        self.id = keyword
        self.ids = [keyword]
    
    def nextValue(self, keyword):
        if self.value:
            self.value = self.value.get(keyword, None)

        self.id += f'.{keyword}'
        self.ids.append(keyword)
    
    def getType(self):
        return type(self.value)

    def getValue(self) -> ...:
        return self.value
    
    def getKeyword(self):
        return self.id

    def getKeywords(self) -> list:
        return self.ids

    def pp(self):
        if not self.value:
            print(f"erro: {self.id} nao existe!!")
            exit()
        print(self.value, end="")

    def pp_dict(self, var):
        kws = self.getKeywords()

        if kws[0] == 'it':
            newVar = var
            for match in kws[1:]:
                if not (newVar := newVar.get(match, None)):
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