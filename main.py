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
	pos_i_max = random.randint(0,2)
	pos_c_max = random.randint(0,2)
	tabuleiroInicial.board[pos_i_max][pos_c_max] = 'X'

	pos_i_min = random.randint(0,2)
	pos_c_min = random.randint(0,2)

	while(pos_c_min == pos_c_max and pos_i_min == pos_i_max):
		pos_i_min = random.randint(0,2)
		pos_c_min = random.randint(0,2)	
	
	tabuleiroInicial.board[pos_i_min][pos_c_min] = 'O'

	estadoinicial = Estado(tabuleiroInicial, None, 0, 'Min')
	 
	numeroEstados = gera_arvore(estadoinicial)
	print(numeroEstados)

	estadoinicial.tabuleiro.imprimetabuleiro()

	print(estadoinicial.verificaEstadoFinal())
	while(estadoinicial.verificaEstadoFinal() == False):
		if(estadoinicial.turn == 'Min'):
			estadoinicial.listaDeFilhos.sort(key=lambda x: x.utilidade, reverse=True)
			print("Vez de Max\nResultado:")
		else:
			estadoinicial.listaDeFilhos.sort(key=lambda x: x.utilidade, reverse=False)
			print("Vez de Min\nResultado:")


		for i in estadoinicial.listaDeFilhos:
			print(i.utilidade)



		for filho in estadoinicial.listaDeFilhos:
			

			if(estadoinicial.turn == 'Max' and filho.utilidade <= 0):
				estadoinicial = filho
				break
					
			if(estadoinicial.turn == 'Min' and filho.utilidade >= 0):
				estadoinicial = filho
				break

		estadoinicial.tabuleiro.imprimetabuleiro()

		
	

if __name__ == '__main__':
    main()