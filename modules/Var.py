from aux import throw_error
from modules.Elem import Elem
from re import sub

class Var(Elem):
    def __init__(self, keyword : ..., dict, end = None):
        super().__init__(end)
        self.value = dict.get(keyword, None)
        self.id = keyword
        self.ids = [keyword]
        self.pipes = None
    
    def nextValue(self, keyword):
        if self.value:
            self.value = self.value.get(keyword, None)
        self.id += f'.{keyword}'
        self.ids.append(keyword)
    
    def getType(self):
        return type(self.value)

    def getValue(self) -> ...:
        return self.value

    def setValue(self, newValue):
        self.value = newValue
    
    def getKeyword(self):
        return self.id

    def getKeywords(self) -> list:
        return self.ids

    def pp(self):
        if not self.value:
            throw_error(f"erro: {self.id} nao existe!!", True)
        self.value = super().aplly_pipes(self.value)
        print(self.value, end=self.end)

    def pp_list(self, var, cond):
        if not self.value:
            throw_error(f"erro: {self.id} nao existe!!", True)
        elif self.getKeyword() == cond:
            if self.pipes:
                var = super().aplly_pipes(var)
            print(var, end=self.end)
        else:
            self.aplly_pipes()
            print(self.value, end=self.end)
    def pp_nested(self, spaces):
        if type(self.value) is str:
            self.value = super().aplly_pipes(self.value)
            self.value = sub(r"\n", rf"\n{' ' * spaces}", self.value)
        self.pp()