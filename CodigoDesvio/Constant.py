from AnalisadorLexico import Word, Num, Type
from CodigoIntermediario import Node

# Função para criar constantes
def Constant(tok, p):
    return (tok, p)

# Função para criar constantes inteiras
def IntConstant(i):
    return Constant(Num(i), Type.int_type)

# Constantes estáticas
true = Constant(Word.lexemes['TRUE'], Type.bool_type)
false = Constant(Word.lexemes['FALSE'], Type.bool_type)

# Função de salto condicional
def jumping(constant, t, f):
    if constant == True and t != 0:
        Node.emit(f"goto L{t}")
    elif constant == False and f != 0:
        Node.emit(f"goto L{f}")
