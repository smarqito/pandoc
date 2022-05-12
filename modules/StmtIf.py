from modules.Stmt import Stmt
from modules.Var import Var


class StmtIf(Stmt):
    def __init__(self, cond : Var, elems : list = []):
        super().__init__()
        self.cond = cond
        self.body = elems

    def testCondition(self) -> bool:
        return self.cond.getValue()

    def pp(self):
        if self.testCondition():
            print("begin if")
            print("condicao", self.cond.getValue())
            for elem in self.body:
                elem.pp()
            print("end if")
            return True
        return False