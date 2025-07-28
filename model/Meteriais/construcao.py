from model.Estoque.estoque import Estoque

from model.Meteriais.material import (
    Terra,Pedra,Cobre,Estanho,Ferro,Níquel,Prata,Ouro,Platina,Titânio
)
from model.Meteriais.comida import Comida

from colorama import Fore, Style, init
import random

class Construcao:
  def __init__(self,nome,simbolo,tipo,material,vida,quantidadeP,x,y):
      self.nome = nome
      self.simbolo = simbolo
      self.tipo = tipo
      
      self.material = material
      self.materiais_postos = []

      self.inventario =[]
      
      self.vida = vida
      self.x = x
      self.y = y

      self.quantidadePMax = quantidadeP
      self.quantidadeP = quantidadeP
      self.n_pessoas = 0

      self.Demanda_Tempo = False

  def setValores(self,material,x,y):
      self.material = material
      self.x = x
      self.y = y
  
  def acao(self,item):
      self.inventario.append(item)
  
  def movimentar(self, humano, mapa):
    alvo = self.encontrar_mais_proximo()
    if alvo:
        ax, ay = alvo
        
        if humano.x < ax:
            humano.x += 1
        elif humano.x > ax:
            humano.x -= 1

        if humano.y < ay:
            humano.y += 1
        elif humano.y > ay:
            humano.y -= 1

        # Se chegou a construção
        if humano.x == ax and humano.y == ay:
            self.AoChegar(humano)

  def AoChegar(self,humano):
    humano.Dormir = "Dormindo"
    def habitar_Socializar(humano):
        humano.Dentro_estrutura = True
        self.inventario.append(humano)
        self.quantidadeP -= 1

    if self.tipo == "Armazem":
        for item in humano.inventario:
            self.addInventario(item)
        
        humano.iventario = []
        humano.acao_momento.pop(0)
        humano.acao_momento.append("Socializar")
        
    elif self.tipo == "Habitacional":
        if self.quantidadeP > 0:
            habitar_Socializar(humano)
            humano.Dormir = "Dormindo"
    elif self.tipo == "Socializar" or self.tipo == "Religioso":
        if self.quantidadeP > 0:
            habitar_Socializar(humano)
            match self.tipo:
                case "Socializar":
                    humano.necessidades["Diversão"] -=10
                case "Religioso":
                    humano.necessidades["Diversão"] -=10
    else:
        self.trabalho_acao(humano)
    
  def trabalho_acao(self,humano):
      humano.Dentro_estrutura = True
      self.inventario.append(humano)
      humano.profissao[0].trabalho(self.materiais)
    
  def addInventario(self,item):
      Tem = False
      for i in range(len(self.inventario)):
          if item.nome == self.inventario[i].nome.nome:
              self.inventario[i].quantidade += 1
              Tem = True

      if Tem == False:
          self.inventario.append(Estoque(item,1))
    
  def encontrar_mais_proximo(self):
    #menor_dist = float("inf")
    #alvo = None
    #for i in range(len(mapa)):
    #    for j in range(len(mapa[0])):
    #        if mapa[i][j] in simbolos:
    #            dist = abs(humano.x - i) + abs(humano.y - j)
    #            if dist < menor_dist:
    #                menor_dist = dist
    #                alvo = (i, j)
    
    #return alvo
    return (self.x,self.y)

  def Interior(self):
    text = ""
    if self.tipo == "Habitacional" or self.tipo == "Socializar" or self.tipo == "Religioso":
        text += "Pessoas:"
        for humano in self.inventario:
            text += f"\n-> {humano.nome}"
    elif self.tipo == "Armazem":
        text += "Inventario:"
        for i in range(len(self.inventario)):
            text += f"\n-> {self.inventario[i].nome.nome} - {self.inventario[i].quantidade}"
    
    return text
    
  def Descricao(self):
    dados = f"Nome: {self.nome} \nTipo: {self.tipo} \nVida: {self.vida}\n"
    interior = self.Interior()
    text =  dados + interior + "\n\n"
    text  += "-"*30
    return text

