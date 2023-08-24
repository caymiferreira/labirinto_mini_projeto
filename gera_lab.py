from random import randint

livre = ' '
ocupado = '#'
parede  = '#'

linhas = 6
colunas = 10

comeca = (1,0)
termina = (linhas-2,colunas-1)

def gera_lab(m=6,n=10):
	lab = [([parede]*n)]
	for i in range(1,m-1):
		linha = [livre] * n
		for j in range(n):
			if randint(0,7) in [0,1]:
				linha[j] = ocupado
			if j in [0,n-1]:
				linha[j] = parede
		lab.append(linha)
	lab.append([parede]*n)
	lab[comeca[0]][comeca[1]] = livre
	lab[termina[0]][termina[1]] = livre
	return lab

def print_lab(lab):
	for i in lab:
		print("".join(i))

if __name__ == '__main__':
	l = gera_lab()
	print_lab(l)
