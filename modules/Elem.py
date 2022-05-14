from abc import abstractmethod


class Elem:
    def __init__(self, end = None) -> None:
        self.setEnd(end)
        # self.end = end.getValue() if end else "" 
    
    def getEnd(self):
        return self.end
    
    def setEnd(self, end):
        if end:
            if type(end) is str:
                self.end = end
            else:
                self.end = end.getEnd()
        else:
            self.end=""

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
    def handle_pipes(self, pipes):
        pass
    