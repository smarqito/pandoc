from abc import abstractmethod

from modules.Pipes import Pipes


class Elem:
    def __init__(self, end = None) -> None:
        self.setEnd(end)
        # self.end = end.getValue() if end else "" 
        self.pipes = None
    
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
    def set_pipes(self, pipes):
        self.pipes = pipes
    @abstractmethod
    def aplly_pipes(self, value):
        if self.pipes:
            return self.pipes.handlePipes(value)
        return value
    
    def add_pipe(self, pipe):
        if self.pipes:
            self.pipes.addPipe(pipe)
        else:
            self.pipes = Pipes([pipe])

    def add_pipes(self, pipes):
        if self.pipes:
            self.pipes.addPipes(pipes)
        else:
            self.pipes = pipes