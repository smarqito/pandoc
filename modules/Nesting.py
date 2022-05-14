from modules.Elem import Elem


class Nesting(Elem):
    def __init__(self, prefix, elems = [], end = None) -> None:
        super().__init__(end)
        self.prefix = prefix
        self.elems = elems
        self.spaces = len(prefix.getValue()) + 2

    def pp(self):
        self.prefix.pp()
        for elem in self.elems[:1]:
            print(' ' * 2, end=self.end)
            elem.pp()
        for elem in self.elems[1:]:
            elem.pp_nested(self.spaces)
        print("", end=self.end)

    
