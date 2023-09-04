from AnalisadorLexico import Word
from TabelaSimbolos import Type

def create_temp(p):
    count = 0
    
    def temp():
        nonlocal count
        count += 1
        return {
            "p": p,
            "number": count,
            "__str__": __str__
        }
    
    def __str__():
        return "t" + str(temp()["number"])
    
    temp()["__str__"] = __str__
    return temp()

