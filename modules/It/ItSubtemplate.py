from re import *
from modules.Stmt.StmtSubtemplate import StmtSubtemplate


class ItSubtemplate(StmtSubtemplate):
    def __init__(self, filename, parser, keywords = [], end = None):
        super().__init__(filename, parser, keywords, end)


    def pp(self):
        super().pp()
        print("", end=self.end)

        