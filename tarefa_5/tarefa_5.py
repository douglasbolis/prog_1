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

def f_simplifica(f):
	novaf, x = (), 0
	
	x = abs(f_mdc())
	novaf = f_criaFracao(f[0]//x, f[1]//x)
	
	return novaf
#fim funcao

def f_soma(f1, f2):
	n, d = 0, 0
	
	if (f1[1] == f2[1]):
		d = f1[1]
	else:
		d = f1[1]*f2[1]
	#fim if
	
	n = ((d//f1[1])*f1[0]) + (d//f2[1])*f2[0]))//d
	
	return (f_simplifica(f_criaFracao(n, d)))
#fim funcao

def f_subtracao():
	t = ()
	
	t = f_criaFracao(-f2[0], f2[1])	
	return (f_soma(f1, t))
#fim funcao

def f_multiplica(f1, f2):
	
	
#fim funcao
def main():
	num, den = 0, 0
	x = ()
	
	num = int(input("Informe um valor para o numerador: "))
	den = int(input("Informe um valor para o denominador: "))
	
	x = f_criaFracao(num, den)
	print(x)
	
	return 0
#fim main

if __name__ == '__main__':
	main()
#fim if
