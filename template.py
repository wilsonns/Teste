import pygame as pg
import math
import random

###
class Mortal:
    def __init__(self,atributos=((1,1,1),(1,1,1),(1,1,1)),habilidades=((0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))):
        self.ancoras = []
        self.atributos = {"Mentais":{"Inteligência":atributos[0][0],
                                     "Raciocínio":atributos[0][1],
                                     "Perseverança":atributos[0][2]},
                          "Fisicos": {"Força":atributos[1][0],
                                      "Destreza":atributos[1][1],
                                      "Vigor":atributos[1][2]},
                          "Sociais":{"Presença":atributos[2][0],
                                     "Manipulação":atributos[2][1],
                                     "Autocontrole":atributos[2][2]}}
        
        self.habilidades = {"Mentais": {"Ciências":habilidades[0][0],
                                      "Computação":habilidades[0][1],
                                      "Erudição":habilidades[0][2],
                                      "Investigação":habilidades[0][3],
                                      "Medicina":habilidades[0][4],
                                      "Ocultismo":habilidades[0][5],
                                      "Ofícios":habilidades[0][6],
                                      "Política":habilidades[0][7]},
                            "Físicas": {"Armamento":habilidades[1][0],
                                      "Armas de Fogo":habilidades[1][1],
                                      "Briga":habilidades[1][2],
                                      "Condução":habilidades[1][3],
                                      "Esportes":habilidades[1][4],
                                      "Furto":habilidades[1][5],
                                      "Furtividade":habilidades[1][6],
                                      "Sobrevivência":habilidades[1][7]},
                          "Sociais": {"Empatia":habilidades[2][0],
                                      "Expressão":habilidades[2][1],
                                      "Intimidação":habilidades[2][2],
                                      "Manha":habilidades[2][3],
                                      "Persuasão":habilidades[2][4],
                                      "Socialização":habilidades[2][5],
                                      "Subterfúgio":habilidades[2][6],
                                      "Trato com Animais":habilidades[2][7]}}
        self.vantagens = []
        self.aspiracoes = []
        self.moralidade = 0
        defa = 0
        if self.atributos["Fisicos"]["Destreza"] > self.atributos["Mentais"]["Raciocínio"]:
            defa = self.atributos["Mentais"]["Raciocínio"]
        else:
            defa = self.atributos["Fisicos"]["Destreza"]
        self.derivados = {"Defesa":defa+self.habilidades["Físicas"]["Esportes"],
                          "Deslocamento":self.atributos["Fisicos"]["Destreza"]+self.atributos["Fisicos"]["Força"]+5, 
                          "Tamanho":5,
                          "Blindagem":(0,0),
                          "Iniciativa":0
                          }
        self.moralidadeSt = "Integridade"
        self.condicoes = []
        self.inclinacoes = []
        self.vitalidade = {"Máximo":5,
                           "Contundente":0,
                           "Letal":0,
                           "Agravado":0}
        self.FdV = {"Máximo":self.atributos["Mentais"]["Perseverança"]+self.atributos["Sociais"]["Autocontrole"],
                    "Atual":2}
        
    def set_atributo(self,atributo, valor):
        for categoria, atrib in self.atributos.items():
            for atribut, val in self.atributos[categoria].items():
                if atribut == atributo:
                    self.atributos[categoria][atribut] = valor

    
    def set_habilidade(self,habilidade, valor):
        for categoria,habil in self.habilidades.items():
            for habili, val in self.habilidades[categoria].items():
                if habili == habilidade:
                    self.habilidades[categoria][habili] = valor


    ##########COMBATE########################
    def tomar_dano(self,dano):
       self.vitalidade["Contundente"] += dano[0]
       self.vitalidade["Letal"] += dano[1]
       self.vitalidade["Agravado"] += dano[2]

class Mago(Mortal):
    def __init__(self,senda,ordem, atributos = ((1,1,1),(1,1,1),(1,1,1)), habilidades=((0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))):
        super().__init__(atributos,habilidades)
        self.senda = senda
        self.ordem = ordem
        self.combustivel = {"Máximo":10,
                     "Atual":10}
        self.combustivelSt = "Mana"
        self.potenciaSobrenatural = 0
        self.potenciaSobrenaturalSt = "Gnose"
        self.moralidadeSt = "Sabedoria"
        self.arcanos = {"Espaço":["Comum",0],
                        "Espírito":["Comum",0],
                        "Forças":["Comum",0],
                        "Matéria":["Comum",0],
                        "Mente":["Comum",0],
                        "Morte":["Comum",0],
                        "Primórdio":["Comum",0],
                        "Sorte":["Comum",0],
                        "Tempo":["Comum",0],
                        "Vida":["Comum",0]}
        self.obsessoes = []

    def lancar_feitico(self):
        print("Lançou um feitiço, ou melhor, lançou a braba")