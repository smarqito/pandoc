from abc import abstractmethod


class Elem:
    def __init__(self, end = None) -> None:
        self.end = end.getValue() if end else None
    
    def getEnd(self):
        return self.end
    
    def setEnd(self, end):
        self.end = end

    @abstractmethod
    def pp(self):   pass
    @abstractmethod
    def pp_dict(self, var):
        self.pp()
    @abstractmethod
    def pp_list(self, var, cond):
        self.pp()
    def pp_nested(self, spaces):
        self.pp()
    