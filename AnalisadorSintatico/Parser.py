from AnalisadorLexico import Lexer, Tag, Word, Token #Type
from CodigoIntermediario import Stmt, While, Id, Seq, Do, If, Else, Break, Arith, Set, SetElem, Unary, Expr, Node
from TabelaSimbolos import Array, Type
from CodigoDesvio import Or, And, Not, Rel, Access, Constant

top = None
used = 0

look = {}

def move():
    global look
    look = Lexer.scan()

def error(s):
    raise Exception(f"near line {Lexer.line}: {s}")

def match(t):
    global look
    print(look)
    if look["tag"] == t:
        move()
    else:
        error("syntax error")

def program():
    move()
    s = block()
    begin = s.newlabel()
    after = s.newlabel()
    Node.emitlabel(begin)
    Node.gen(begin, after)
    Node.emitlabel(after)

def block():
    match('{')
    savedEnv = top
    top = dict()
    decls()
    s = stmts()
    match('}')
    top = savedEnv
    return s

def decls():
    global used
    while look["tag"] == Tag.tags["BASIC"]:
        p = type()
        tok = look
        match(Tag.tags["ID"])
        match(';')
        id = Id(Word(tok), p, used)
        top[tok] = id
        used += p.width

def type():
    p = look
    match(Tag.tags["BASIC"])
    if look["tag"] != '[':
        return p
    else:
        return dims(p)

def dims(p):
    match('[')
    tok = look
    match(Tag.tags["NUM"])
    match(']')
    if look["tag"] == '[':
        p = dims(p)
    return Array(tok.value, p)

def stmts():
    if look["tag"] == '}':
        return Stmt.Null
    else:
        return Seq(stmt(), stmts())

def stmt():
    x = None
    s = None
    sl = None
    s2 = None
    savedStmt = None

    if look["tag"] == ';':
        move()
        return Stmt.Null
    elif look["tag"] == Tag.tags["IF"]:
        move()
        match('(')
        x = bool_node()
        match(')')
        sl = stmt()

        if look["tag"] != Tag.tags["ELSE"]:
            return If(x, sl)
        else:
            match(Tag.tags["ELSE"])
            s2 = stmt()
            return Else(x, sl, s2)
    elif look["tag"] == Tag.tags["WHILE"]:
        whilenode = While()
        savedStmt = Stmt.Enclosing
        Stmt.Enclosing = whilenode
        move()
        match('(')
        x = bool_node()
        match(')')
        sl = stmt()
        whilenode.init(x, sl)
        Stmt.Enclosing = savedStmt
        return whilenode
    elif look["tag"] == Tag.tags["DO"]:
        donode = Do()
        savedStmt = Stmt.Enclosing
        Stmt.Enclosing = donode
        move()
        sl = stmt()
        match(Tag.tags["WHILE"])
        match('(')
        x = bool_node()
        match(')')
        match(';')
        donode.init(sl, x)
        Stmt.Enclosing = savedStmt
        return donode
    elif look["tag"] == Tag.tags["BREAK"]:
        match(Tag.tags["BREAK"])
        match(';')
        return Break()
    elif look["tag"] == '{':
        return block()
    else:
        return assign()

def assign():
    global stmt
    t = look
    match(Tag.tags["ID"])
    id = top.get(t)
    if id is None:
        error(f"{t} undeclared")

    if look["tag"] == '=':
        move()
        stmt = Set(id, bool_node())
    else:
        x = offset(id)
        match('=')
        stmt = SetElem(x, bool_node())
        match(';')

    return stmt

def bool_node():
    x = join()
    while look["tag"] == Tag.tags["OR"]:
        tok = look
        move()
        x = Or.create_or(tok, x, join())
    return x

def join():
    x = equality()
    while look["tag"] == Tag.tags["AND"]:
        tok = look
        move()
        x = And.create_and(tok, x, equality())
    return x

def equality():
    x = rel()
    while look["tag"] == Tag.tags["EQ"] or look["tag"] == Tag.tags["NE"]:
        tok = look
        move()
        x = Rel.create_rel(tok, x, rel())
    return x

def rel():
    x = expr()
    if look["tag"] in ['<', Tag.tags["LE"], Tag.tags["GE"], '>']:
        tok = look
        move()
        return Rel(tok, x, expr())
    return x

def expr():
    x = term()
    while look["tag"] == '+' or look["tag"] == '-':
        tok = look
        move()
        x = Arith(tok, x, term())
    return x

def term():
    x = unary()
    while look["tag"] == '*' or look["tag"] == '/':
        tok = look
        move()
        x = Arith(tok, x, unary())
    return x

def unary():
    if look["tag"] == '-':
        move()
        return Unary(Word('minus'), unary())
    elif look["tag"] == '!':
        tok = look
        move()
        return Not.create_not(tok, unary())
    else:
        return factor()

def factor():
    global x
    if look["tag"] == '(':
        move()
        x = bool_node()
        match(')')
        return x
    elif look["tag"] == Tag.tags["NUM"]:
        x = Constant(look, Type.Int)
        move()
        return x
    elif look["tag"] == Tag.tags["REAL"]:
        x = Constant(look, Type.Float)
        move()
        return x
    elif look["tag"] == Tag.tags["TRUE"]:
        x = Constant(True)
        move()
        return x
    elif look["tag"] == Tag.tags["FALSE"]:
        x = Constant(False)
        move()
        return x
    elif look["tag"] == Tag.tags["ID"]:
        s = str(look)
        id = top.get(look)
        move()

        if look["tag"] != '[':
            return id
        else:
            return offset(id)

def offset(a):
    global x
    match('[')
    i = bool_node()
    match(']')
    type = a.type
    type = type.of
    w = Constant(type.width)
    tl = Arith(Token('*'), i, w)
    loc = tl

    while look["tag"] == '[':
        match('[')
        i = bool_node()
        match(']')
        type = type.of
        w = Constant(type.width)
        tl = Arith(Token('*'), i, w)
        t2 = Arith(Token('+'), loc, tl)
        loc = t2

    return Access.create_access(a, loc, type)

# Agora você pode chamar a função program() para começar o parsing.

