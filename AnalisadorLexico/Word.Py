LEXEME = 0
TAG = 1

# Função para criar tokens
def create_token(lexeme, tag):
    return (lexeme, tag)

# Tokens
AND = create_token("&&", 256)
OR = create_token("||", 257)
EQ = create_token("==", 258)
NE = create_token("!=", 259)
LE = create_token("<=", 260)
GE = create_token(">=", 261)
MINUS = create_token("minus", 262)
TRUE = create_token("True", 263)
FALSE = create_token("False", 264)
TEMP = create_token("t", 265)

# Exemplo de uso
my_token = AND
print(my_token[LEXEME])  # Saída: "&&"
print(my_token[TAG])  # Saída: 256
