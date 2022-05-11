from modules.Stmt import Stmt


class ForStmt(Stmt):
    def __init__(self, var, rules, sep = None):
        super().__init__()
        self.var = var
        if rules:
            self.rules = rules
        if sep:
            self.sep = sep