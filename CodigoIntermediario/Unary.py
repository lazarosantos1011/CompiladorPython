from AnalisadorLexico.Lexer import Token
from TabelaSimbolos import Type
from CodigoIntermediario import Node

expr = None

def create_unary(tok, x):
    def unary():
        global expr
        nonlocal tok, x
        expr = x
        type = Type.max(Type.Int, expr["type"])
        if type is None:
            error("type error")
        return {
            "tok": tok,
            "expr": expr,
            "type": type,
            "gen": gen,
            "__str__": __str__
        }
    
    def gen():
        return create_unary(tok, expr["reduce"]())
    
    def __str__():
        return str(tok) + " " + str(expr)
    
    return unary()

def error(s):
    raise Node.error(s)  # SUBSTITUIR Error com a implementação real de erro

def emit(s):
    print("\t" + s)

