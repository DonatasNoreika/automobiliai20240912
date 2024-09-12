
from models.automobilis import Automobilis

class Elektromobilis(Automobilis):
    def __init__(self, marke, modelis, metai, talpa):
        super().__init__(marke, modelis, metai)
        self.talpa = talpa