from modules.Stmt import Stmt


class IfStmt(Stmt):
    def __init__(self, cond, rules = None, _elseif = None, _else = None):
        super().__init__()
        self.cond = cond
        if rules:
            self.rules = rules
        if _elseif:
            self._elseif = _elseif
        if _else:
            self._else = _else
        