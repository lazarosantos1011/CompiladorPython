# Arquivo Num.py

NUM = 'NUM'

def create_num_token(value):
    return (NUM, value)

def num_to_string(token):
    return str(token[1])

# Usage example
token = create_num_token(42)  # Create a token with tag 'NUM' and value 42
token_string = num_to_string(token)  # Convert the token to a string
print(token_string)  # Output: '42'