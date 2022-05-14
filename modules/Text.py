from re import *
from modules.Elem import Elem



class Text(Elem):
    _texto = ""
    def __init__(self, texto, end = None):
        super().__init__(end)
        self._text = texto
    
    def getValue(self):
        return self._text

    def pp(self):
        print(self._text, end = self.end if self.end else "")

    def pp_nested(self, spaces):
        sub(r"(\n)", rf"$1{' ' * spaces}", self._texto)
        return super().pp_nested(spaces)