from AnalisadorLexico import Tag

def create_real_token(value):
    if isinstance(value, int):
        value = float(value)
    return { 'tag': Tag.tags.get('REAL'), 'value': value }

def real_to_string(token):
    return str(token['value'])

# Usage example
#token1 = create_real_token(float(input("Digite um número real: ")))  # Create a token with tag 'REAL' and integer value 3
#token_string1 = real_to_string(token1)  # Convert the token to a string
#print(token_string1)  # Output: '3.0'

#token2 = create_real_token(float(input("Digite um número real: ")))  # Create a token with tag 'REAL' and float value 3.14
#token_string2 = real_to_string(token2)  # Convert the token to a string
#print(token_string2)  # Output: '3.14'