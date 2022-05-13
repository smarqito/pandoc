from modules.Stmt import Stmt
from re import *

class Subtemplate(Stmt):
    def __init__(self, filename, parser):
        super().__init__()
        self.parser = parser
        self.filename = filename
        self.handleFilename()

    def handleFilename(self):
        m = search(r"(?P<fname>[^\\\/;:\"?<>|]+)(?P<ext>\.\w+)?$", self.filename)
        if m['ext']:
            self.parser.finfo['ext'] = m['ext']
        self.parser.finfo['fname'] = m['fname']

    # def changeObj(self, newObj):
    #     self.parser.yaml = newObj

    def pp_dict(self, var):
        self.parser.yaml = var
        self.pp()

    def pp(self):
        finfo = self.parser.finfo
        path = finfo['path'] + finfo['fname'] + finfo['ext']
        f = open(path, "r")
        txt = f.read()
        erro = self.parser.parse(txt)
        erro.pp()


        