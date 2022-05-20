from modules.Elem import Elem


class Comment(Elem):
    def __init__(self, comment, flag, prefix = "", suffix = "",end=None) -> None:
        super().__init__(end)
        self.comment = comment
        self.flag = flag 
        self.prefix = prefix
        self.suffix = suffix

    def pp(self):
        if self.flag:
            print(self.prefix + self.comment + self.suffix,end = self.end if self.end else "")