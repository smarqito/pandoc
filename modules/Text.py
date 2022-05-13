from re import *
from modules.Elem import Elem



class Text(Elem):
    _texto = ""
    def __init__(self, texto):
        super().__init__()
        self._text = texto
    
    def pp(self):
        print(self._text, end="")

    def pp_nested(self, spaces):
        sub(r"(\n)", rf"$1{' ' * spaces}", self._texto)
        return super().pp_nested(spaces)