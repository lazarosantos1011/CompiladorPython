# Arquivo: Array.py
from AnalisadorLexico import Tag

def create_array(sz, p):
    def get_width():
        return sz * p["get_width"]()

    def to_string():
        return "[" + str(size) + "]" + p["to_string"]()

    return {"get_width": get_width, "to_string": to_string}

# Funções para Type e Real
def create_type(name, lexeme, width):
    return {"get_width": lambda: width, "to_string": lambda: name}

def create_real():
    return {"get_width": lambda: 0, "to_string": lambda: ""}

# Definições e inicializações
def create_real_token(v):
    return {"tag": Tag.tags.get("REAL"), "value": v}

# Uso
size = 1
p = create_type("int", None, 4)  # Substituir None com um lexeme apropriado para o int_type
array = create_array(size, p)
print(array["get_width"]())  # Output: 4
print(array["to_string"]())  # Output: [1] (assumindo que int_type define 'int' como o name)
