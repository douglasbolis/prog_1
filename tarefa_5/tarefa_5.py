__author__ ='douglas'

# Exercício proposto para a manipulação de frações:

# Função implementada jundo a Letra (A) para cria uma nova fração
# através do parametro do tipo tupla com dois elementos do tipo inteiro
def f_criaFracao(n, d):
	t = ()
	
	if (n<0 and d<0) or (n>0 and d<0):
		t = (-n, -d)
	else:
		if d == 0:
			t = (n, 1)
		else:
			t = (n, d)
		#fim if
	#fim if
	return t
#fim funcao

# Função implementada jundo a Letra (B) para retornar o maximo divisor comum
# entre o numerador e o denominador de uma fração através do parametro passado
# do tipo tupla com dois elementos do tipo inteiro
def f_mdc(f1):
	mdc, resto, aux = 0, 0, 0
	n, d = 0, 0

	if f1[0] > f1[1]:
		n = f1[0]
		d = f1[1]
	else:
		n = f1[1]
		d = f1[0]
	#fim if

	resto = n%d

	while resto != 0:
		n = d
		d = resto
		resto = n%d
	#fim while

	mdc = d

	return mdc
#fim funcao

# Função implementada jundo a Letra (C) para retornar uma nova fração simplificada
# vinda de uma outra fração passada como parametro do tipo tupla com dois elementos
# do tipo inteiro
def f_simplifica(f):
	novaf, x = (), 0
	
	x = abs(f_mdc(f))
	novaf = f_criaFracao(f[0]//x, f[1]//x)
	
	return novaf
#fim funcao

# Função implementada jundo a Letra (D) para retornar a soma simplificada simplificada
# de duas frações vindas como parametro do tipo tupla com dois elementos do tipo inteiro
def f_soma(f1, f2):
	n, d = 0, 0

	d = f1[1]*f2[1]
	n = ((d//f1[1])*f1[0]) + ((d//f2[1])*f2[0])
	
	return f_simplifica(f_criaFracao(n, d))
#fim funcao

# Função implementada jundo a Letra (E) para retornar a subtração simplificada simplificada
# de duas frações vindas como parametro do tipo tupla com dois elementos do tipo inteiro
def f_subtracao(f1, f2):
	t = ()
	
	t = f_criaFracao(-f2[0], f2[1])	
	return (f_soma(f1, t))
#fim funcao

# Função implementada jundo a Letra (F) para retornar a multiplicação simplificada simplificada
# de duas frações vindas como parametro do tipo tupla com dois elementos do tipo inteiro
def f_multiplicacao(f1, f2):
	n, d = 0, 0

	d = f1[1]*f2[1]
	n = f1[0]*f2[0]

	return f_simplifica(f_criaFracao(n, d))
#fim funcao

# Função implementada jundo a Letra (G) para retornar a divisão simplificada simplificada
# de duas frações vindas como parametro do tipo tupla com dois elementos do tipo inteiro
def f_divisao(f1, f2):
	n, d = 0, 0

	d = f1[1]*f2[0]
	n = f1[0]*f2[1]

	return f_simplifica(f_criaFracao(n, d))
#fim funcao

def f_impropria(f):
	impropria = False

	if f[0] >= f[1]:
		impropria = True
	else:
		impropria = False
	#fim if

	return impropria
#fim funcao

def f_imprimeFracao(f):
	print("%d/%d" %(f[0], f[1]))
#fim funcao

# Função implementada junto a Letra (J) para desenvolver um main() para testar as funções
# criadas acima
def main():
	num1, den1, num2, den2 = 0, 0, 0, 0
	frac1, frac2, frac3, frac4, frac5, frac6 = (), (), (), (), (), ()

	print("\nValores para a 1ª fracao:")
	num1 = int(input("Numerador: "))
	den1 = int(input("Denominador: "))

	print("\nValores para a 2ª fracao:")
	num2 = int(input("Numerador: "))
	den2 = int(input("Denominador: "))

	frac1 = f_criaFracao(num1, den1)
	frac2 = f_criaFracao(num2, den2)

	frac3 = f_soma(frac1, frac2)
	frac4 = f_subtracao(frac1, frac2)
	frac5 = f_multiplicacao(frac1, frac2)
	frac6 = f_divisao(frac1, frac2)

	print("\nFrações geradas pelo programa:")
	f_imprimeFracao(frac3)
	f_imprimeFracao(frac4)
	f_imprimeFracao(frac5)
	f_imprimeFracao(frac6)

	return 0
#fim main

if __name__ == '__main__':
	main()
#fim if
