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

def f_exibeAtores(dicAcervo, filmeSt, filmeNd, cod):
    if cod == 1:
        print("Atores de %s e %s:" %(filmeSt, filmeNd))
        for el in dicAcervo[filmeSt]:
            print("\t-%s" %(el))
        #fim for
        for el in dicAcervo[filmeNd]:
            print("\t-%s" %(el))
        #fim for
    else:
        if cod == 2:
           s=0
        else:
            s=0
        #fim if
    #fim id
#fim funcao

def f_imprimeFilmes(dic):
    print("----------------- Filmes -----------------")
    for chave, valor in dic.items():
        print("%s" %(chave))
    #fim for
    print("")
#fim funcao

def main():
    dicAcervo = {
        "Anchorman 2: The Lengend Continues":["Will Ferrell", "Steve Carell", "Paul Rudd", "Adam McKay"],
        "Ironman": ["Robert Downey Jr", "Terrence Howard", "Jeff Bridges"],
        "The Avengers": ["Robert Downey Jr", "Mark Rufallo", "Chris Hemsworth", "Chris Evans", "Scarlett Johansson", "Jeremy Renner"]
        }
    nomeFilme, nomeAtor, filmeSt, filmeNd, cod = "", "", "", "", 5

    #nomeFilme = input("Informe o nome do Filme: ")
    #nomeAtor = input("Informe o nome de um Ator para o Filme %s: " %(nomeFilme))
    #f_adicionaFilmeAtor(dicAcervo, nomeFilme, nomeAtor)
    #f_insereFilmeAtores(dicAcervo)

    f_imprimeFilmes(dicAcervo)

    print("Escolha dois filmes da lista acima")
    filmeSt = input("Primeiro Filme: ")
    filmeNd = input("Segundo Filme: ")

    while cod!= 0:
        cod=1
        f_exibeAtores(dicAcervo, filmeSt, filmeNd, cod)
        cod=0
    #fim while
#fim main

if __name__ == "__main__":
    main()
#fim if