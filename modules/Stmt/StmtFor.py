from modules.It.ItVar import ItVar
from modules.Stmt.Stmt import Stmt
from modules.Var import Var


class StmtFor(Stmt):
    def __init__(self, cond : Var | ItVar, elems : list = [], sep = None, end = None):
        super().__init__(end)
        self.cond = cond
        self.elems = elems
        self.sep = sep
    
    def handleStr(self):
        for elem in self.elems:
            elem.pp_dict(self.cond.getValue())

    def handleList(self):
        size = len(self.cond.getValue()) - 1
        for it in self.cond.getValue():
            for elem in self.elems:
                elem.pp_list(it, self.cond.getKeyword())

            if self.sep and size:
                print(self.sep, end=self.end)
                size -= 1

    def handleDict(self):
        size = len(self.cond.getValue()) - 1
        for it in self.cond.getValue():
            for elem in self.elems:
                elem.pp_dict(self.cond.getValue().get(it))

            if self.sep and size:
                print(self.sep, end=self.end)
                size -= 1

    def pp(self):
        if self.pipes:
            for elem in self.elems:
                elem.add_pipes(self.pipes)
        self.cond.setValue(self.cond.aplly_pipes(self.cond.getValue()))
        if self.cond.getType() is dict:
            self.handleDict()
        elif self.cond.getType() is list:
            self.handleList()
        else:
            self.handleStr()
