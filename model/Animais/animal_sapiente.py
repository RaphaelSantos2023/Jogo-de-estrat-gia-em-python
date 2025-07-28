from model.Animais.animal import Animal
from model.Meteriais.comida import Comida
from model.Animais.profisoes import Lenhador, Minerador, Pescador, Fazendeiro
from model.Meteriais.material import Material
import random
from colorama import Fore, Style, init


personalidade = [
    {"nome": "Amável", "oposto": "Rude"},
    {"nome": "Rude", "oposto": "Amável"},
    {"nome": "Leal", "oposto": "Desleal"},
    {"nome": "Desleal", "oposto": "Leal"},
    {"nome": "Corajoso", "oposto": "Covarde"},
    {"nome": "Covarde", "oposto": "Corajoso"},
    {"nome": "Gentil", "oposto": "Irritável"},
    {"nome": "Irritável", "oposto": "Gentil"},
    {"nome": "Empático", "oposto": "Egoísta"},
    {"nome": "Paciente", "oposto": "Impulsivo"},
    {"nome": "Impulsivo", "oposto": "Paciente"},
    {"nome": "Otimista", "oposto": "Pessimista"},
    {"nome": "Pessimista", "oposto": "Otimista"},
    {"nome": "Extrovertido", "oposto": "Introvertido"},
    {"nome": "Introvertido", "oposto": "Extrovertido"},
    {"nome": "Generoso", "oposto": "Avareza"},
    {"nome": "Sarcástico", "oposto": "Sincero"},
    {"nome": "Teimoso", "oposto": "Flexível"}
]

Interacoes = {
    "Amavel": {"Feliz": 2, "Neutro": 1, "Triste": 0, "Irritado": -1},
    "Leal": {"Feliz": 2, "Neutro": 0, "Triste": -1, "Irritado": -1},
    "Corajoso": {"Feliz": 2, "Neutro": 0, "Triste": -1, "Irritado": -1},
    "Gentil": {"Feliz": 2, "Neutro": 1, "Triste": 0, "Irritado": -1},

    "Irritavel": {"Feliz": 1, "Neutro": 0, "Triste": -1, "Irritado": -2},
    "Desleal": {"Feliz": 1, "Neutro": 0, "Triste": -1, "Irritado": -1},
    "Covarde": {"Feliz": 2, "Neutro": 1, "Triste": -1, "Irritado": -1},
    "Rude": {"Feliz": 1, "Neutro": 0, "Triste": -1, "Irritado": -2},

    # Novos traços adicionados
    "Empatico": {"Feliz": 3, "Neutro": 1, "Triste": 1, "Irritado": -1},
    "Sarcástico": {"Feliz": 1, "Neutro": 0, "Triste": -1, "Irritado": -2},
    "Paciente": {"Feliz": 2, "Neutro": 2, "Triste": 1, "Irritado": 0},
    "Impulsivo": {"Feliz": 1, "Neutro": 0, "Triste": -2, "Irritado": -3},
    "Otimista": {"Feliz": 3, "Neutro": 1, "Triste": 0, "Irritado": -1},
    "Pessimista": {"Feliz": 0, "Neutro": -1, "Triste": -2, "Irritado": -2},
    "Introvertido": {"Feliz": 1, "Neutro": 0, "Triste": -1, "Irritado": -1},
    "Extrovertido": {"Feliz": 2, "Neutro": 1, "Triste": 0, "Irritado": -1},
    "Teimoso": {"Feliz": 1, "Neutro": 0, "Triste": -1, "Irritado": -2},
    "Generoso": {"Feliz": 3, "Neutro": 1, "Triste": 0, "Irritado": -1}
}

