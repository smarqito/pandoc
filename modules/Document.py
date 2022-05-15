class Document:
    def __init__(self, elems : list = []):
        self.elems = elems

    def pp(self):
        for elem in self.elems:
            elem.pp()

    def add_pipes(self, pipes):
        for elem in self.elems:
            elem.add_pipes(pipes)