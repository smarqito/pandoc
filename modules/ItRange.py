from modules.ItVar import ItVar


class ItRange(ItVar):
    def __init__(self, default, _range, kws = [], end = None) -> None:
        self.n, self.m = _range
        super().__init__(kws, default, end)
    
    def handleDefault(self):
        super().handleDefault()
        if self.default:
            self.default = "".join(list(self.default)[self.n : self.m + 1 if self.m else None])