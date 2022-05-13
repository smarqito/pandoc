class Pipes:
    '''
        Define application of pipes on text
    '''
    def __init__(self, pipes = []) -> None:
        self.pipes = pipes
        self.handlePipes()
        
    def handlePipes(self, value):
        for pipe in self.pipes:
            value = pipe.apply(pipe)
        return value
