import pygame as pg
import random

SPRITESIZE = 32
VELOCIDADE = 8

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
    def __init__(self, arquivo, colorKey = -1):
        sheet = Spritesheet(arquivo)
        self.sheet = sheet.dividir_total(colorKey)
        self.altura = sheet.altura
        self.largura = sheet.largura
        self.atual = self.sheet[0][0]
        self.direcao = 0

    def iter(self):
        self.j = 0

    def next(self,direcao):
        self.direcao = direcao
        if self.j >= self.altura-1:
            self.j = 0
        else:
            self.j += 1
        self.atual = self.sheet[self.direcao][self.j]
        

