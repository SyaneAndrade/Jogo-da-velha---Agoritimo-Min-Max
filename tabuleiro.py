#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Classe que representa o tabuleiro do Jogo da Velha
"""
class Tabuleiro(object):
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def imprimetabuleiro(self):
        print('\n'.join([''.join(['{:3}'.format(col) for col in linha]) for linha in self.board]))
        print()


def main():
    tabuleiro = Tabuleiro()
    tabuleiro.imprimetabuleiro()

if __name__ == '__main__':
    main()

