import pygame as pg

TIPOSTERRENO = {"dummy":pg.image.load("Recursos/dummy.png"),
                "Calçada":pg.image.load("Recursos/Calcada.png"),
                "Chão Batido":pg.image.load("Recursos/Chão Batido.png"),
                "Parede":pg.image.load("Recursos/Parede.png")
                }

class Tile:
    def __init__(self,x=0,y=0,sprite="dummy"):
        #ARGUMENTOS POSICIONAIS
        self.x = x 
        self.y = y
        self.sprite = TIPOSTERRENO[sprite]
        self.entidade = None

    def __getitem__(self,key):
        pass

    def set_sprite(self,sprite="dummy"):
        self.sprite = TIPOSTERRENO[sprite]

    def render(self,tela,SPRITESIZE = 32):
        tela.blit(self.sprite,(self.x*SPRITESIZE,self.y*SPRITESIZE))

class Nodo(object):
    def __init__(self, x, y, obstaculo = False):
        #ARGUMENTOS POSICIONAIS
        self.x = x
        self.y = y
        self.obstaculo = obstaculo
        #VALORES PARA PATHFINDING
        self.f = 0
        self.g = 0
        self.h = 0
        self.vizinhos = []
        self.pai = None

    def __eq__(self, outro):
        if outro != None and outro.x == self.x and self.y == outro.y:
            return True
        else:
            return False

    def definirVizinhos(self, mapa):
        for x in range(self.x-1,self.x+2):
            for y in range(self.y-1,self.y+2):
                nodo = mapa.nodos[x+y*mapa.largura]
                if nodo.obstaculo == False and nodo.x != self.x and nodo.y != self.y:
                    self.vizinhos.append(nodo)

class Mapa(object):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.tiles = []
        
        for y in range(self.altura):
            for x in range(self.largura):
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

    def get_tile(self,x,y):
        return self.tiles[x+(y*self.largura)]

    def get_entidade(self,x,y):
        return self.get_tile(x,y).entidade

    def tem_entidade(self,x,y):
        if self.get_tile(x,y).entidade != None:
            return True
        else:
            return None
    def render(self, tela):
        for tile in self.tiles:
            tile.render(tela)


class Mapa_Pathfinding(object):
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura
        self.nodos = []          
        for y in range(altura):
            for x in range(largura):
                self.nodos.append(Nodo(x,y))
                print("Nodo:"+str(x+(y*largura))+"Pos:X="+str(x)+"/ Y="+str(y))

        for y in range(altura):
            for x in range(largura):
                nodo = self.nodos[x+(y*largura)]
                if y > 0:
                    nodo.vizinhos.append(self.nodos[x+((y-1)*largura)])
                    
                if y < self.altura-1:
                    nodo.vizinhos.append(self.nodos[x+((y+1)*largura)])
                    
                if x > 0:
                    nodo.vizinhos.append(self.nodos[(x-1)+(y*largura)])
                    
                if x < self.largura-1:
                    nodo.vizinhos.append(self.nodos[(x+1)+(y*largura)])
                    
"""                if y>0 and x > 0:
                    nodo.vizinhos.append(self.nodos[(x-1)+(y-1)*largura])
                         
                if y < self.altura-1 and x>0:
                    nodo.vizinhos.append(self.nodos[(x-1)+(y+1)*largura])
                         
                if x < self.largura-1 and y > 0:
                    nodo.vizinhos.append(self.nodos[(x+1)+(y-1)*largura])
                         
                if x < self.largura-1 and y < self.altura-1:
                    nodo.vizinhos.append(self.nodos[(x+1)+(y+1)*largura])    """  