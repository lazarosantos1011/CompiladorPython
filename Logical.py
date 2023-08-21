def check(pi, p2):
    if pi == "Type.Bool" and p2 == "Type.Bool":
        return "Type.Bool"
    else:
        return None

def gen(exprl, op, expr2, newlabelQ, emit, emitlabel):
    f = newlabelQ()
    a = newlabelQ()
    temp = f"Temp({type})"

    jumping(0, f)

    emit(f"{temp} = true")
    emit(f"goto L{a}")
    emitlabel(f)
    emit(f"{temp} = false")
    emitlabel(a)

    return temp

def toStringO(exprl, op, expr2):
    return f"{exprl} {op} {expr2}"

# Exemplo de uso:

exprl = "some_exprl"
expr2 = "some_expr2"
op = "&&"
type = "Type.Bool"

def newlabelQ():
    # Implementação da função newlabelQ
    pass

def jumping(condition, label):
    # Implementação da função jumping
    pass

def emit(code):
    # Implementação da função emit
    pass

def emitlabel(label):
    # Implementação da função emitlabel
    pass

result = check(exprl.type, expr2.type)
if result is None:
    error("type error")

gen_result = gen(exprl, op, expr2, newlabelQ, emit, emitlabel)
string_representation = toStringO(exprl, op, expr2)

print(result)
print(gen_result)
print(string_representation)
