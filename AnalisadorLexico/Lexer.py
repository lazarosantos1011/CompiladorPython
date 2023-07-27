#type não ta utilizado corretamente, criar função depois.
#Faltando outra parte
from typing import Type
from Tag import tag
from Word import create_token
import sys

line = 1
peek = ''
words = {}

def reserve(w):
    words[w.lexeme] = w

def Lexer():
    reserve(create_token("if", tag.IF))
    reserve(create_token("else", tag.ELSE))
    reserve(create_token("while", tag.WHILE))
    reserve(create_token("do", tag.DO))
    reserve(create_token("break", tag.BREAK))
    reserve(create_token("true", tag.TRUE))
    reserve(Type.Int)
    reserve(Type.Bool)
    reserve(create_token("False", tag.FALSE))
    reserve(Type.Char)
    reserve(Type.Float)

def readch():
    global peek
    peek = sys.stdin.read(1)

def readch(c):
    readch()
    if peek != c:
        return False
    peek = ''
    return True
#FALTA TERMINAR
def scan():
    while True:
        if peek == '\n':
            line += 1
        else:
            break

    if peek == '&':
        if readch('&'):
            return Word.and_token
        else:
            return Token('&')
    elif peek == '|':
        if readch('|'):
            return Word.or_token
        else:
            return Token('|')
    elif peek == '=':
        if readch('='):
            return Word.eq_token
        else:
            return Token('=')
    elif peek == '!':
        if readch('='):
            return Word.ne_token
        else:
            return Token('!')
    elif peek == '<':
        if readch('='):
            return Word.le_token
        else:
            return Token('<')
    elif peek == '>':
        if readch('='):
            return Word.ge_token
        else:
            return Token('>')

    if peek.isdigit():
        v = 0
        while peek.isdigit():
            v = 10 * v + int(peek)
            readch()

        if peek != '.':
            return Num(v)
        
        x = float(v)
        d = 10.0

        while True:
            readch()
            if not peek.isdigit():
                break
            x = x + int(peek) / d
            d = d * 10.0
        
        return Real(x)

    if peek.isalpha():
        b = ''
        while peek.isalnum():
            b += peek
            readch()

        s = b
        w = Word.get(s)
        if w is not None:
            return w
        else:
            w = Word(s, Tag.ID)
            words[s] = w
            return w
