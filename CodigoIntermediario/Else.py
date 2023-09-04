#Arq Else.py
from AnalisadorLexico import Type #,newlabel
from CodigoIntermediario import Expr


def create_else_stmt(x, s1, s2):
    if x["type"] != Type.BOOL:
        x["error"]("boolean required in if")

    label1 = Expr.newlabel()  # label1 para stmt1
    label2 = Expr.newlabel()  # label2 para stmt2
    Expr.jumping(x, 0, label2)  # fall through to stmt1 on true
    Expr.emitlabel(label1)
    Expr.gen(s1, label1, s2["a"])
    Expr.emit("goto L" + str(s2["a"]))
    Expr.emitlabel(label2)
    Expr.gen(s2, label2, s2["a"])
