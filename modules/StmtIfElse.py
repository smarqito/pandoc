from modules.StmtIf import StmtIf
from modules.Var import Var


class StmtIfElse(StmtIf):
    def __init__(self, cond : Var, elems=[], elseifs=[], elseElems=[]):
        super().__init__(cond, elems)
        self.elseifs = elseifs
        self.elseBody = elseElems

    def pp(self):
        print("begin ifelse")
        f = False
        f = super().pp()
        if not f:
            for elseif in self.elseifs:
                if f := elseif.pp():
                    break
        if not f:
            for elseElem in self.elseBody:
                elseElem.pp()
        print("end ifelse")