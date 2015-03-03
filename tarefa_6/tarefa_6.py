__author__ = 'douglas'

# Exercício (1)
# funcao responsavel para cadastrar as imagens no dicionario
def f_cadastraImagem(dic, nome, lst):

    canSupEsqN = (lst[0], lst[1])
    canInfDirN = (lst[2], lst[3])
    canSupDirN = (lst[2] - lst[0], lst[1])
    canInfEsqN = (lst[0], lst[3] - lst[1])

    if nome in dic:
        print("Imagem já cadastrada.")
    else:
        if ():
            for chave, valor in dic.items():
                canSupEsq = (valor[0], valor[1])
                canInfDir = (valor[2], valor[3])
                canSupDir = (valor[2] - valor[0], valor[1])
                canInfEsq = (valor[0], valor[3] - valor[1])

                if (canSupEsq < canSupEsqN) and (canSupDir < canSupDirN) and (canInfDir < canInfDirN) and (canInfEsq < canInfEsqN):
                    print("A imagem sobrepoe outra figura.")
                else:
                    dic[nome] = lst
                #fim if
            #fim for
    #fim if
#fim funcao


def main():
    tamTela = [(0, 0), (1200, 786)]
    dimensao = []
    dicPropag = {}
    nomeImagem, xi, yi, xf, yf = "", 0, 0, 0, 0

    nomeImagem = input("Informe o nome da imagem: ")

    while nomeImagem != "":
        print("Informe os pixels iniciais da imagem para: ")
        xi = int(input("X inicial: "))
        yi = int(input("Y inicial: "))

        if ((xi >= 0) and (xi <= 1200)) and ((yi >= 0) and (yi <= 786)):
            print("Informe os pixels finais da imagem para: ")
            xf = int(input("X final: "))
            yf = int(input("Y final: "))
            if ((xf > xi) and (xf <= 1200)) and ((yf > yi) and (yf <= 786)):
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