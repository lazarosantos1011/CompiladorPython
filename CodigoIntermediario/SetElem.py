# Arq SetElem.py
from CodigoIntermediario import Id, Stmt, Expr, Node
from TabelaSimbolos import Type, Array

def create_set_elem(x, y):
    global array, index, expr
    array = x["array"]
    index = x["index"]
    expr = y

    if check(x["type"], y["type"]) is None:
        Node.error("erro de tipo")

def check(p1, p2):
    if isinstance(p1, Array) or isinstance(p2, Array):
        return None
    elif p1 == p2:
        return p2
    elif Type.numeric(p1) and Type.numeric(p2):
        return p2
    else:
        return None

def gen_set_elem(b, a):
    s1 = index["reduce"]()["toString"]()
    s2 = expr["reduce"]()["toString"]()
    Node.emit(array["toString"]() + " [ " + s1 + " ] = " + s2)