class Demanda_tempo(Construcao):
    def __init__(self,nome,simbolo,tipo,material,vida,quantidadeP,x,y,horas):
        super().__init__(nome,simbolo,tipo,material,vida,quantidadeP,x,y)
        self.Demanda_Tempo = True
        self.hora = horas
    
    def acao_tempo(self,reino,matriz,relogio,regiao):
        for pessoa in self.inventario:
            if pessoa.horas_dentro - relogio.horas == self.hora:
                pessoa.Dentro_estrutura = False
                self.inventario.remove(pessoa)
    
class Construcao_trabalho(Demanda_tempo):
    def __init__(self,nome,simbolo,material,vida,quantidadeP,x,y,horas):
        super().__init__(nome,simbolo, "Trabalho",material, vida, quantidadeP,x,y,horas)
        self.dia = 1
        self.profissao_requerida = ""
        self.material_feito = []
    
    def acao_tempo(self,reino,matriz,relogio,regiao):
        if relogio.hora == 6 or relogio.hora == 14:
            for cidadao in reino.cidadaos:
                if cidadao.profissos[0].nome == self.profissao_requerida:
                    self.movimentar(cidadao,matriz)
        
        
        if relogio.hora == 12 or relogio.hora == 18:
            self.coletar(regiao)
            for pessoa in self.inventario:
                pessoa.Dentro_estrutura = False
                pessoa.acao_momento[0] = "Guardar"
                self.inventario.remove(pessoa)
    
    def trabalho_acao(self,humano):
        humano.Dentro_estrutura = True
        self.inventario.append(humano)
    
    def coletar(self, regiao):
        return ""

class Mina(Construcao_trabalho):
    def __init__(self, x, y, Material):
        super().__init__("Mina", f"{Fore.LIGHTBLACK_EX}M{Style.RESET_ALL}",Material, 25, 10,x,y,5)
        self.dia = 1
        self.profissao_requerida = "Minerador"
        self.material_feito = [
            (Pedra(),     1),
            (Cobre(),     2),
            (Estanho(),   3),
            (Ferro(),     4),
            (Níquel(),    5),
            (Prata(),     6),
            (Ouro(),      7),
            (Platina(),   8),
            (Titânio(),   9)
        ]
    
    def coletar(self, regiao):
        nivel_sorte = regiao.riqueza_mineral

        for pessoa in self.inventario:
            quantidade = random.randint(1,5)
            pesos = []

            for material, raridade in self.minerios:
                base_peso = 1 / raridade
                boost = (nivel_sorte * (raridade ** 1.5)) * 0.01
                peso_final = base_peso + boost
                pesos.append(peso_final)
            
            minerio = random.choices([m[0] for m in self.minerios], weights=pesos, k=1)[0]
            pessoa.inventario.append(minerio)        

class Cabana(Construcao):
  def __init__(self, x, y, Material):
      super().__init__("Cabana", f"{Fore.LIGHTYELLOW_EX}C{Style.RESET_ALL}", "Habitacional",Material, 5, 2,x,y)

class Casa(Construcao):
  def __init__(self, x, y, Material):
      super().__init__("Casa", f"{Fore.RED}C{Style.RESET_ALL}", "Habitacional",Material, 10,4,x,y)

