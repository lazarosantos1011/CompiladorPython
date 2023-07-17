# Arquivo Num.py

NUM = 'NUM'

def create_num_token(value):
    if not isinstance(value, int):
        raise ValueError("Num tokens must have integer values")
    return { 'tag': NUM, 'value': value }

def num_to_string(token):
    return str(token['value'])

# Exemplo

token1 = create_num_token(int(input("Digite um inteiro: ")))  # Cria token com a tag "NUM" e valor inteiro 42
token_string1 = num_to_string(token1)  # Converte o token para string
print(token_string1)  # Saída: '42'

token2 = create_num_token(int(input("Digite um inteiro: ")))  # Gera um ValueError pois 3.14 não é um inteiro
