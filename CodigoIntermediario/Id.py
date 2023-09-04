
def create_op(tok, p):
    def op():
        return {
            "tok": tok,
            "type": p,
            "gen": gen,
            "reduce": reduce
        }
    
    def gen():
        return create_op(tok, p)
    
    def reduce():
        x = op()["gen"]()
        t = create_temp(op()["type"])
        emit(str(t) + " = " + str(x))
        return t
    
    return op()

def create_temp(p):
    count = 0
    
    def temp():
        nonlocal count
        count += 1
        return {
            "type": p,
            "number": count
        }
    
    def __str__():
        return "t" + str(temp()["number"])
    
    temp()["__str__"] = __str__
    return temp()

def emit(s):
    print("\t" + s)

