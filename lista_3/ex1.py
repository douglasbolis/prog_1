__author__ = 'douglas'

def f_adicionaFilmeAtores(d, f, n):

    if f in d:
        d[f].append(n)
    else:
        d[f] = [n]
    #fim if
#fim funcao