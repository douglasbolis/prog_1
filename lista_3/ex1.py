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
    lst = []

    print("")
    if cod == 1:
        print("Atores de %s e %s:" %(filmeSt, filmeNd))
        for el in dicAcervo[filmeSt]:
            f_insereLista(lst, el)
        #fim for
        for el in dicAcervo[filmeNd]:
            f_insereLista(lst, el)
        #fim for

        for elem in lst:
            print("\t-%s" %(elem))
        #fim for
    else:
        if cod == 2:
            print("Atores de %s e %s:" %(filmeSt, filmeNd))
            for el in dicAcervo[filmeSt]:
                for il in dicAcervo[filmeNd]:
                    if el == il:
                        print("\t-%s" %(el))
                    #fim if
                #fim for
            #fim for
        else:
            print("Atores de %s e %s:" %(filmeSt, filmeNd))
            f_somenteEmUmFilme(dicAcervo, filmeSt, filmeNd)
            f_somenteEmUmFilme(dicAcervo, filmeNd, filmeSt)
        #fim if
    #fim id
#fim funcao

def f_insereLista(lst, el):
    igual = False

    for i in range(len(lst)):
        if el == lst[i]:
            igual = True
        #fim if
    #fim for

    if not igual:
        lst.append(el)
    #fim if
#fim funcao

def f_somenteEmUmFilme(dic, filmeA, filmeB):
    contA, contB, igual = 0, 0, False
    while contA < len(dic[filmeA]):
        igual = False
        contB = 0
        while contB < len(dic[filmeB]):
            if dic[filmeA][contA] == dic[filmeB][contB]:
                igual = True
            #fim if
            contB += 1
        #fim while
        if not igual:
            print("\t-%s" %(dic[filmeA][contA]))
        #fim if
        contA += 1
    #fim while
#fim funcao

def f_imprimeFilmes(dic):
    print("----------------- Filmes -----------------")
    for chave in dic.keys():
        print("%s" %(chave))
    #fim for
    print("")
#fim funcao

def f_contracenouAtor(dic, ator):
    lst, contracanou = [], False

    print("Os(As) Atores/Atrizes que contracenaram com %s: " %(ator))
    for chave, valor in dic.items():
        for elem in valor:
            if ator == elem:
                contracenou = True
            #fim if
        #fim for
    #fim for
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

    # f_imprimeFilmes(dicAcervo)
    #
    # print("Escolha dois filmes da lista acima")
    # filmeSt = input("Primeiro Filme: ")
    # filmeNd = input("Segundo Filme: ")
    # print("\nFilmes: '%s e %s'" %(filmeSt, filmeNd))
    # print("1 - Exibir na tela todos os Atores que aparecem nos dois Filmes")
    # print("2 - Exibir na tela todos os Atores que estao nos dois Filmes")
    # print("3 - Exibir na tela todos os Atores que estao somente em um dos Filmes")
    # print("0 - Encerra")
    # cod = int(input("Opcao: "))
    #
    # while cod != 0:
    #     f_exibeAtores(dicAcervo, filmeSt, filmeNd, cod)
    #     print("\nFilmes: '%s e %s'" %(filmeSt, filmeNd))
    #     print("1 - Exibir na tela todos os Atores que aparecem nos dois Filmes")
    #     print("2 - Exibir na tela todos os Atores que estao nos dois Filmes")
    #     print("3 - Exibir na tela todos os Atores que estao somente em um dos Filmes")
    #     print("0 - Encerra")
    #     cod = int(input("Opcao: "))
    #fim while

    nomeAtor = input("Informe o nome de um Ator: ")
    f_contracenouAtor(dicAcervo, nomeAtor)



#fim main

if __name__ == "__main__":
    main()
#fim if