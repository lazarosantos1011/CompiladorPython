# Arq Do.py
from AnalisadorLexico import Type#, newlabel
from CodigoIntermediario import Stmt, Expr

expr = None
stmt = None

def init_do(s, x):
    global expr, stmt
    expr = x
    stmt = s

    if x["type"] != Type.BOOL:
        x["error"]("booleano necessário no do")

def gen_do(b, a):
    global expr, stmt
    after = a
    label = Expr.newlabel()  # Rótulo para expr
    stmt.gen(b, label)
    Expr.emitlabel(label)
    expr.jumping(b, 0)
