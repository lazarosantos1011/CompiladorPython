# Arq Rel.py
from AnalisadorSintatico import Parser
from CodigoIntermediario import Node

def create_rel(tok, x1, x2):
    expr1 = Parser.bool(x1)
    expr2 = Parser.bool(x2)

    Node.emit(f"{expr1} {tok} {expr2}")
