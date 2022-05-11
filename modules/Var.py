from modules.Elem import Elem


class Var(Elem):
    def __init__(self, varElems = []):
        super().__init__()
        self.var = varElems