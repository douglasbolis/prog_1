__author__ = 'douglas'

# Função do exercício (1)
def f_adicionaFilmeAtor(d, f, n):
    if f in d:
        d[f].append(n)
    else:
        d[f] = [n]
    #fim if
#fim funcao

# Função do exercício (2)
def f_insereFilmeAtores(dicAcervo):
    nomeFilme, nomeAtor, lstAtor = "", "", []

    nomeFilme = input("Digite o nome do Filme: ")
    nomeAtor = input("Digite o nome de um Ator para o Filme: ")

    while nomeAtor != "":
        f_adicionaFilmeAtor(dicAcervo, nomeFilme, nomeAtor)
        nomeAtor = input("Digite o nome de um Ator para o Filme: [String vazia encerra]: ")
    #fim while
#fim funcao

# Função do exercício (3)
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
            if cod == 3:
                print("Atores de %s e %s:" %(filmeSt, filmeNd))
                f_somenteEmUmFilme(dicAcervo, filmeSt, filmeNd)
                f_somenteEmUmFilme(dicAcervo, filmeNd, filmeSt)
            else:
                print("Condigo invalido!")
            #fim if
        #fim if
    #fim id
#fim funcao

# Função do exercício (4)
def f_contracenouAtor(dic, ator):
    lstFilmes, lstAtores = [], []

    print("\nOs(As) Atores/Atrizes que contracenaram com %s: " %(ator))
    for chave, valor in dic.items():
        for elem in valor:
            if ator == elem:
                f_insereLista(lstFilmes, chave)
             #fim if
        #fim for
        for elem in lstFilmes:
            for contr in range(len(dic[elem])):
                if ator != dic[elem][contr]:
                    f_insereLista(lstAtores, dic[elem][contr])
                #fim if
            #fim for
        #fim for
    #fim for
    for el in lstAtores:
        print("\t- %s" %(el))
        #fim for
#fim funcao

# Função auxiliar para inserir elementos numa lista
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

# Funcao auxiliar do exercício (3) para exibir os atores que estao somente em um dos filmes passado pelo parametro
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

# Função auxiliar para exibir os filmes, se o segundo parametro for 'True' ela também exibirá os atores dos filmes
def f_exibeFilmesAtores(dic, ator):
    print("\n----------------- Filmes -----------------")
    for chave, valor in dic.items():
        print("%s" %(chave))
        if ator:
            for el in valor:
                print("\t- %s" %(el))
            #fim for
            print("")
        #fim if
    #fim for
    print("")
#fim funcao

# Função main do exercicio (5)
def main():
    nomeFilme, nomeAtor, filmeSt, filmeNd, cod = "", "", "", "", 5
    dicAcervo = {}
        # "Anchorman 2: The Lengend Continues":["Will Ferrell", "Steve Carell", "Paul Rudd", "Adam McKay"],
        # "Ironman 2": ["Robert Downey Jr", "Mickey Rourke", "Gwyneth Paltrow", "Scarlett Johansson", "Samuel L. Jackson"],
        # "The Avengers": ["Robert Downey Jr", "Mark Rufallo", "Chris Hemsworth", "Chris Evans", "Scarlett Johansson", "Jeremy Renner"],
        # "RED": ["Bruce Willis", "Morgan Freeman", "Helen Mirren", "John Malkovich"],
        # "Sin City": ["Bruce Willis", "Mickey Rourke", "Jessica Alba", "Clive Owen"]
        # }

# Utilizando a função desenvolvida para o exercício (1)
    nomeFilme = input("Informe o nome do Filme: ")
    nomeAtor = input("Informe o nome de um Ator para o Filme %s: " %(nomeFilme))
    f_adicionaFilmeAtor(dicAcervo, nomeFilme, nomeAtor)

# Utilizando a função desenvolvida para o exercício (2)
    f_insereFilmeAtores(dicAcervo)

# Utilizando a função para fins de conferir se os filmes e atores foram inseridos corretamente
# E também para auxiliar a escolha no exercício (3)
    f_exibeFilmesAtores(dicAcervo, True)

# Utilizando a função desenvolvida para o exercício (3)
    print("Escolha dois filmes da lista acima")
    filmeSt = input("Primeiro Filme: ")
    filmeNd = input("Segundo Filme: ")
    print("\nFilmes: '%s e %s'" %(filmeSt, filmeNd))
    print("1 - Exibir na tela todos os Atores que aparecem nos dois Filmes")
    print("2 - Exibir na tela todos os Atores que estao nos dois Filmes")
    print("3 - Exibir na tela todos os Atores que estao somente em um dos Filmes")
    print("0 - Encerra")
    cod = int(input("Opcao: "))

    while cod != 0:
        f_exibeAtores(dicAcervo, filmeSt, filmeNd, cod)
        print("\nFilmes: '%s e %s'" %(filmeSt, filmeNd))
        print("1 - Exibir na tela todos os Atores que aparecem nos dois Filmes")
        print("2 - Exibir na tela todos os Atores que estao nos dois Filmes")
        print("3 - Exibir na tela todos os Atores que estao somente em um dos Filmes")
        print("0 - Encerra")
        cod = int(input("Opcao: "))
    #fim while

# Utilizando a função desenvolvida para o exercício (4)
    nomeAtor = input("Informe o nome de um Ator: ")
    f_contracenouAtor(dicAcervo, nomeAtor)

    return 0
#fim main

if __name__ == "__main__":
    main()
#fim if