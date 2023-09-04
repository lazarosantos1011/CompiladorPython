# Arq Logical.py
from AnalisadorLexico import Type
from CodigoIntermediario import Expr, Temp, Node, Set
expr1, expr2 = None, None

# def create_logical(tok, x1, x2):
#     super(tok, None)  # null type to start
#     expr1 = x1
#     expr2 = x2
#     type = Set.check(expr1["type"], expr2["type"])
#     if type is None:
#         Node.error("erro de tipo")

# def check_logical(p1, p2):
#     if p1 == Type.BOOL and p2 == Type.BOOL:
#         return Type.BOOL
#     else:
#         return None

# def gen_logical():
#     f = Node.newlabel()
#     a = Node.newlabel()
#     temp = Temp(type)
#     Expr.jumping(0, f)
#     Node.emit(temp["toString"]() + " = true")
#     Node.emit("goto L" + str(a))
#     Node.emitlabel(f)
#     Node.emit(temp["toString"]() + " = false")
#     Node.emitlabel(a)
#     return temp

# def to_string_logical():
#     return expr1["toString"]() + " " + op["toString"]() + " " + expr2["toString"]()
