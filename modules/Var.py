from modules.Elem import Elem


class Var(Elem):
    def __init__(self, keyword : ..., dict):
        super().__init__()
        try:
            self.value = dict[keyword]
            self.id = keyword
        except:
            print(f"Variavel {keyword} nao definida")
            exit()
    
    def nextValue(self, keyword):
        try:
            self.value = self.value[keyword]
            self.id += f'.{keyword}'
        except:
            print(f"Variavel {self.value}.{keyword} nao definida")
            exit()
    
    def getValue(self) -> ...:
        return self.value
    
    def pp(self):
        print(self.value, end="")