# Arq Break.py
from CodigoIntermediario import Stmt, Node

stmt = None

def create_break():
    global stmt

    if Stmt.Enclosing is None:
        Node.error("break não associado a um bloco")
    stmt = Stmt.Enclosing

def gen_break(b, a):
    Node.emit("goto L" + str(stmt["after"]))
