# Arq Seq.py
from CodigoIntermediario import Stmt, Node
stmt1, stmt2 = None, None
def create_seq(s1, s2):
    global stmt1, stmt2
    stmt1 = s1
    stmt2 = s2

def gen_seq(b, a):
    if stmt1 == Stmt.Null:
        stmt2.gen(b, a)
    elif stmt2 == Stmt.Null:
        stmt1.gen(b, a)
    else:
        label = Node.newlabel()
        stmt1.gen(b, label)
        Node.emitlabel(label)
        stmt2.gen(label, a)
