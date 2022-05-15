import sys
from aux import throw_error
from modules.It.It import It

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
        if "key" == self.keywords[0]:
            if len(self.keywords) == 1:
                var = list(var.keys())[0]
            else:
                for k in self.keywords[1:]:
                    var = var[k]
        elif "value" == self.keywords[0]:
            var = " ".join(list(var.values()))
        else:
            for key in self.keywords:
                if not (var := var.get(key, None)):
                    throw_error(f"erro: {self.getKeyword()} nao existe!!", True)
        var = super().aplly_pipes(var)
        print(var, end=self.end)
    
    def pp_list(self, var, cond):
        return super().pp_list(var, cond)
    
    def pp(self):
        if self.default:
            self.default = super().aplly_pipes(self.default)
            print(self.default, end=self.end)
        else:
            throw_error(f"erro: {self.getKeyword()} nao existe!!", True)