from CodigoIntermediario import Node

def expr(tok, p):
    op = tok
    type = p
    
    def gen():
        return expr
    
    def reduce():
        return expr
    
    def jumping(t, f):
        emitjumps(str(expr), t, f)
    
    def emitjumps(test, t, f):
        if t != 0 and f != 0:
            Node.emit("if " + test + " goto L" + str(t))
            Node.emit("goto L" + str(f))
        elif t != 0:
            Node.emit("if " + test + " goto L" + str(t))
        elif f != 0:
            Node.emit("iffalse " + test + " goto L" + str(f))
        else:
            pass
    
    def __str__():
        return str(op)
    
    return {
        "gen": gen,
        "reduce": reduce,
        "jumping": jumping,
        "emitjumps": emitjumps,
        "__str__": __str__
    }
