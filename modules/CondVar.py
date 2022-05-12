from modules.Elem import Elem


class CondVar:
    def __init__(self, keyword : ..., dict):
        super().__init__()
        self.value = dict.get(keyword, False)
        self.id = keyword
    
    def nextValue(self, keyword) -> bool:
        if self.value:
            self.value = self.value.get(keyword, False)
        self.id += f'.{keyword}'