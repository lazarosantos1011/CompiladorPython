# Arq Set.py
from TabelaSimbolos import Type
from CodigoIntermediario import Node

expr = None


def create_set_stmt(i, x):
    global expr
    id = i
    expr = x

    if check(id["type"], expr["type"]) is None:
        Node.error("erro de tipo")

def check(p1, p2):
    if Type.numeric(p1) and Type.numeric(p2):
        return p2
    elif p1 == Type.Bool and p2 == Type.BOOL:
        return p2
    else:
        return None

def gen_set(b, a):
    global expr
    Node.emit(id["toString"]() + " = " + expr["gen"]()["toString"]())
