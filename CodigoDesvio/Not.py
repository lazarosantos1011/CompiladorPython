# Arq Not.py
from CodigoIntermediario import Expr, Node
from AnalisadorSintatico import Parser

def create_not(tok, x2, t, f):
    if tok == "!":
        x2.jumping(f, t)
        Node.emit(f"{tok} {x2}")
