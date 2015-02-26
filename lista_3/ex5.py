import ex1

__author__ = 'douglas'

def main():
    dicAcervo, nomeFilme, nomeAtor = {}, "", ""
    contTest = 0

    #while contTest < 3:
    nomeFilme = input("Informe o nome do Filme: ")
    nomeAtor = input("Informe o nome de um Ator para o Filme %s: " %(nomeFilme))
    ex1.f_adicionaFilmeAtores(dicAcervo, nomeFilme, nomeAtor)
    #contTest += 1
    #fim while

    print(dicAcervo)
#fim main

if __name__ == "__main__":
    main()
#fim if