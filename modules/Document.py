class Document:
    def __init__(self, elems : list = []):
        self.elems = elems

    def pp(self, dict):
        for elem in self.elems:
            elem.pp()