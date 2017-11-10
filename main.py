from tabuleiro import Tabuleiro
from estado import Estado
import random

def imprime_arvore(estado):
	tab = ""
	for n in range(0,estado.nivel):
		tab = str(tab+"\t")
	

	if( len(estado.listaDeFilhos) == 0 ):
		print(tab+"[ut:" + str(estado.utilidade )+ " nv:" + str(estado.nivel) + " tn:" + estado.turn+"]")
	else:
		for e in estado.listaDeFilhos:
			print(tab+"[ut:"+ str(estado.utilidade)+ " nv:" + str(estado.nivel) + " tn:" + estado.turn+"]")

		for e in estado.listaDeFilhos:
			imprime_arvore(e)
		

def gera_arvore(estado):
	
	filhos = estado.possiveisJogadas()

	if( len(filhos) == 0 ):
		return 1

	numeroEstados = 0

	for filho in estado.listaDeFilhos:
		numeroEstados = numeroEstados + gera_arvore(filho)

	return numeroEstados



def main():
	tabuleiroInicial = Tabuleiro()
	pos_i = random.randint(0,2)
	pos_c = random.randint(0,2)
	tabuleiroInicial.board[pos_i][pos_c] = 'X'

	pos_i = random.randint(0,2)
	pos_c = random.randint(0,2)
	tabuleiroInicial.board[pos_i][pos_c] = 'O'

	estadoinicial = Estado(tabuleiroInicial, None, 0, 'Min')
	

	numeroEstados = gera_arvore(estadoinicial)
	#imprime_arvore(estadoinicial)
	print(numeroEstados)
	estadoinicial.tabuleiro.imprimetabuleiro()

	while(estadoinicial.verificaEstadoFinal() == False):
		print("Vez de "+estadoinicial.turn+"\nResultado:")

		for filho in estadoinicial.listaDeFilhos:

			if(estadoinicial.turn == 'Min' and filho.utilidade == -1):
				estadoinicial = filho
				
			if(estadoinicial.turn == 'Max' and filho.utilidade == 1):
				estadoinicial = filho

			estadoinicial.tabuleiro.imprimetabuleiro()

	

if __name__ == '__main__':
    main()