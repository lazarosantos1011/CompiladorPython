import sys
from AnalisadorLexico import Lexer
from AnalisadorSintatico import Parser

def main():
    try:
        # lex = Lexer()  # Criação de uma instância de Lexer para análise léxica.
        # parse = Parser(lex)  # Criação de uma instância de Parser, passando a instância de Lexer para análise sintática.
        Parser.program()  # Inicia a análise do programa.
        sys.stdout.write('\n')  # Escreve uma quebra de linha na saída padrão.
    except Exception as e:
        sys.stderr.write(f'Erro: {str(e)}\n')  # Trata e imprime quaisquer exceções na saída de erro padrão.

if __name__ == "__main__":
    main()  # Chama a função principal quando o script é executado.
