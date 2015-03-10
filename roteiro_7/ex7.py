__author__ = 'douglas'

def f_preencheMatriz(nome, a, b):
    dic = {}
    print("\nInforme um numero para:")
    for i in range(a):
        for j in range(b):
            elem = int(input("%s%d%d: " %(nome.upper(), i+1, j+1)))
            dic[(i,j)] = elem
        #fim for
    #fim for

    return dic
#fim funcao

def main():
    dicMatriz = {}
    nome = input("Informe uma letra que represente sua matriz: ")
    tamL = int(input("Informe a qtd de linhas da matriz %s: " %(nome.upper())))
    tamC = int(input("Informe a qtd de colunas da matriz %s: " %(nome.upper())))
    dicMatriz = f_preencheMatriz(nome, tamL, tamC)

    print("\nMatriz %s:" %(nome.upper()))
    for i in range(tamL):
        print("")
        for j in range(tamC):
            print(" %d" %(dicMatriz[(i,j)]), end="")
        #fim for
    #fim for
    print("")
    print(dicMatriz)
    print("")
#fim main

if __name__ == "__main__":
    main()
#fim if