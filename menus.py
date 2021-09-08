import pygame as pg

class Menu:
    def __init__(self,opcoes):
        self.opcoes = opcoes
        maior = 0
        for opcao in opcoes:
            if len(opcao) > maior:
                maior = len(opcao)
        self.altura = len(opcoes)*16
        self.largura = maior*16
    def render(self,tela,posx,posy,fonte):
        menu = pg.rect.Rect(posx,posy,self.largura,self.altura)
        pg.draw.rect(tela,(50,50,70,15),menu)
        loops = 0
        for opcao in self.opcoes:
            tela.blit(fonte.render(opcao,True,(0,0,0)),(menu[0],menu[1]+loops))
            loops += 1

    def atualizar(self):
        pass