class Taverna(Demanda_tempo):
    def __init__(self, x, y, Material):
        super().__init__("Taverna", "B", "Socializar",Material, 10, 6,x,y,5)
        self.comida = []
    
    def acao_tempo(self,reino,matriz,relogio,regiao):
        for cidadao in reino.cidadaos:
            if len(cidadao.profissos) > 1:
                for profissao in cidadao.profissos:
                    if profissao.nome == "Taverneiro":
                        cidadao.acao_momento[0] = "Trabalhar"
                        break
    
    def trabalho_acao(self, humano):
        for item_humano in humano.inventario:
            encontrado = False
            for item_taverna in self.inventario:
                if item_taverna.nome == item_humano["Nome"]:
                    item_taverna.quantidade += item_humano["Quantidade"]
                    encontrado = True
                    break
            if not encontrado:
                self.inventario.append(Estoque(item_humano["Nome"],item_humano["Quantidade"]))

        humano.inventario = []
        humano.acao_momento.pop(0)
        humano.acao_momento.append("Socializar")

class Murro(Construcao):
  def __init__(self, x, y, Material):
      super().__init__("Murro de Pedra", "0", "Defesa", Material, 10, 0,x,y)

class Posto_Comercio(Construcao):
  def __init__(self, x, y, Material):
      super().__init__("Posto de comercio", f"{Fore.LIGHTYELLOW_EX}${Style.RESET_ALL}", "Defesa", Material, 10,0,x,y)

class Templo(Construcao):
    def __init__(self,x,y,Material):
        super().__init__(f"Templo", "Ã", "Religioso",Material, 20,0,x,y)
    
    def definir_deus(self,deus):
        self.Divindade = deus
        self.nome_individual = f"Templo de {deus.nome}"

    def AcaoDivina(self,id,alvo):
        self.Divindade.Acao(id,alvo)
    
    def ChecarBencaos(self):
        Text = "\nBençãos:"
        Text += f"\n{Fore.LIGHTGREEN_EX}1{Style.RESET_ALL}. {self.Divindade.Bencao_Descricao["Ordem"]}"
        Text += f"\n{Fore.LIGHTBLACK_EX}2{Style.RESET_ALL}. {self.Divindade.Bencao_Descricao["Neutro"]}"
        Text += f"\n{Fore.LIGHTMAGENTA_EX}3{Style.RESET_ALL}. {self.Divindade.Bencao_Descricao["Caos"]}"

        return Text
    
    def Descricao(self):
        dados = f"Nome: {self.nome} \nTipo: {self.tipo} \nVida: {self.vida}\n"
        interior = self.Interior()
        bencaos = self.ChecarBencaos()
        
        text =  dados + bencaos + interior + "\n"
        text  += "-"*30
        return text

class Armazem(Construcao):
    def __init__(self, x, y, Material):
        super().__init__("Armazem", f"{Fore.LIGHTYELLOW_EX}W{Style.RESET_ALL}", "Armazem", Material, 20, 0,x,y)
    
    def Interior(self):
        text = "Animais:"
        print(f"tamanho array: {len(self.inventario)}")
        for i in range(len(self.inventario)):
            quantidade_carne = self.inventario[i].nome.comida_quantidade * self.inventario[i].quantidade
            text += f"\n-> {self.inventario[i].nome.nome} - {self.inventario[i].quantidade} - Quantidade de carne: {quantidade_carne}"
        
        return text
    
class Armazem_materiais(Construcao):
    def __init__(self, x, y, Material):
        super().__init__("Armazem de materiais", f"{Fore.LIGHTYELLOW_EX}w{Style.RESET_ALL}", "Armazem", Material, 20, 0,x,y)

