import pygame as pg
import random
import ai
import template
from sprite import Animacao, SPRITESIZE, VELOCIDADE

class Entidade:
    def __init__(self,x,y,nome, sprite, mapa, temp, atributos, habilidades):
        self.nome = nome #O nome da entidade
        
        #Posição absoluta da Entidade
        self.x = x 
        self.y = y
        #Posição de desenho da entidade
        self.pixelX = self.x*SPRITESIZE
        self.pixelY = self.y*SPRITESIZE
        
        #Inteligencia artificial para movimentação e pathfinding
        self.AI = ai.AI(mapa,self)

        #template sobrenatural do personagem, que inclui atributosa e tudo mais
        if(temp == "Mago"):
            self.template = template.Mago(atributos,habilidades)
        else:
            self.template = template.Mortal(atributos,habilidades)
        #Añimação
        self.sprite = Animacao(sprite)
        self.direcao = self.sprite.direcao
        self.andando = False
        self.sprite.iter()        
        #0 = baixo
        #1 = direita
        #2 = esquerda
        #3 = cima
                
    def render(self,tela):
        tela.blit(self.sprite.atual,(self.pixelX,self.pixelY))
        #Função para desenhar a entidade na tela

    def mover(self,proximox,proximoy, mapa):
        if proximoy > self.y:
            self.direcao = 0
        if proximox > self.x:
            self.direcao = 1
        if proximox < self.x:
            self.direcao = 2
        if proximoy < self.y:
            self.direcao = 3
        #Define a direção do sprite

        mapa.get_tile(self.x,self.y).entidade = None #Tira o ponteiro pra entidade na tile atual

        if self.direcao == 0:
            self.pixelY += VELOCIDADE
            self.sprite.next(self.direcao)
        elif self.direcao == 1:
            self.pixelX += VELOCIDADE
            self.sprite.next(self.direcao)
        elif self.direcao == 2:
            self.pixelX -= VELOCIDADE
            self.sprite.next(self.direcao)
        elif self.direcao == 3:
            self.pixelY -= VELOCIDADE
            self.sprite.next(self.direcao)
            #Movimenta o sprite no eixo X ou Y uma quantidade de pixels igual à Velocidade e itera para o próximo sprite na folha

        if self.pixelX%SPRITESIZE == 0:
            self.x = int(self.pixelX/SPRITESIZE)
        
        if self.pixelY%SPRITESIZE == 0:
            self.y = int(self.pixelY/SPRITESIZE)
            #muda a posição absoluta da entidade apenas se o sprite tiver se movido inteiramente pra dentro daquele tile 
        mapa.get_tile(self.x,self.y).entidade = self#altera o ponteiro pra entidade na tile atual
        #Função que faz a movimentação do personagem    

    def atualizar(self,mapax):
        self.AI.atualizar(mapax)
        #Função que atualiza a IA do perosnagem
