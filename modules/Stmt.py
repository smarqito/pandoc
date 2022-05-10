from abc import abstractmethod
from modules.Rule import Rule
class Stmt(Rule):
    def __init__(self):
        pass
    @abstractmethod
    def toHtml(self):   pass
    