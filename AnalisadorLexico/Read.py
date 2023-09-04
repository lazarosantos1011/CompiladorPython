import Lexer

file = open("C://Users//edudo//OneDrive//Documentos//PYTHON//lexicalanalyzer//CompiladorPython//AnalisadorLexico//test.txt", "rb")
arq = []

for line in file:
    for character in line:
        arq.append(chr(character))

Lexer.cria_Lexer(arq)

while (Lexer.readch() < (len(arq)-1)):
    token = Lexer.scan()

for i in Lexer.retorno:
    print("Token: ", i)

file.close()