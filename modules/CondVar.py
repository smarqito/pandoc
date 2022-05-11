from modules.Elem import Elem


class CondVar(Elem):
    def __init__(self, keyword : ..., dict):
        super().__init__()
        self.value = dict.get(keyword, False)
        self.id = keyword
    
    def nextValue(self, keyword) -> bool:
        if self.value:
            self.value = self.value.get(keyword, False)
        self.id += f'.{keyword}'
    
    def getValue(self) -> ...:
        return self.value
    
    def pp(self):
        print(self.value, end="")