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
