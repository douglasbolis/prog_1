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

def f_simplifica(f):
	novaf, x = (), 0
	
	x = abs(f_mdc(f))
	novaf = f_criaFracao(f[0]//x, f[1]//x)
	
	return novaf
#fim funcao

def f_soma(f1, f2):
	n, d = 0, 0

	d = f1[1]*f2[1]
	n = ((d//f1[1])*f1[0]) + ((d//f2[1])*f2[0])
	
	return f_simplifica(f_criaFracao(n, d))
#fim funcao

def f_subtracao(f1, f2):
	t = ()
	
	t = f_criaFracao(-f2[0], f2[1])	
	return (f_soma(f1, t))
#fim funcao

def f_multiplica(f1, f2):
	d = 0
	
#fim funcao
def main():
	num1, den1, num2, den2 = 0, 0, 0, 0
	x, f1, f2 = (), (), ()

	# num = int(input("Informe um valor para o numerador: "))
	# den = int(input("Informe um valor para o denominador: "))

	# x = f_criaFracao(num, den)
	# print(x)

	# x = f_simplifica(x)
	# print(x)

	print("Valores para a fracao 1:")
	num1 = int(input("Numerador: "))
	den1 = int(input("Denominador: "))

	print("Valores para a fracao 2:")
	num2 = int(input("Numerador: "))
	den2 = int(input("Denominador: "))

	f1 = (num1, den1)
	f2 = (num2, den2)
	x = f_soma(f1, f2)

	# x = f_simplifica(f1)

	print(x)

	return 0
#fim main

if __name__ == '__main__':
	main()
#fim if
