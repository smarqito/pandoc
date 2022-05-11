from modules.Stmt import Stmt


class StmtIf(Stmt):
    def __init__(self, cond, elems : list = []):
        super().__init__()
        self.cond = cond
        self.elems = elems

    def pp(self):
        print("begin if")
        print("condicao", self.cond)
        for elem in self.elems:
            elem.pp()
        print("end if")