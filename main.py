import pygame as pg
import random

from mapa import Mapa, Mapa_Pathfinding, Nodo, TIPOSTERRENO
from ai import AI
from entidade import Entidade

##MEU PROGRAMINHA PRA RODAR MAGO

pg.init()

rodando = True

VERSAO = "v0.0.1"

FPS = 10
VELOCIDADE = 8

SPRITESIZE = 32
SCREENSIZE = (25*SPRITESIZE,20*SPRITESIZE)

tela = pg.display.set_mode(SCREENSIZE)
pg.display.set_caption("Mage Player"+ VERSAO)
icone = pg.image.load("Recursos/dummy.png")
pg.display.set_icon(icone)


mapa = Mapa(25,20)
mapa_Pathfinding = Mapa_Pathfinding(25,20)
modelo = Entidade(5,5,"Recursos/Personagem.png",mapa_Pathfinding)
novoModelo = Entidade(6,6,"Recursos/Personagem.png",mapa_Pathfinding)
modelo.AI.mapa = mapa_Pathfinding
novoModelo.AI.mapa = mapa_Pathfinding
novoModelo.nome = "Achatado"
modelo.nome = "Modelor"
ck = pg.time.Clock()
fonte = pg.font.SysFont('arial',16)
first = True

entidades = []
entidades.append(modelo)
entidades.append(novoModelo)
for x in range(20,30):
    mapa.tiles[x].set_sprite("Parede")
    mapa_Pathfinding.nodos[x].obstaculo = True

mapa.get_tile(5,5).entidade = modelo

selecionado = None

def selecionar(x,y,mapa,selecionado):
    if selecionado != None and mapa.get_entidade(x,y) == selecionado:
        selecionado = None
        return True
    if selecionado == None and mapa.tem_entidade(x,y) == True:
        return mapa.get_entidade(x,y)

while rodando:
    for evento in pg.event.get():
        if evento.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            click = pg.mouse.get_pressed()
            posx = int(pos[0]/SPRITESIZE)
            posy = int(pos[1]/SPRITESIZE)

            if evento.button == pg.BUTTON_LEFT:
                if selecionado != None:
                    selecionado.AI.acharCaminho(selecionado.AI.get_nodo(selecionado.x,selecionado.y),selecionado.AI.get_nodo(posx,posy),tela)
            elif evento.button == pg.BUTTON_RIGHT:
                selecionado = selecionar(posx,posy,mapa,selecionado)
    tela.fill((255,255,255))
    mapa.render(tela)

    for entidade in entidades:
        entidade.atualizar(mapa)
        entidade.render(tela)
    if selecionado != None:
        tela.blit(fonte.render("Selecionado:"+selecionado.nome,True,(0,0,0)),(0,0))
    pg.display.update()
    ck.tick(FPS)
    if first:
        first = False
        pg.time.wait(1000)

pg.quit()