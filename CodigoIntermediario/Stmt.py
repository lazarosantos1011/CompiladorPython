# Arq Stmt.py
from CodigoIntermediario import Node, Expr

# Criando uma função para Stmt
def stmt():
    def gen(b, a): # essa função é implementada nas "subclasses"
        pass  # Implemente a lógica da função gen aqui

    after = 0

    def enclosing():
        return None

    return {
        "gen": gen,
        "after": after,
        "enclosing": enclosing
    }

# Criando uma instância nula de Stmt
Stmt_Null = stmt()

# Criando uma instância nula de Stmt para Enclosing
Stmt_Enclosing = Stmt_Null
