# Importações
from lexer import Token, Word
from symbols import Type

# Função para criar constantes
def Constant(tok, p):
    return (tok, p)

# Função para criar constantes inteiras
def IntConstant(i):
    return Constant(Num(i), Type.Int)

# Constantes estáticas
True = Constant(Word.True, Type.Bool)
False = Constant(Word.False, Type.Bool)

# Função de salto condicional
def jumping(constant, t, f):
    if constant == True and t != 0:
        emit(f"goto L{t}")
    elif constant == False and f != 0:
        emit(f"goto L{f}")