class Armazem_Comida(Construcao):
    def __init__(self, x, y, Material):
        super().__init__("Armazem de comida", f"{Fore.LIGHTYELLOW_EX}M{Style.RESET_ALL}", "Armazem", Material, 20, 0,x,y)
    
    def movimentar(self, humano, intensao,mapa):
        alvo = self.encontrar_mais_proximo()
        if alvo:
            ax, ay = alvo 
            #if ax != None and ay != None:
                #print(f"{humano.nome} está se movendo {humano.x},{humano.y} para {ax},{ay}")
            
            if humano.x < ax:
                humano.x += 1
            elif humano.x > ax:
                humano.x -= 1

            if humano.y < ay:
                humano.y += 1
            elif humano.y > ay:
                humano.y -= 1

            # Se chegou a construção
            if humano.x == ax and humano.y == ay:

                if intensao == "Guardar":
                    self.AoChegar(humano)
                else:
                    self.AoChegar_Comer(humano)
    
    def AoChegar_Comer(self, humano):
        if humano.fome < 80:
            comidas_disponiveis = [item for item in self.inventario if isinstance(item.nome, Comida) and item.quantidade > 0]
            if comidas_disponiveis:
                comida = random.choice(comidas_disponiveis)
                humano.Comer(comida.nome)
                comida.quantidade -= 1
                if humano.felicidade + 50 >= 100:
                    humano.felicidade = 100
                else:
                    humano.felicidade += 50
            else:
                humano.acao_momento[0] = "Socializar"
        else:
            humano.acao_momento[0] = "Socializar"

class Plantacao(Demanda_tempo):
    def __init__(self,tipo_cultivo,dia):
        super().__init__("Plantação", f"\033[38;5;94m_\033[0m", "Crescimento", Terra(), 10, 0,0,0,0)
        self.pronta = False
        self.dia = dia
        self.ultimo_dia = 0
        self.tipo_cultivo = tipo_cultivo

    def acao_tempo(self,reino,matriz,relogio,regiao):
        if (relogio.dia - self.dia) % self.tipo_cultivo.dias_para_colheita == 0 and self.ultimo_dia != relogio.dia:
            self.ultimo_dia = relogio.dia
            self.quantidade_comida = random.randint(5,20)
            
            for i in range(self.quantidade_comida):
                self.inventario.append(self.tipo_cultivo.resultado)
            
            for cidadao in reino.cidadaos:
                if cidadao.profissos[0].nome == "Fazendeiro":
                    cidadao.acao_momento[0] = "Colher"
                    self.pronta = True
                    break
    
    def trabalho_acao(self, humano):
        humano.inventario = self.inventario.copy()
        self.inventario = []
        self.quantidade_comida = random.randint(1,10)
        self.pronta = False
        humano.acao_momento.pop(0)
        humano.acao_momento.append("Guardar")
    
    def Descricao(self):
        dados = f"Nome: {self.nome} \nTipo: {self.tipo} \nVida: {self.vida}\n"
        calculo_dias = self.ultimo_dia + self.tipo_cultivo.dias_para_colheita
        dados +=  f"Dias de cultivo: {self.tipo_cultivo.dias_para_colheita}\nCultivo: {self.tipo_cultivo.resultado.nome}\nDia da colheita: {calculo_dias}\n"
        dados  += "-"*30
        return dados

class Quartel(Construcao):
    def __init__(self, x, y, Material):
            super().__init__("Quartel Militar", f"{Fore.LIGHTGREEN_EX}%{Style.RESET_ALL}", "Militar", Material, 20, 0,x,y)

class Construir:
    def __init__(self,nome,preco_ouro,quantidade_materiais,construcao):
        self.nome  = "Construir "+nome
        self.preco_ouro = preco_ouro
        self.quantidade_materiais = quantidade_materiais
        self.construcao = construcao
        

    def requisicao(self,ouro,mapa,reino,material,x,y):
        condicao = self.verificarCondicoes(ouro,material)

        if condicao:
            continuar = True
            ouro -= self.preco_ouro
            reino.ouro = ouro
            for constru in reino.construcoes:
                if constru.nome == "Armazem de materiais":
                    for i in range(len(constru.inventario)):
                        if constru.inventario[i].nome.nome == material.nome.nome and continuar:
                            if constru.inventario[i].quantidade >= self.quantidade_materiais:
                                constru.inventario[i].quantidade -= self.quantidade_materiais
                                continuar = False
                            else:
                                constru.inventario[i].quantidade = 0
                            
            
            self.construir(x,y,mapa,reino,material)
            print("Construção realizada com sucesso!")
        else:
            print("Você não tem recursos suficientes para construir isso.")
        
    def construir(self,x,y,mapa,reino,Material):
        construcao = self.construcao(x,y,Material.nome)
        mapa[x][y] = construcao.simbolo
        reino.construcoes.append(construcao)
    
    def verificarCondicoes(self,ouro,materiais):
        if ouro >= self.preco_ouro and materiais.quantidade >= self.quantidade_materiais:
            return True
        return False

