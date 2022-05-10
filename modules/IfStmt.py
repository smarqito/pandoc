from modules.Stmt import Stmt


class IfStmt(Stmt):
    def __init__(self, cond, rules = None):
        super().__init__()
        self.cond = cond
        self.rules = rules