class Animal_Sapien (Animal):
  def __init__(self,simbolo,vida,dano,idade,Nome_especie,x,y):
      
      super().__init__(simbolo,vida,100,dano,100,idade," ",10,x,y)
      self.GerarNome()
      self.Nome_especie = Nome_especie
      self.personalidade = []
      self.necessidades = {"Diversão": 0, "Fé": 0, "Socializar" : 0}
      self.emTemplo = False
      self.seDivertindo = False

      self.Ferido = False
      self.Doente = False
      self.livre = True

      self.acao_momento = ["Socializar"]
      self.profissos = self.GerarProfissao()
      self.conhecidos = []
      self.n_filhos = random.randint(1,4)
      self.Quantidade_filhos = 0
      self.parceiro = None

      self.Dentro_estrutura = False
      self.explorando = False
      self.servico_militar = False
      self.servico_religioso = False
      self.servico_deus = None
      self.deus_adorado = None
      
      self.max_x = 0
      self.max_y = 0
      self.min_x = 0
      self.min_y = 0
      self.horas_dentro = 0
      
      self.intencao = ''
      self.ComplementoRaca()
      self.GerarPersonalidade()

  def DesignarNomePersonalidade(self,nome,personalidade):
      self.nome = nome
      self.personalidade = personalidade
  
  def movimentar(self,tamanho,relogio, matriz,reino,Construcaao=None):
    
    if self.acao_momento[0] == "Trabalhar":
        self.profissos[0].movimentar(self,reino,matriz)

    elif self.acao_momento[0] == "Comer":
        self.horas_dentro = relogio.dia
        for construcao in reino.construcoes:
            if construcao.nome == "Armazem de comida" and construcao.inventario != []:
                    construcao.movimentar(self,"Comer", matriz)
            
    elif self.acao_momento[0] == "Guardar":
        if isinstance(self.inventario[0],Comida):
            for construcao in reino.construcoes:
                if construcao.nome == "Armazem de comida":
                    construcao.movimentar(self,"Guardar",matriz)
        elif isinstance(self.inventario[0],Material):
            for construcao in reino.construcoes:
                if construcao.nome == "Armazem de materiais":
                    construcao.movimentar(self, matriz)
    
    elif self.acao_momento[0] == "Colher":
        for plantacao in reino.construcoes:
            if plantacao.nome == "Plantação":
                if plantacao.pronta:
                    plantacao.movimentar(self, matriz)
    
    elif self.acao_momento[0] == "Descançar":
        for construcao in reino.construcoes:
            if construcao.tipo == "Habitacional":
                construcao.movimentar(self, matriz)
        if self.felicidade != 100:
            self.felicidade +=1
        
    elif self.acao_momento[0] == "Rezar":
        for construcao in reino.construcoes:
            if construcao.nome =="Templo":
                if isinstance(construcao.Divindade,self.deus_adorado) and construcao.quantidadeP< construcao.quantidadePMax:
                    construcao.movimentar(self,matriz)
    elif self.acao_momento[0] == "Se Divertir":
        for construcao in reino.construcoes:
            if construcao.tipo == "Socializar":
                if construcao.quantidadeP > 0:
                    print("Achou!!!!!!!!")
                    print(f"{self.nome} está na ação {self.acao_momento[0]}")
                    construcao.movimentar(self,matriz)
    
    elif self.acao_momento[0] != "Dormindo":
        self.definir_XY(tamanho)
        while matriz[self.x][self.y] != ".":
            self.definir_XY(tamanho)
    #if self.acao_momento[0] != "Dormindo" and self.acao_momento[0] != "Socializar":
    #    print(f"{self.nome} está na ação {self.acao_momento[0]}")
    
  def GerarNome(self):
    nomes = []

    match self.genero:
        case "Masculino":
            nomes = [
                "Tharion", "Eldor", "Kael", "Darian", "Fenrik", "Beren", "Alaric", "Garruk",
                "Maeron", "Torvin", "Lorcan", "Draven", "Varian", "Hadrian", "Zarek", "Nerion",
                "Aelric", "Caelum", "Rowan", "Talion"
            ]
        case "Feminino":
            nomes = [
                "Lyra", "Seraphine", "Elowen", "Nymeria", "Aeris", "Thalia", "Isolde", "Sylwen",
                "Mireya", "Ygritte", "Alura", "Celestine", "Nimue", "Vanya", "Selene", "Rhiannon",
                "Arianne", "Leoriel", "Velanna", "Elaria"
            ]

    sobrenomes = [
        "Sombravento", "Coração de Fogo", "da Névoa", "Folha Prateada", "da Rocha Partida",
        "Tempeslume", "Silenciosa", "Chama Negra", "dos Nove Véus", "Espinho de Ferro",
        "do Vale Esquecido", "Guardassol", "Trizumbra", "Olho de Vidro", "Cavalgélido",
        "Sussurro Noturno", "Luz de Estrelas", "Sangue Antigo", "Punhal de Prata", "Martelo Rubro",
        "Cinturão de Névoa", "da Lua Minguante", "da Torre Quebrada", "Sombragema",
        "d’Oásis Escondido", "Escudo de Cinza", "da Espiral Carmesim", "Vulto Errante",
        "da Rosa Negra", "do Abismo"
    ]

    self.nome = random.choice(nomes) + " " + random.choice(sobrenomes)


  def Interacao(self, humano):
    global Interacoes

    interacao = 0
    emocao = humano.emocoes
    for i in range(3):
        p1 = self.personalidade[i]
        p2 = humano.personalidade[i]
        interacao += Interacoes.get(p2["nome"], {}).get(emocao, 0)
    self.conhecidos.append((humano, interacao, "Conhecido"))
    self.interacoesDecisao(interacao)

  def interacoesDecisao(self, interacao):
          if interacao > 0:
              self.EmBomMau("Bom")
          elif interacao < 0:
              self.EmBomMau("MAU")
   
  def atualizar_emocao(self, humano, reino):
        for i in range(len(self.conhecidos)):
            pessoa, interacao, posicao = self.conhecidos[i]
            if pessoa == humano:
                emocao = humano.emocoes
                # Atualiza interação somando valores das personalidades
                for j in range(3):
                    p2 = humano.personalidade[j]

                    # Se p2 for um dicionário ou objeto, use um identificador único
                    if isinstance(p2, dict):
                        interacao += Interacoes.get(p2.get('nome', ''), {}).get(emocao, 0)
                    elif hasattr(p2, 'nome'):  # Se p2 for um objeto, acesse o nome ou algum atributo
                        interacao += Interacoes.get(p2.nome, {}).get(emocao, 0)
                    else:
                        interacao += Interacoes.get(str(p2), {}).get(emocao, 0)

                NovaPosicao = posicao  # mantém a posição atual, pode mudar abaixo
                if posicao != "Mãe" or posicao != "Pai" or posicao != "Filho" or posicao != "Filha":
                    if interacao >= 800 and self.parceiro is None and humano.parceiro is None:
                        index = 0
                        p = None
                        inter = 0
                        pos = ""

                        for idx in range(len(humano.conhecidos)):
                            p, inter, pos = humano.conhecidos[idx]
                            if p == self:
                                index = idx
                                break
                        valor = self.sexualidade.relacao(humano)
                        valor2 = humano.sexualidade.relacao(self)
                        if valor and valor2 and inter >= 0:
                            self.parceiro = humano
                            humano.parceiro = self  # corrigido aqui (parceiro)
                            humano.conhecidos[index] = (p, inter, "Parceiro")
                            # Atualiza o status do conhecido na lista de ambos para "Parceiro"
                            self.conhecidos[i] = (pessoa, interacao, "Parceiro")

                            # Agora encontra o índice de self na lista conhecidos do humano
                            NovaPosicao = "Parceiro"

                    elif interacao >= 200 and humano != self.parceiro:
                        NovaPosicao = "Amigo"
                    elif interacao <= -50 and humano != self.parceiro:
                        NovaPosicao = "Inimigo"

                    elif interacao >= 1000 and humano == self.parceiro and self.genero == 'Feminino' and self.sexualidade.preferencia != 'Mesmo' and self.Quantidade_filhos < self.n_filhos:
                        self.procriar(reino)
                self.conhecidos[i] = (pessoa, interacao, NovaPosicao)
                self.interacoesDecisao(interacao)
                break

  def procriar(self,reino):

      self.Quantidade_filhos += 1
      especie_parceiro = self.parceiro.Nome_especie
      especieCrianca = random.choice([especie_parceiro,self.Nome_especie])

      simbolo = random.choice([self.simbolo,self.parceiro.simbolo])
      
      cria = Animal_Sapien(simbolo,self.vidaMax,100,1,especieCrianca,self.x,self.y)

      cria.GerarNome()
      cria.GerarPersonalidade()
      
      self.felicidade += 100
      self.parceiro.felicidade += 100

      genero_cria = ""
      if cria.genero == "Feminino":
          genero_cria = "Filha"
      else:
          genero_cria = "Filho"
    
      self.conhecidos.append((cria, 10000, genero_cria))
      self.parceiro.conhecidos.append((cria, 10000, genero_cria))
      
      cria.conhecidos.append((self, 100, "Mãe"))
      cria.conhecidos.append((self.parceiro, 100, "Pai"))

      sobrenome_pai = self.parceiro.nome.split(' ', 1)[1]
      sobrenome_mae = self.nome.split(' ', 1)[1]
      
      cria.nome = cria.nome.split(' ', 1)[0] + ' ' + sobrenome_mae + ' ' + sobrenome_pai
      reino.populacao += 1
      reino.cidadaos.append(cria)
      
  def Socializar(self, humano,reino):
          if humano not in [h for h, _, _ in self.conhecidos]:
            self.Interacao(humano)
          else:
            self.atualizar_emocao(humano,reino)

  def __str__(self):
          return self.nome
    
  def definir_XY(self,tamanho):
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        novo_x = max(0, min(tamanho - 1, self.x + dx))
        novo_y = max(0, min(tamanho - 1, self.y + dy))
        self.x = novo_x
        self.y = novo_y

  def GerarPersonalidade(self):
      personalidadesBoas = [personalidade[i] for i in range(1, len(personalidade), 2)]

      personalidadesMas = [personalidade[i] for i in range(0, len(personalidade), 2)]


      Espectro = random.choice(["Bom", "Mau"])

      if Espectro == "Bom":
          boas = random.sample(personalidadesBoas, 2)
          opostos_boas = {p['oposto'] for p in boas}
          mas_filtradas = [p for p in personalidadesMas if p['nome'] not in opostos_boas]
          mas = random.sample(mas_filtradas, 1)
      else:
          mas = random.sample(personalidadesMas, 2)
          opostos_mas = {p['oposto'] for p in mas}
          boas_filtradas = [p for p in personalidadesBoas if p['nome'] not in opostos_mas]
          boas = random.sample(boas_filtradas, 1)

      self.personalidade = boas + mas
      random.shuffle(self.personalidade)  # opcional: mistura a ordem
      self.EmBomMau(Espectro)

  def EmBomMau(self,espectro):
      if espectro == "Bom":
          self.felicidade+=1
          self.emocoes = random.choice(["Feliz", "Neutro"])
      if espectro == "MAU":
          self.felicidade-=1
          self.emocoes = random.choice(["Neutro","Triste", "Irritado"])

  def GerarProfissao(self):
      proffisao = random.choice([Lenhador(),Minerador(),Pescador(),Fazendeiro()])
      return [proffisao]

  def ComplementoRaca(self):
      self.vida += self.Nome_especie.vida
      self.dano += self.Nome_especie.dano
      self.forca += self.Nome_especie.forca
      self.destreza += self.Nome_especie.destreza
      self.inteligencia += self.Nome_especie.inteligencia
      self.carisma += self.Nome_especie.carisma
      self.constituicao += self.Nome_especie.constituicao

  def getInventario(self):
      text = '\nInventario: \n'
      for item in self.inventario:
          text += f"• {item.nome}\n"
      return text
    
  def mostrar_Necessidade(self):
    text = ""
    if self.necessidades["Diversão"]> 50:
        text += "- Necessidade de diversão\n"
    if self.necessidades["Fé"] > 50:
        text += "- Necessidade de rezar\n"
    if self.necessidades["Socializar"] > 50:
        text += "- Necessidade de socializar\n"
    text = f"{Fore.RED}"+text+f"{Style.RESET_ALL}"

    if text == "":
        text = "Contente\n"
        text = f"{Fore.GREEN}"+text+f"{Style.RESET_ALL}"
    
    return 

  def Descricao(self):
    descricao_base = super().Descricao()
    inventario = self.getInventario()
    necessidade = self.mostrar_Necessidade()
    personalidade_str = ", ".join([p['nome'] if isinstance(p, dict) else str(p) for p in self.personalidade])
    profissoes_str = ", ".join([p.nome for p in self.profissos]) if self.profissos else "Nenhuma"

    return (
    f"\n👤 {self.nome} — Um(a) {self.Nome_especie.nome}\n"
    f"🎭 Emoção atual: {self.emocoes}\n"
    f"Necessidade: \n{necessidade}\n"
    f"😀 Felicidade: {self.felicidade}\n"
    f"🍽️ Fome: {self.fome}\n"
    f"🧠 Personalidade: {personalidade_str}\n"
    f"🛠️ Profissões: {profissoes_str}\n"
    f"🎯 Ação atual: {self.acao_momento[0]}\n"
    f"🏷️ Espécie: {self.Nome_especie.nome}\n"
    f"† Fé: {self.deus_adorado.nome}\n"
    f"{inventario}"
    )


