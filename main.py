import pygame as pg
import random

from mapa import Mapa, Mapa_Pathfinding, Nodo, TIPOSTERRENO, adcionar_terreno
from ai import AI
from entidade import Entidade
from sprite import SPRITESIZE, VELOCIDADE
import menus
##MEU PROGRAMINHA PRA RODAR MAGO

pg.init()
ck = pg.time.Clock()
rodando = True
VERSAO = "v0.0.1"

FPS = 10 #Frames por segundo
SCREENSIZE = (25*SPRITESIZE,20*SPRITESIZE) #Tamanho da tela em Pixels

tela = pg.display.set_mode(SCREENSIZE)
pg.display.set_caption("Mage Player"+ VERSAO)
icone = pg.image.load("Recursos/dummy.png")
pg.display.set_icon(icone)
fonte = pg.font.SysFont('arial',16)

adcionar_terreno("dummy")
adcionar_terreno("Parede")
adcionar_terreno("Calçada")
adcionar_terreno("Chão Batido")

mapa = Mapa(25,20,Mapa_Pathfinding(25,20))

selecionado = None
rendermenu = False

mapa.criar_entidade(random.randint(0, mapa.largura),random.randint(0,mapa.altura),"Birola","Recursos/Personagem.png","Mago",((2,4,3),(3,1,3),(1,1,4)),((1,3,2,3,1,0,0),(0,0,3,2,1,1,2),(1,0,0,1,2,0,0)))
menu = menus.Menu(("Disgraça","Disgrama","DISGRAÇLASLSEJKASOZASA","Zero"))

pospix = 0
pospiy = 0
while rodando:
    for evento in pg.event.get():
        if evento.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            click = pg.mouse.get_pressed()
            posx = int(pos[0]/SPRITESIZE)
            posy = int(pos[1]/SPRITESIZE)
            if evento.button == pg.BUTTON_LEFT:
                pospix = pos[0]
                pospiy = pos[1]
                rendermenu = True
                #if selecionado != None:
                    #selecionado.AI.acharCaminho(selecionado.AI.get_nodo(selecionado.x,selecionado.y),selecionado.AI.get_nodo(posx,posy),tela)
            #elif evento.button == pg.BUTTON_RIGHT:
                #selecionado = selecionar(posx,posy,mapa,selecionado)
    tela.fill((255,255,255))
    mapa.render(tela)

    for entidade in mapa.entidades:
        entidade.atualizar(mapa)
        entidade.render(tela)
    #if selecionado != None:
        #tela.blit(fonte.render("Selecionado:"+selecionado.nome,True,(0,0,0)),(0,0))

    if rendermenu == True:
        menu.render(tela,pospix,pospiy,fonte)

    pg.display.update()
    ck.tick(FPS)

pg.quit()