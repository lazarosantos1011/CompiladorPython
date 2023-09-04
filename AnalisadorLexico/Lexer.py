#type não ta utilizado corretamente, criar função depois.
#Faltando outra parte
from AnalisadorLexico import Real, Num, Token, Tag, Word, Table
# from Word import lexemes
line = 1
peek = ''
words = {}
global buffer
buffer = []
index = 0
retorno = []

simple_tags = [';', '-', '+', '*', '/', '(', ')', '[', ']', '{', '}']

def cria_Lexer(b):
    global buffer
    buffer = b
    print(buffer)

def readch():
    global index
    global peek
    global buffer
    peek = buffer[index]
    index+=1
    return index

def readch_next():
    global buffer
    global index
    return buffer[index]

def scan():
    global line
    global peek
    token = {}

    if peek == '\n':
        line += 1
        return True
    
    elif peek == ' ' or peek == '\t' or peek == '\r':
        return True
    
    elif peek == '&':
        if readch_next() == '&':
            readch()
            token = Word.lexemes['AND']
        else:
            token = Token.cria_Token('&')

    elif peek == '|':
        if readch_next() == '|':
            readch()
            token = Word.lexemes['OR']
        else:
            token = Token.cria_Token('|')

    elif peek == '=':
        if readch_next() == '=':
            readch()
            token = Word.lexemes['EQ']
        else:
            token = Token.cria_Token('=')

    elif peek == '!':
        if readch_next() == '=':
            readch()
            token = Word.lexemes['NE']
        else:
            token = Token.cria_Token('!')

    elif peek == '<':
        if readch_next() == '=':
            readch()
            token = Word.lexemes['LE']
        else:
            token = Token.cria_Token('<')

    elif peek == '>':
        if readch_next() == '=':
            readch()
            token = Word.lexemes['GE']
        else:
            token = Token.cria_Token('>')

    elif peek in simple_tags:
        token = Token.cria_Token(peek)

    if peek.isdigit():
        v = int(peek)
        while readch_next().isdigit():
            readch()
            v = 10 * v + int(peek)

        if readch_next() != '.':
            token = Num.create_num_token(v)
        
        readch()
        v = float(v)
        d = 10.0

        while readch_next().isdigit():
            readch()
            v = v + int(peek) / d
            d = d * 10.0
        if not v in Table.values:
            Table.values.append(v)
        token = Real.create_real_token(v)
    
    if peek.isalpha():
        b = peek
        while readch_next().isalpha():
            readch()
            b += peek

        w = Word.lexemes.get(b.upper())
        if w is not None: # cria token de palavra reservada
            token = w
        else:
            w = Word.create_token(b, Tag.tags.get('ID')) # cria token de id
            if not b in Table.ids:
                Table.ids.append(b)
            token = w

    retorno.append(token)
    return token
