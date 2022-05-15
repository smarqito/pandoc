from re import *
from modules.Elem import Elem



class Text(Elem):
    def __init__(self, texto, end = None):
        super().__init__(end)
        self._text = texto
    
    def getValue(self):
        return self._text

    def pp(self):
        self._text = super().aplly_pipes(self._text)
        print(self._text, end = self.end if self.end else "")

    def pp_nested(self, spaces):
        self._text = super().aplly_pipes(self._text)
        sub(r"(\n)", rf"$1{' ' * spaces}", self._text)
        return super().pp_nested(spaces)

        