__author__ = 'douglas'

# Exercício (1)
# funcao responsavel para cadastrar as imagens no dicionario
def f_cadastraImagem(dic, nome, lst):
    # [x1, y1, x2, y2]
    canSupEsqN = (lst[0], lst[1])
    canInfDirN = (lst[2], lst[3])
    canSupDirN = (lst[2] - lst[0], lst[1])
    canInfEsqN = (lst[0], lst[3] - lst[1])

    # print(canSupEsqN)
    # print(canInfDirN)
    # print(canSupDirN)
    # print(canInfEsqN)

    if nome in dic:
        print("Imagem já cadastrada.")
    else:
        for chave, valor in dic.items():
            canSupEsq = (valor[0], valor[1])
            canInfDir = (valor[2], valor[3])
            canSupDir = (valor[2] - valor[0], valor[1])
            canInfEsq = (valor[0], valor[3] - valor[1])

            if ((canInfDir[0] >= canSupEsqN[0]) and (canInfDir[1] >= canSupEsqN[1])):
                print("aqui 1")
                if ((canSupDir[0] >= canInfEsqN[0]) and (canSupDir[1] <= canInfEsqN[1])):
                    print("aqui 2")
                    if ((canSupEsq[0] <= canInfDirN[0]) and (canSupEsq[1] <= canInfDirN[1])):
                        print("aqui 3")
                        if ((canInfEsq[0] <= canSupDirN[0]) and (canInfEsq[1] >= canSupDirN[1])):
                            print("aqui 4")
                            print("A imagem sobrepoe outra figura.")
            else:
                print("aqui a")
                dic[nome] = lst
            #fim if
        #fim for
    #fim if
#fim funcao


def main():
    tamTela = [0, 0, 1200, 786]
    dimensao = []
    dicPropag = {}
    nomeImagem, xi, yi, xf, yf = "", 0, 0, 0, 0

    nomeImagem = input("Informe o nome da imagem: ")

    while nomeImagem != "":
        print("Informe os pixels iniciais da imagem para: ")
        xi = int(input("X inicial: "))
        yi = int(input("Y inicial: "))

        if ((xi >= tamTela[0]) and (xi <= tamTela[2])) and ((yi >= tamTela[1]) and (yi <= tamTela[3])):
            print("Informe os pixels finais da imagem para: ")
            xf = int(input("X final: "))
            yf = int(input("Y final: "))
            if ((xf > xi) and (xf <= tamTela[2])) and ((yf > yi) and (yf <= tamTela[3])):
                print("aqui A1")
                dimensao = [xi, yi, xf, yf, 0]
                f_cadastraImagem(dicPropag, nomeImagem, dimensao)
            #fim if
        #fim if
        nomeImagem = input("Informe o nome da imagem: ")
    #fim while
    print(dicPropag)

#fim main

if __name__ == "__main__":
    main()
#fim if