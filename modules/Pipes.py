class Pipes:
    '''
        Define application of pipes on text
    '''
    def __init__(self, pipes = []) -> None:
        self.pipes = pipes
        
    def handlePipes(self, value):
        for pipe in self.pipes:
            value = pipe.apply(value)
        return value
    
    def addPipe(self, pipe):
        self.pipes.append(pipe)
    
    def addPipes(self, pipes):
        '''@param pipes Pipes'''
        for pipe in pipes.pipes:
            self.addPipe(pipe)