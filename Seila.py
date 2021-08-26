import pygame as pg
import random

##MEU PROGRAMINHA PRA RODAR MAGO

pg.init()

rodando = True

VERSAO = "v0.0.1"

FPS = 12
VELOCIDADE = 8

SPRITESIZE = 32
SCREENSIZE = (25*SPRITESIZE,20*SPRITESIZE)
TIPOSTERRENO = {"dummy":pg.image.load("Recursos/dummy.png"),
                "Calçada":pg.image.load("Recursos/Calcada.png"),
                "Chão Batido":pg.image.load("Recursos/Chão Batido.png")
                }

tela = pg.display.set_mode(SCREENSIZE)
pg.display.set_caption("Mage Player"+ VERSAO)
icone = pg.image.load("Recursos/dummy.png")
pg.display.set_icon(icone)

class Tile:
    def __init__(self,x=0,y=0,sprite="dummy"):
        self.x = x
        self.y = y
        self.sprite = TIPOSTERRENO[sprite]
        self.entidade = None
    def render(self,tela):
        tela.blit(self.sprite,(self.x*SPRITESIZE,self.y*SPRITESIZE))

class Mapa:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.tiles = []
        for x in range(self.largura):
            for y in range(self.altura):
                #r = random.randint(1,3)
                r =1
                str = None
                if r == 1:
                    str = "Calçada"
                elif r == 2:
                    str = "Chão Batido"
                elif r == 3:
                    str = "dummy"
                self.tiles.append(Tile(x,y,str))

    def render(self, tela):
        for tile in self.tiles:
            tile.render(tela)

class Spritesheet(pg.sprite.Sprite):
    def __init__(self,arquivo):
        try:
            self.arquivo = pg.image.load(arquivo).convert()
            self.largura = int(self.arquivo.get_width()/SPRITESIZE)
            self.altura = int(self.arquivo.get_height()/SPRITESIZE)
        except pg.error as message:
            print("Não foi possivel abrir o arquivo:" + arquivo)
            raise SystemExit(message)
    
    def imagem_em(self, retangulo,colorKey = None):
        rect = pg.Rect(retangulo)
        rect.size = (31,31)

        imagem = pg.Surface(rect.size).convert()

        imagem.blit(self.arquivo,(0,0),rect)
        if colorKey is not None:
            if colorKey == -1:
                colorKey = imagem.get_at((0,0))
            imagem.set_colorkey(colorKey,pg.RLEACCEL)
                
        return imagem

    def imagens_em(self,retangulos,colorKey = None):
        imagens = []
        for retangulo in retangulos:
            imagens.append(self.imagem_em(retangulo,colorKey))
        return imagens
    
    def dividir_total(self,colorKey = None):
        imagens = []
        xinic = 0
        xfin = 0
        yinic = 0
        yfin = 0
        yprimeiro = True
        xprimeiro = True
        for y in range(self.altura):
            imagens.append([])
            if yprimeiro == True:
                yinic = 0
                yfin = yinic + SPRITESIZE-1
                yprimeiro = False
            else:
                yinic = yfin+1
                yfin = yinic + SPRITESIZE-1
            xprimeiro = True
            for x in range(self.largura):
                if xprimeiro == True:
                    xinic = 0
                    xfin = xinic + SPRITESIZE -1
                    xprimeiro = False
                else:
                    xinic = xfin + 1
                    xfin = xinic + SPRITESIZE-1
                imagens[y].append(self.imagem_em((xinic,yinic,xfin,yfin),colorKey))
        numero = 0
        for tira in imagens:
            for imagem in tira:
                numero += 1 
                pg.image.save(imagem,"Teste/Arquivo"+str(numero)+".png")
        return imagens

class Animacao:
    def __init__(self, arquivo):
        sheet = Spritesheet(arquivo)
        self.sheet = sheet.dividir_total(-1)
        self.altura = sheet.altura
        self.largura = sheet.largura
        self.atual = self.sheet[0][0]
        self.direcao = 0

    def iter(self):
        self.j = 0

    def next(self):
        if self.j >= self.altura-1:
            self.j = 0
        else:
            self.j += 1
        self.atual = self.sheet[self.direcao][self.j]
        

class Entidade:
    def __init__(self, sprite):
        self.x = 0
        self.y = 0
        self.pixelX = self.x*SPRITESIZE
        self.pixelY = self.y*SPRITESIZE
        self.sprite = Animacao(sprite)
        self.caminho = []
        self.direcao = self.sprite.direcao
        self.andando = False
        self.sprite.iter()
        #0 = baixo
        #1 = esquerda
        #2 = direita
        #3 = cima

    def render(self,tela):
        self.andar()
        tela.blit(self.sprite.atual,(self.pixelX,self.pixelY))


    def andar(self):
        if self.direcao == 0:
            self.pixelY += VELOCIDADE
            self.sprite.next()
        elif self.direcao == 1:
            self.pixelX -= VELOCIDADE
            self.sprite.next()
        elif self.direcao == 2:
            self.pixelX += VELOCIDADE
            self.sprite.next()
        elif self.direcao == 3:
            self.pixelY -= VELOCIDADE
            self.sprite.next()


    def atualizar(self):
        self.caminho

mapa = Mapa(25,20)
modelo = Entidade("Recursos/Personagem.png")
modelo.x = 10
modelo.y = 10

modelo.caminho.append((11,10))

ck = pg.time.Clock()
first = True

while rodando:

    
    tela.fill((255,255,255))

    mapa.render(tela)

    modelo.render(tela)
  
    pg.display.update()
    ck.tick(FPS)
    if first:
        first = False
        pg.time.wait(1000)

pg.quit()