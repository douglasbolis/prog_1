__author__ = 'douglas'

def f_adicionaFilmeAtor(d, f, n):

    if f in d:
        d[f].append(n)
    else:
        d[f] = [n]
    #fim if
#fim funcao

def f_insereFilmeAtores(dicAcervo):
    nomeFilme, nomeAtor, lstAtor = "", "", []

    nomeFilme = input("Digite o nome do Filme: ")
    nomeAtor = input("Digite o nome de um Ator para o Filme: ")

    while nomeAtor != "":
        f_adicionaFilmeAtor(dicAcervo, nomeFilme, nomeAtor)
        nomeAtor = input("Digite o nome de um Ator para o Filme: [String vazia encerra]: ")
    #fim while
#fim funcao

def f_exibeAtores(dicAcervo, filmeSt, filmeNd):
    s=0
#fim funcao

def f_imprimeDados(dic):
    for chave, valor in dic.items():
        print("%s" %(chave))
        for elemento in valor:
            print("\t- %s" %(elemento))
    #fim for
    print("")
#fim funcao

def main():
    dicAcervo = {"Achorman 2: The Lengend Continues":["Will Ferrell", "Steve Carell", "Paul Rudd", "Adam McKay"]}
    nomeFilme, nomeAtor = "", ""

    #nomeFilme = input("Informe o nome do Filme: ")
    #nomeAtor = input("Informe o nome de um Ator para o Filme %s: " %(nomeFilme))
    #f_adicionaFilmeAtor(dicAcervo, nomeFilme, nomeAtor)
    #f_insereFilmeAtores(dicAcervo)

    f_imprimeDados(dicAcervo)

    print(dicAcervo)
#fim main

if __name__ == "__main__":
    main()
    #fim if