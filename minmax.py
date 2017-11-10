#!/usr/bin/python
# -*- coding: UTF-8 -*-

from estado import Estado

class MinMax(object):
    
    def minmaxDecision(estado):
        if (estado.verificaEstadoFinal()):
            return estado.utilidade
        listaFilhos = estado.getFilhos()
        v = 0
        if(estado.turn == 'Max'):
            v =int('-inf')
            for estadoFilho in listaFilhos:
                v = max(v, estadoFilho.utilidade)
        else:
            v = int('inf')
            for estadoFilho in listaFilhos:
                v = min(v, estadoFilho.utilidade)
        estado.utilidade = v


