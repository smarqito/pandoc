from modules.Elem import Elem


class Texto(Elem):
    _texto = ""
    def __init__(self, texto):
        super().__init__()
        self._texto = texto
    
    def pp(self):
        print(self._texto, end="")