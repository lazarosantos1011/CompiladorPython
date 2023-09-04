# Arq Or.py
from AnalisadorLexico import Token
from TabelaSimbolos import Type
from AnalisadorSintatico import Parser
from CodigoIntermediario import Expr, Node
from CodigoDesvio import Logical

expr1, expr2 = None, None

def create_or(tok, x1, x2):
    if tok == "||":
        a = Parser.bool(x1)
        b = Parser.bool(x2)
        Node.emit(f"{a} || {b}")

def jumping_or(t, f):
    label = t if t != 0 else Node.newlabel()
    expr1.jumping(label, 0)
    expr2.jumping(t, f)
    if t == 0:
        Node.emitlabel(label)
