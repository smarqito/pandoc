from modules.Stmt import Stmt
from modules.Var import Var


class StmtFor(Stmt):
    def __init__(self, cond : Var, elems : list = []):
        super().__init__()
        self.cond = cond
        self.elems = elems
    def handleStr(self):
        for elem in self.elems:
            elem.pp()

    def handleIt(self):
        for it in self.cond:
            for elem in self.elems:
                elem.pp(it)
   
   
    def pp(self):
        pass