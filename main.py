from tabuleiro import Tabuleiro
from estado import Estado
import random

def main():
    tabuleiroInicial = Tabuleiro()
    pos_i = random.randint(0,2)
    pos_c = random.randint(0,2)
    tabuleiroInicial.board[pos_i][pos_c] = 'X'
    estadoinicial = Estado(tabuleiroInicial, None, 0, 'Max')
    estadoinicial.tabuleiro.imprimetabuleiro()

if __name__ == '__main__':
    main()