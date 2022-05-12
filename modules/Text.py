from modules.Elem import Elem


class Text(Elem):
    _texto = ""
    def __init__(self, texto):
        super().__init__()
        self._text = texto
    
    def pp(self):
        print(self._text, end="")