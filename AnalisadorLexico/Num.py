#num.py
from Token import Token

class Num(Token):
    def __init__(self, v):
        super().__init__(tag.NUM)
        self.value = v

    def __str__(self):
        return str(self.value)