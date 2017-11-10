#!/usr/bin/python
# -*- coding: UTF-8 -*-

import copy
from tabuleiro import Tabuleiro
"""
Classe que representa o estado
do Jogo da Velha
"""
class Estado(object):
    listaDeFilhos = []
    def __init__(self, tabuleiro, pai, nivel, turn):
        self.tabuleiro = tabuleiro
        self.pai = pai
        self.nivel = nivel
        self.utilidade = 0
        self.turn = turn
    
    """
    Method: vitoriaJogador
    Parameters: [pos]
    verifica quais dos jogadores ganharam o jogo se Min ou se Max
    """
    def vitoriaJogador(self, pos):
        if(pos == 'X'):
            self.utilidade = 1
        if(pos == 'O'):
            self.utilidade = -1

    """
    Method: verificaColuna
    Parameters: [col]
    verifica se existe um jogo ganho nas colunas do tabuleiro
    """
    def verificaColuna(self, col):
        pos = self.tabuleiro.board[0][col]
        afirmacao = False
        for linha in range(1,3):
            if(pos == self.tabuleiro.board[linha][col] and pos != '-'):
                afirmacao = True
            else:
                afirmacao = False
                break
        if afirmacao:
            self.vitoriaJogador(self.tabuleiro.board[0][col])
        return afirmacao

    """
    Method: verificaLinha
    Parameters: [linha]
    verifica se existe um jogo ganho nas linhas do tabuleiro
    """
    def verificaLinha(self, linha):
        pos = self.tabuleiro.board[linha][0]
        afirmacao = False
        for col in range(1,3):
            if(pos == self.tabuleiro.board[linha][col] and pos!='-'):
                afirmacao = True
            else:
                afirmacao = False
                break
        if afirmacao:
            self.vitoriaJogador(self.tabuleiro.board[linha][0])
        return afirmacao

    """
    Method: verificaDiagonal
    Parameters: []
    verifica se existe um jogo ganho nas diagonais do tabuleiro
    """
    def verificaDiagonal(self):
        if(self.tabuleiro.board[1][1] == '-'):
            return False
        if(self.tabuleiro.board[0][0] == self.tabuleiro.board[1][1] == self.tabuleiro.board[2][2]):
            self.vitoriaJogador(self.tabuleiro.board[0][0])
            return True
        if(self.tabuleiro.board[2][0] == self.tabuleiro.board[1][1] == self.tabuleiro.board[0][2]):
            self.vitoriaJogador(self.tabuleiro.board[1][1])
            return True
        return False

    """
    Method: verificaEmpate
    Parameters: []
    verifica se nenhum dos jogadores ganhou o game e o tabuleiro está completamente preenchido
    """
    def verificaEmpate(self):
        for linha in self.tabuleiro.board:
            for col in linha:
                if(col == '-'):
                    return False
        return True

    """
    Method: verificaEstadoFinal
    Parameters: []
    verifica se existe um jogo ganho do tabuleiro, utilizando os methodos verifica
    """
    def verificaEstadoFinal(self):
        if(self.verificaEmpate()):
            return True
        if(self.verificaColuna(0) or self.verificaColuna(1) or self.verificaColuna(2)):
            return True
        if(self.verificaLinha(0) or self.verificaLinha(1) or self.verificaLinha(2)):
            return True
        if(self.verificaDiagonal()):
            return True
        return False
    """
    Method: verificaColuna
    Parameters: [col]
    verifica se existe um jogo ganho nas colunas do tabuleiro
    """
    def verificaColunaCV_1(self, col, s):
        pos = s
        afirmacao = False
        for linha in range(0,3):
            if(pos == self.tabuleiro.board[linha][col]):
                afirmacao = True
            else:
                if( self.tabuleiro.board[linha][col] != '-' != s):
                    afirmacao = False
                break
        if afirmacao:
            self.vitoriaJogador(self.tabuleiro.board[0][col])
        return afirmacao

    """
    Method: verificaLinha
    Parameters: [linha]
    verifica se existe um jogo ganho nas linhas do tabuleiro
    """
    def verificaLinhaCV_1(self, linha, s):
        pos = s
        afirmacao = False
        for col in range(0,3):
            if(pos == self.tabuleiro.board[linha][col]):
                afirmacao = True
            else:
                if( self.tabuleiro.board[linha][col] != '-' != s):
                    afirmacao = False
                break
        return afirmacao

    """
    Method: verificaDiagonal
    Parameters: []
    verifica se existe um jogo ganho nas diagonais do tabuleiro
    """
    def verificaDiagonalCV_1(self, s):

        if((self.tabuleiro.board[0][0] == self.tabuleiro.board[2][2] and self.tabuleiro.board[1][1] == '-') or ( self.tabuleiro.board[0][0] == self.tabuleiro.board[1][1] and self.tabuleiro.board[2][2] == '-')):
            return True
        if((self.tabuleiro.board[2][0] == self.tabuleiro.board[0][2] and self.tabuleiro.board[1][1] == '1') or (self.tabuleiro.board[2][0] == self.tabuleiro.board[1][1] and self.tabuleiro.board[0][2] == '-')):
            return True
        return False

    """
    Method: verificaColuna
    Parameters: [col]
    verifica se existe um jogo ganho nas colunas do tabuleiro
    """
    def verificaColunaComVar(self, col, s):
        pos = self.tabuleiro.board[0][col]
        afirmacao = False
        for linha in range(1,3):
            if(pos == self.tabuleiro.board[linha][col] and pos != '-'):
                afirmacao = True
            else:
                afirmacao = False
                break
        #if afirmacao:
         #   self.vitoriaJogador(self.tabuleiro.board[0][col])
        return afirmacao

    """
    Method: verificaLinha
    Parameters: [linha]
    verifica se existe um jogo ganho nas linhas do tabuleiro
    """
    def verificaLinhaComVar(self, linha, s):
        pos = self.tabuleiro.board[linha][0]
        afirmacao = False
        for col in range(1,3):
            if(pos == self.tabuleiro.board[linha][col] and pos!='-'):
                afirmacao = True
            else:
                afirmacao = False
                break
        #if afirmacao:
            #self.vitoriaJogador(self.tabuleiro.board[linha][0])
        return afirmacao

    """
    Method: verificaDiagonal
    Parameters: []
    verifica se existe um jogo ganho nas diagonais do tabuleiro
    """
    def verificaDiagonalComVar(self, s):
        if(self.tabuleiro.board[1][1] == '-'):
            return False
        if(self.tabuleiro.board[0][0] == self.tabuleiro.board[1][1] == self.tabuleiro.board[2][2]):
            #self.vitoriaJogador(self.tabuleiro.board[0][0])
            return True
        if(self.tabuleiro.board[2][0] == self.tabuleiro.board[1][1] == self.tabuleiro.board[0][2]):
            #self.vitoriaJogador(self.tabuleiro.board[1][1])
            return True
        return False

    """
    Method: verificaDistanciaFinal
    Parameters: []
    verifica se existe um jogo ganho do tabuleiro ou se esta quase, diferenciando por pontuacao
    """
    def verificaDistanciaFinal(self,s):
        if(self.verificaEmpate()):
            return 0
        if(self.verificaColunaComVar(0,s) or self.verificaColunaComVar(1,s) or self.verificaColunaComVar(2,s)):
            return 100
        if(self.verificaLinhaComVar(0,s) or self.verificaLinhaComVar(1,s) or self.verificaLinhaComVar(2,s)):
            return 100
        if(self.verificaDiagonalComVar(s)):
            return 100
        if(self.verificaColunaCV_1(0,s) or self.verificaColunaCV_1(1,s) or self.verificaColunaCV_1(2,s)):
            return 50
        if(self.verificaLinhaCV_1(0,s) or self.verificaLinhaCV_1(1,s) or self.verificaLinhaCV_1(2,s)):
            return 50
        if(self.verificaDiagonalCV_1(s)):
            return 50

        return 0


    """
    Method: posicaoValida
    Parameters: [pos]
    verifica se a posicao do tabuleiro pode ser marcada
    """
    def posicaoValida(self, pos):
        if(pos == '-'):
            return True
        return False

    """
    Method: possiveisJogadas
    Parameters: []
    return: Lista de Estados Possiveis
    gera todos os estados possiveis apartir do estado atual
    """
    def possiveisJogadas(self):
        estadonovospossiveis = []
        for linha in range(0, 3):
            for col in range(0, 3):
                if(self.posicaoValida(self.tabuleiro.board[linha][col])):
                    novotabuleiro = copy.deepcopy(self.tabuleiro)
                    turn = ''
                    if(self.turn == 'Max'):
                        turn = 'Min'
                        mark = 'O'
                        novotabuleiro.board[linha][col] = 'O'
                        
                    if(self.turn == 'Min'):
                        turn = 'Max'
                        mark = 'X'
                        novotabuleiro.board[linha][col] = 'X'
                        
                    pai = self
                    nivel = self.nivel + 1
                    novoestado  = Estado(novotabuleiro, pai, nivel, turn)
                    novoestado.utilidade = novoestado.verificaDistanciaFinal(mark)
                    if(mark == 'O'):
                        novoestado.utilidade = -(novoestado.utilidade)

                    estadonovospossiveis.append(novoestado)
        self.listaDeFilhos = estadonovospossiveis
        return estadonovospossiveis 
    
    """
    Method: getFilhos
    Parameters: []
    retorna a lista de filhos do estado se essa existe, esses filhos serão adcionados na geração da arvore
    """
    def getFilhos(self):
        return self.listaDeFilhos
"""
def main():
    tabuleiro = Tabuleiro()
    estadoinicial = Estado(tabuleiro, None, 0, 'Max')
    listaEsperada = estadoinicial.possiveisJogadas()

    for estado in listaEsperada:
        estado.tabuleiro.imprimetabuleiro()
    print(estadoinicial.verificaEstadoFinal())

if __name__ == '__main__':
    main()
                    
"""