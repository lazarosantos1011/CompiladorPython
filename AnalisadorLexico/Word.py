LEXEME = 0
TAG = 1

# Função para criar tokens
def create_token(lexeme, tag, width = ""):
    if width == "":
        return {'lexeme': lexeme, 'tag': tag}
    else:
        return {'lexeme': lexeme, 'tag': tag, 'width': width}

# Dicionário de tags e lexemas
lexemes = {
    'AND': create_token("&&", 256),
    'BASIC': create_token("basic", 257),
    'INT': create_token('int', 257, 4),
    'BOOL': create_token('bool', 257, 1),
    'FLOAT': create_token('float', 257, 8),
    'CHAR': create_token('char', 257, 1),
    'BREAK': create_token("break", 258),
    'DO': create_token("do", 259),
    'ELSE': create_token("else", 260),
    'EQ': create_token("==", 261),
    'FALSE': create_token("false", 262),
    'GE': create_token(">=", 263),
    'ID': create_token("id", 264),
    'IF': create_token("if", 265),
    'INDEX': create_token("index", 266),
    'LE': create_token("<=", 267),
    'MINUS': create_token("minus", 268),
    'NE': create_token("!=", 269),
    'NUM': create_token("num", 270),
    'OR': create_token("||", 271),
    'REAL': create_token("real", 272),
    'TEMP': create_token("temp", 273),
    'TRUE': create_token("true", 274),
    'WHILE': create_token("while", 275)
}

# Exemplo de uso
#retirar o exemplo na hora da implementação
#my_token = tags['REAL']
#print(my_token[LEXEME])  # Saída: "&&"
#print(my_token[TAG])  # Saída: 256
