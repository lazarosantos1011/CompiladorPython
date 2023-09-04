# ambiente que é usado para rastrear informações 
# de símbolos em um programa ou contexto específico.
from AnalisadorLexico import Tag
from CodigoIntermediario import Id

# File: Env.py
def create_env(n):
    table = {}
    prev = n

    def put(w, i):
        nonlocal table
        table[w] = i

    def get(w):
        nonlocal table, prev
        e = create_env
        while e:
            found = e.table.get(w)
            if found:
                return found
            e = e.prev
        return None

    return {"put": put, "get": get}

'''from lexer import Token
from inter import Id'''

# Usage example
if __name__ == "__main__":
    # Creating environment instances
    global_env = create_env(None)
    local_env1 = create_env(global_env)
    local_env2 = create_env(local_env1)

    # Creating identifiers
    id1 = Id("x", Tag.ID)
    id2 = Id("y", Tag.ID)
    id3 = Id("z", Tag.ID)

    # Putting identifiers in environments
    global_env["put"](id1, "Value of x")
    local_env1["put"](id2, "Value of y in local_env1")
    local_env2["put"](id3, "Value of z in local_env2")

    # Getting identifiers from environments
    search_id = "x"
    result1 = global_env["get"](search_id)
    result2 = local_env1["get"](search_id)
    result3 = local_env2["get"](search_id)

    print("Result from global_env:", result1)
    print("Result from local_env1:", result2)
    print("Result from local_env2:", result3)
