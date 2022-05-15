from modules.Stmt.Stmt import Stmt
from re import *

class StmtSubtemplate(Stmt):
    def __init__(self, filename, parser, keywords = [], end = None, pipes = []):
        super().__init__(end)
        self.parser = parser
        self.filename = filename
        self.keywords = keywords
        self.pipes = pipes
        self.handleFilename()


    def handleFilename(self):
        
        if m := search(r"(?P<fname>[^\\\/;:\"?<>|]+)(?P<ext>\.\w+)$", self.filename):
            self.parser.finfo['ext'] = m['ext']
        else:
            m = search(r"(?P<fname>[^\\\/;:\"?<>|]+)$", self.filename)
        
        self.parser.finfo['fname'] = m['fname']

    def setObj(self, newObj):
        self.parser.yaml = newObj

    def setKeywords(self, kws):
        self.keywords = kws

    def pp_dict(self, var):
        for k in self.keywords:
            var = var[k]
        self.parser.yaml = var
        self.pp()

    def pp(self):
        finfo = self.parser.finfo
        path = finfo['path'] + finfo['fname'] + finfo['ext']
        f = open(path, "r")
        subfile = f.read()
        subtemplate = self.parser.parse(subfile)
        if self.pipes:
            subtemplate.add_pipes(self.pipes)
        subtemplate.pp()
        # print("",end=self.end)