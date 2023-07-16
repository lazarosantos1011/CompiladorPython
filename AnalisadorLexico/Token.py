#Token.py

class Token:
    def __init__(self, t):
        self.tag = t
    def __str__(self):
        return str(chr(self.tag))