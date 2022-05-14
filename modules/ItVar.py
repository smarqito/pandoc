from modules.It import It

class ItVar(It):
    def __init__(self, kws, default, end = None) -> None:
        super().__init__(default, end)
        self.keywords = kws
        self.handleDefault()
    
    def handleDefault(self):
        if self.default:
            var = self.default
            for key in self.keywords:
                if not (var := var.get(key, None)):
                    break
            self.default = var

    def pp_dict(self, var):
        for key in self.keywords:
            if not (var := var.get(key, None)):
                print(f"erro: {self.getKeyword()} nao existe!!")
                exit()
        print(var, end="")
    
    def pp_list(self, var, cond):
        return super().pp_list(var, cond)
    
    def pp(self):
        if self.default:
            print(self.default, end="")
        else:
            print(f"erro: {self.getKeyword()} nao existe!!")
            exit()