from modules.Elem import Elem


class It(Elem):
    def __init__(self, default = None, end = None) -> None:
        super().__init__(end)
        self.default = default

    def pp_dict(self, var):
        print(var, end=self.end)
    
    def pp_list(self, var, cond):
        print(var, end=self.end)

    def pp(self):
        if self.default:
            print(self.default, end=self.end)