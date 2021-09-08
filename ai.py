import pygame as pg
import mapa
import entidade
import math


class AI:
    def __init__(self, mapa, si):
          self.mapa = mapa
          self.caminho = []
          self.si = si#Um ponteiro à entidade que representa essa AI
     
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

    def acharCaminho(self, inicio, objetivo,tela):
        
        # Loop do Pathfinding:
        # 1. reseta todos os nodos, limpa as listas aberta e fechada
        # 2. insere o nodo inicial na lista aberta e define ele como atual
        # 3. Inicia o loop:processa o nodo atual , tirando-o da lista aberta e colocando na lista fechada. 
        # Todos os vizinhos do nodo inicial são inseridos na lista aberta
        # 4. Reorganize a lista aberta de forma crescente baseado na variavel F; O nodo com o menor F agora é o atual;
        # 5. Repita o passo 3 até que a lista aberta fique vazia(significa que o caminho não foi encontrado) 
        # OU até que o nodo atual seja == ao nodo objetivo
        # 6. Se o objetivo for encontrado, trace o caminho de volta através do nodo pai do objetivo, 
        # repetindo isso até formar o caminho do inicio ao objetivo
        # 7. Retorne um vetor revertido com os nodos que compoem o caminho

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
               
    def calcularG(self,nodo):
        if nodo.x != nodo.pai.x and nodo.y != nodo.pai.y:
            return nodo.pai.g+14
        else:
            return nodo.pai.g +10
          
    def calcularH(self, atual,objetivo):
        dx = atual.x - objetivo.x
        dy = atual.y - objetivo.y
        distancia = int(math.sqrt((dx*dx)+(dy*dy)))
        return distancia*10
     
    def calcularF(self, nodo):
        return nodo.g+nodo.h

