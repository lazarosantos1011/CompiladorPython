# Arq Access.py
import CodigoIntermediario.Expr as Expr
from AnalisadorLexico import Word, Tag
from CodigoIntermediario import Expr, Temp, Node
from TabelaSimbolos import Array

array, index = None, None

def create_access(a, i, p):
    # super(Word("[]", Tag.INDEX), p)  # p is element type after flattening the array
    global array, index
    array = a
    index = i
    gen_access()

def gen_access():
    global array, index
    size = Array.array_size(array)

    t1 = Temp.create_temp()
    t2 = Temp.create_temp()
    Node.emit(f"\tt{t1} = {index} * {size}\n\tt{t2} = {array} [t{t2}]")
    # return Access(array, index["reduce"](), type)
