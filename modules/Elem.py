from abc import abstractmethod


class Elem:
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def pp(self):   pass
    @abstractmethod
    def pp_dict(self, var):
        self.pp()
    @abstractmethod
    def pp_list(self, var, cond):
        self.pp()
    