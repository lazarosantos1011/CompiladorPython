LEXEME = 0
TAG = 1

# Função para criar tokens
def create_token(lexeme, tag):
    return (lexeme, tag)

# Dicionário de tags e lexemas
tags = {
    'AND': create_token("&&", 256),
    'BASIC': create_token("BASIC", 257),
    'BREAK': create_token("BREAK", 258),
    'DO': create_token("DO", 259),
    'ELSE': create_token("ELSE", 260),
    'EQ': create_token("EQ", 261),
    'FALSE': create_token("FALSE", 262),
    'GE': create_token("GE", 263),
    'ID': create_token("ID", 264),
    'IF': create_token("IF", 265),
    'INDEX': create_token("INDEX", 266),
    'LE': create_token("LE", 267),
    'MINUS': create_token("MINUS", 268),
    'NE': create_token("NE", 269),
    'NUM': create_token("NUM", 270),
    'OR': create_token("OR", 271),
    'REAL': create_token("REAL", 272),
    'TEMP': create_token("TEMP", 273),
    'TRUE': create_token("TRUE", 274),
    'WHILE': create_token("WHILE", 275)
}

# Exemplo de uso
my_token = tags['REAL']
print(my_token[LEXEME])  # Saída: "&&"
print(my_token[TAG])  # Saída: 256
