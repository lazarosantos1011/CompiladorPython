# Arq If.py
from CodigoIntermediario import Node, Stmt, Expr
from TabelaSimbolos import Type 
expr, stmt = None, None

def create_if_stmt(x, s):
    global expr, stmt
    expr = x
    stmt = s
    if x["type"] != Type.Bool:
        x["error"]("boolean required in if")



    label = Node.newlabel()  # label for the code for stmt
    Expr.jumping(x, 0, s["a"])  # fall through on true, goto a on false
    Node.emitlabel(label)
    Stmt.gen(s, label, s["a"])
