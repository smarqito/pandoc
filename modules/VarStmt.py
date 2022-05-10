from modules.Stmt import Stmt


class VarStmt(Stmt):
    def __init__(self, var):
        super().__init__()
        self.var = var