from abc import abstractmethod


class Elem:
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def pp(self):   pass
    @abstractmethod
    def pp(self, var): pass
    