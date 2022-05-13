from modules.Elem import Elem


class It(Elem):
    def __init__(self, default = None) -> None:
        super().__init__()
        self.default = default

    def pp_dict(self, var):
        print(var)
    
    def pp_list(self, var, cond):
        print(var)

    def pp(self):
        if self.default:
            print(self.default)