from modules.Elem import Elem


class It(Elem):
    def __init__(self, default = None, end = None) -> None:
        super().__init__(end)
        self.default = default

    def pp_dict(self, var):
        var = super().aplly_pipes(var)
        print(var, end=self.end)
    
    def pp_list(self, var, cond):
        var = super().aplly_pipes(var)
        print(var, end=self.end)

    def pp(self):
        if self.default:
            print(self.default, end=self.end)