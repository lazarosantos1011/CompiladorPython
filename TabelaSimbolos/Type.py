# Definição de constantes para tipos
from AnalisadorLexico import Word, Tag

Int = {"name": "int", "tag": 256, "width": 4}
Float = {"name": "float", "tag": 257, "width": 8}
Char = {"name": "char", "tag": 258, "width": 1}
Bool = {"name": "bool", "tag": 259, "width": 1}

# Função para verificar se um tipo é numérico
def numeric(p):
    return p in (Char, Int, Float)

# Função para encontrar o tipo máximo entre dois tipos
def max_type(p1, p2):
    if not numeric(p1) or not numeric(p2):
        return None
    elif p1 == Float or p2 == Float:
        return Float
    elif p1 == Int or p2 == Int:
        return Int
    else:
        return Char