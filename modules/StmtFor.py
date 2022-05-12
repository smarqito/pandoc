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

    def handleList(self):
        for it in self.cond.getValue():
            for elem in self.elems:
                elem.pp_list(it, self.cond.getKeyword())

    def handleDict(self):
        for it in self.cond.getValue():
            for elem in self.elems:
                elem.pp_dict(self.cond.getValue().get(it))

    def pp(self):
        if self.cond.getType() is dict:
            self.handleDict()
        elif self.cond.getType() is list:
            self.handleList()
        else:
            self.handleStr()
