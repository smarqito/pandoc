from modules.Elem import Elem


class Entity(Elem):
    '''
    Define conversion of backslash to string
    '''
    entities = {
        '\$' : '$',
        '\div' : '<div>_</div>'
    }
    def __init__(self, entity, end = None) -> None:
        super().__init__(end)
        self.entity = entity
    
    def getValue(self) -> str:
        return Entity.entities[self.entity]

    def pp(self):
        # global entities
        print(self.getValue(), end=self.end)

    def handle_pipes(self, pipes):
        pass
    
