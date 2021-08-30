import pygame as pg
from mapa import Mapa_Pathfinding, Nodo
import entidade
import math


class AI:
    def __init__(self, mapa, si:entidade.Entidade):
          self.mapa = mapa
          self.caminho = []
          self.si = si
     
    def mover(self, dx:int, dy:int,mapax):
        if self.mapa.nodos[dx+(dy*self.mapa.largura)].obstaculo == False:
            self.si.mover(dx,dy,mapax)

    def get_nodo(self, x:int, y:int):
        return self.mapa.nodos[x+(y*self.mapa.largura)]

    def atualizar(self,mapax):
        if len(self.caminho) > 0:
            proximo = self.caminho[0]
            self.mover(proximo.x,proximo.y, mapax)
            if self.si.x == proximo.x and self.si.y == proximo.y:
                self.caminho.pop(0)

    def acharCaminho(self, inicio:Nodo, objetivo:Nodo,tela):
        aberta = []
        aberta.append(inicio)
        fechada = []
        atual = inicio

        while len(aberta) > 0:
            atual = aberta[0]

            fechada.append(atual)
            aberta.remove(atual)
               
            if atual == objetivo:
                    caminho = []
                    nodo_atual = objetivo
                    while nodo_atual != inicio:
                        caminho.append(nodo_atual)
                        nodo_atual = nodo_atual.pai
                              
                    caminho.append(atual)
                    caminho.reverse()
                    caminho.pop(0)
                    self.caminho = caminho

                    #caminhoreverso = caminho
                    #caminhoreverso.reverse()
                    #for nodo in caminhoreverso:
                            #pg.draw.line(tela,(0,0,255),((nodo.x*32)+16,(nodo.y*32)+16),((nodo.pai.x*32)+16,(nodo.pai.y*32)+16),2)
                            #pg.display.flip()
                            
                    for y in range(self.mapa.altura):
                        for x in range(self.mapa.largura):
                            tile = self.mapa.nodos[x+(y*self.mapa.largura)]
                            tile.g = 0
                            tile.h = 0
                            tile.f = 0
                            tile.pai = None

                    
                    return True
                                   
            for vizinho in atual.vizinhos:
                if vizinho.obstaculo == False and vizinho not in fechada and vizinho in aberta:
                    if vizinho.pai != None and vizinho.pai.g > self.calcularG(atual):
                        vizinho.pai = atual
                        vizinho.g = self.calcularG(vizinho)
                        vizinho.h = self.calcularH(vizinho, objetivo)
                        vizinho.f = self.calcularF(vizinho)
                elif vizinho.obstaculo == False and vizinho not in fechada and vizinho not in aberta:
                    vizinho.pai = atual
                    vizinho.g = self.calcularG(vizinho)
                    vizinho.h = self.calcularH(vizinho, objetivo)
                    vizinho.f = self.calcularF(vizinho)
                    aberta.append(vizinho)

                              
            aberta.sort(key=lambda x:x.f)
            
        for y in range(self.mapa.altura):
            for x in range(self.mapa.largura):
                tile = self.mapa.nodos[x+(y*self.mapa.largura)]
                tile.g = 0
                tile.h = 0
                tile.f = 0
                tile.pai = None

        return False               
               
    def calcularG(self,nodo:Nodo):
        if nodo.x != nodo.pai.x and nodo.y != nodo.pai.y:
            return nodo.pai.g+14
        else:
            return nodo.pai.g +10
          
    def calcularH(self, atual:Nodo,objetivo:Nodo):
        dx = atual.x - objetivo.x
        dy = atual.y - objetivo.y
        distancia = int(math.sqrt((dx*dx)+(dy*dy)))
        return distancia*10
     
    def calcularF(self, nodo:Nodo):
        return nodo.g+nodo.h