class TorreVigilia(Construcao):
    def __init__(self, x, y, Material):
        super().__init__("Torre de vigilha", f"{Fore.LIGHTYELLOW_EX}A{Style.RESET_ALL}", "Defesa",Material, 5,1,x,y)

class ConstruirMina(Construir):
    def __init__(self):
        super().__init__("Mina",preco_ouro=5, quantidade_materiais=2, construcao=Mina)

class ConstruirTorre(Construir):
    def __init__(self):
        super().__init__("Torre de vigilha",preco_ouro=5, quantidade_materiais=2, construcao=TorreVigilia)

class ConstruirCabana(Construir):
    def __init__(self):
        super().__init__("Cabana",preco_ouro=5, quantidade_materiais=2, construcao=Cabana)

class ConstruirCasa(Construir):
    def __init__(self):
        super().__init__("Casa",preco_ouro=10, quantidade_materiais=4, construcao=Casa)

class ConstruirTaverna(Construir):
    def __init__(self):
        super().__init__("Taverna",preco_ouro=10, quantidade_materiais=6, construcao=Taverna)

class ConstruirMurro(Construir):
    def __init__(self):
        super().__init__("Murro",preco_ouro=10, quantidade_materiais=0, construcao=Murro)

class ConstruirPlantacao(Construir):
    def __init__(self):
        super().__init__("Plantação",preco_ouro=5, quantidade_materiais=0, construcao=None)

    def setConstrucao(self,tipo_cultivo,dia):
        print(tipo_cultivo)
        self.construcao = Plantacao(tipo_cultivo,dia)
        
    def verificarCondicoes(self,ouro,materiais):
        if ouro >= self.preco_ouro:
            return True
        return False

    def requisicao(self,ouro,mapa,reino,material,x,y):
        condicao = self.verificarCondicoes(ouro,material)

        if condicao:
            continuar = True
            ouro -= self.preco_ouro
            reino.ouro = ouro
            mapa[x][y] = self.construcao.simbolo
            reino.construcoes.append(self.construcao)

            self.construcao.x = x
            self.construcao.y = y
            print("Construção realizada com sucesso!")
        else:
            print("Você não tem recursos suficientes para construir isso.")

class ConstruirPostoComercio(Construir):
    def __init__(self):
        super().__init__("Posto de Comercio",preco_ouro=10, quantidade_materiais=0, construcao=Posto_Comercio)

class ConstruirTemplo(Construir):
    def __init__(self):
        # A construção de templo exige a divindade ser passada
        def templo_factory(x, y, material):
            templo = Templo(x,y,material)
            templo.x = x
            templo.y = y
            return templo
        
        super().__init__("Templo",preco_ouro=20, quantidade_materiais=0, construcao=templo_factory)

class ConstruirArmazem(Construir):
    def __init__(self):
        super().__init__("Armazem",preco_ouro=20, quantidade_materiais=0, construcao=Armazem)

class ConstruirArmazem_Comida(Construir):
    def __init__(self):
        super().__init__("Armazem de comida",preco_ouro=20, quantidade_materiais=0, construcao=Armazem_Comida)

class ConstruirArmazem_materiais(Construir):
    def __init__(self):
        super().__init__("Armazem de materiais",preco_ouro=20, quantidade_materiais=0, construcao=Armazem_materiais)

class ConstruirQuartel(Construir):
    def __init__(self):
        super().__init__("Quartel Militar",preco_ouro=20, quantidade_materiais=0, construcao=Quartel)
