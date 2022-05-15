from modules.Elem import Elem


class Range(Elem):
    def __init__(self, start, stop, step = 1, end=None) -> None:
        super().__init__(end)
        self.start = start
        self.stop = stop
        self.step = step
        self.value = list(range(start, stop, step))

    def getValue(self):
        return self.value

    def setValue(self, nValue):
        self.value = nValue

    def getType(self):
        return type(self.value)

    def getKeyword(self):
        return ""