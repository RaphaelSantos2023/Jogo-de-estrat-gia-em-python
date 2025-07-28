from model.Meteriais.planta import Arvore, Macieira
from model.Meteriais.Cenario import Pedregulho
from model.Meteriais.comida import Pescado,cultivo_trigo
from model.Meteriais.material import Terra
from model.Meteriais.construcao import Plantacao, Armazem_Comida
from model.Estoque.estoque import Estoque

from colorama import Fore, Style, init
import random

tamanho = 30

class Profissao:
  def __init__(self,nome,simbolo):
      self.nome = nome
      self.simbolo =  simbolo
      self.reino = None
  
  def movimentar(self, humano, reino, mapa):
        alvo = self.encontrar_mais_proximo(humano, mapa, self.simbolo.simbolo)
        ax, ay = alvo
        self.reino = reino
        if ax != None and ay != None:
            print(f"{humano.nome} está se movendo {humano.x},{humano.y} para {ax},{ay}")
        
        if humano.intencao == "Area":
            self.mover_dentro_area(humano, mapa,ax, ay,humano.max_x,humano.min_x,humano.max_y,humano.min_y)
        else:
            self.mover_especifico(humano, mapa,alvo)        

  def trabalhar(self,mapa,ax,ay,humano):
      mapa[ax][ay] = '-'
      humano.inventario.append(self.simbolo.Material)
      
  def mover_especifico(self,humano, mapa,alvo):
      ax, ay = alvo
      print(f"Indo para {ax},{ay}")
      if ax != None and ay != None:
          
          # Se já está no alvo
          if humano.x == ax and humano.y == ay:
              print("Achou")
              self.acao(mapa, humano,ax,ay)

          else:
              # Move em direção ao alvo
              if humano.x < ax:
                  humano.x += 1
              elif humano.x > ax:
                  humano.x -= 1

              if humano.y < ay:
                  humano.y += 1
              elif humano.y > ay:
                  humano.y -= 1
      else:
          print("Não encontrou")
          humano.acao_momento[0] = "Socializar"

  def mover_dentro_area(self,humano, mapa,ax, ay,max_x,min_x,max_y,min_y):
    if ax != None and ay != None:
        self.Acoes_(mapa,ax,ay,max_x,min_x,max_y,min_y,humano)
    else:
        humano.acao_momento.pop(0)
        if humano.inventario != []:
            humano.acao_momento.append("Guardar")
        else:
            humano.acao_momento.append("Socializar")

  def Acoes_(self,mapa,ax,ay,max_x,min_x,max_y,min_y,humano):
        if humano.x == ax and humano.y == ay:
            self.trabalhar(mapa,ax,ay,humano)
        else:
            self.Movimento_(ax,ay,max_x,min_x,max_y,min_y,humano)
        
  def Movimento_(self,ax,ay,max_x,min_x,max_y,min_y,humano):
        if humano.x < ax and humano.x < max_x:
            humano.x += 1
        elif humano.x > ax and humano.x > min_x:
            humano.x -= 1

        if humano.y < ay and humano.y < max_y:
            humano.y += 1
        elif humano.y > ay and humano.y > min_y:
            humano.y -= 1
    
  def encontrar_mais_proximo(self, humano, mapa, simbolos):
    menor_dist = float("inf")
    alvo = (None,None)
    if humano.intencao == "Area":
        for i in range(len(mapa)):
            for j in range(len(mapa[0])):
                if mapa[i][j] in simbolos and i>=humano.min_x and i<=humano.max_x and j>=humano.min_y and j<=humano.max_y:
                    dist = abs(humano.x - i) + abs(humano.y - j)
                    if dist < menor_dist:
                        menor_dist = dist
                        alvo = (i, j)
    else:
        for i in range(len(mapa)):
            for j in range(len(mapa[0])):
                if mapa[i][j] in simbolos:
                    dist = abs(humano.x - i) + abs(humano.y - j)
                    if dist < menor_dist:
                        menor_dist = dist
                        alvo = (i, j)
    return alvo

  def acao(self, mapa, humano,ax,ay):
    mapa[ax][ay] = '-'
    humano.inventario.append(self.simbolo.Material)
    humano.acao_momento.pop(0)
    humano.acao_momento.append("Guardar")

class Lenhador(Profissao):
  def __init__(self):
      super().__init__("Lenhador",Arvore(0,0))

class Pescador(Profissao):
    def __init__(self):
        super().__init__("Pescador",Pescado())

    def Acoes_(self,mapa,ax,ay,max_x,min_x,max_y,min_y,humano):
        if humano.x == ax and humano.y == ay:
            quantidade = random.randint(1,10)
            for i in range(quantidade):
                humano.inventario.append(self.simbolo)
            
            humano.acao_momento.pop(0)
            humano.acao_momento.append("Guardar")
        else:
            self.Movimento_(ax,ay,max_x,min_x,max_y,min_y,humano)
    def acao(self, mapa, humano,ax,ay):
        quantidade = random.randint(1,10)
        for i in range(quantidade):
            humano.inventario.append(self.simbolo)
            
            humano.acao_momento.pop(0)
            humano.acao_momento.append("Guardar")


class Fazendeiro(Profissao):
  def __init__(self):
      super().__init__("Fazendeiro",Plantacao(cultivo_trigo(),0))

  def Acoes_(self,mapa,ax,ay,max_x,min_x,max_y,min_y,humano):
    if humano.x == ax and humano.y == ay:
        for i in range(min_x,max_x+1):
            for j in range(min_y,max_y+1):
                mapa[i][j] = f"{Fore.YELLOW}_{Style.RESET_ALL}"
                humano.acao_momento.pop(0)
                humano.acao_momento.append("Socializar")
    else:
        self.Movimento_(ax,ay,max_x,min_x,max_y,min_y,humano)

class Minerador(Profissao):
  def __init__(self):
      super().__init__("Minerador",Pedregulho(0,0))
      self.estabelecimento = f"{Fore.LIGHTBLACK_EX}M{Style.RESET_ALL}"

class Taverneiro(Profissao):
    def __init__(self):
        super().__init__("Taverneiro",Armazem_Comida(0,0,Terra()))
    
    def trabalhar(self, mapa, ax, ay, humano):
        for construcao in self.reino.construcoes:
            if construcao.x == ax and construcao.y == ay:
                for item in construcao.inventario:
                    if item.quantidade > 1:
                        metade = item.quantidade // 2
                        item.quantidade -= metade

                        # Verifica se o humano já tem esse item no inventário
                        encontrou = False
                        for inv_item in humano.inventario:
                            if inv_item["Nome"] == item.nome:
                                inv_item["Quantidade"] += metade
                                encontrou = True
                                break
                        if not encontrou:
                            humano.inventario.append({
                                "Nome": item.nome,
                                "Quantidade": metade
                            })
