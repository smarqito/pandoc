from modules.Stmt import Stmt


class StmtIf(Stmt):
    def __init__(self, cond, elems : list = []):
        super().__init__()
        self.cond = cond
        self.body = elems

    def testCondition(self) -> bool:
        if self.cond == "True":
            return True
        return False

    def pp(self):
        if self.testCondition():
            print("begin if")
            print("condicao", self.cond)
            for elem in self.body:
                elem.pp()
            print("end if")
            return True
        return False