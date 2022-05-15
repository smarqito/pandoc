from modules.It.ItVar import ItVar


class ItRange(ItVar):
    def __init__(self, default, _range, kws = [], end = None) -> None:
        self.n, self.m = _range
        super().__init__(kws, default, end)
    
    def handleDefault(self):
        super().handleDefault()
        if self.default:
            if type(self.default) is str: 
                self.default = "".join(list(self.default)[self.n : self.m + 1 if self.m else None])
            elif type(self.default) is dict:
                self.default = dict(list(self.default.items())[self.n : self.m + 1 if self.m else None])
            elif type(self.default) is int:
                self.default = "".join(list(str(self.default))[self.n : self.m + 1 if self.m else None])
            else:
                self.default = list(self.default)[self.n : self.m + 1 if self.m else None]
                 # remains iterable