# Arq And.py
from CodigoIntermediario import Node, Expr
from AnalisadorSintatico import Parser

def create_and(tok, x1, x2):
    if tok == "&&":
        expr1 = Parser.bool(x1)
        expr2 = Parser.bool(x2)
        Node.emit(f"{expr1} tok {expr2}")
