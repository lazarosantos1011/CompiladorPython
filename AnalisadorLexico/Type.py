from AnalisadorLexico import Word

int_type = ("int", Word.lexemes['BASIC'], 4)
float_type = ("float", Word.lexemes['BASIC'], 8)
char_type = ("char", Word.lexemes['BASIC'], 1)
bool_type = ("bool", Word.lexemes['BASIC'], 1)

def is_numeric(p):
    return p in (char_type, int_type, float_type)

def max_type(p1, p2):
    if not is_numeric(p1) or not is_numeric(p2):
        return None
    elif p1 == float_type or p2 == float_type:
        return float_type
    elif p1 == int_type or p2 == int_type:
        return int_type
    else:
        return char_type