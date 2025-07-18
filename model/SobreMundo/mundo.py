import random
from colorama import Fore, Style, init
from model.SobreMundo.Reinos import Faccoes

class Mundo:
  def __init__(self,nome,reinos,monstros,racas,regioes,religiao,culturas):
    self.nome = nome
    self.reinos = reinos
    self.monstros = monstros
    self.racas = racas
    self.regioes = regioes
    self.religiao = religiao
    self.culturas = culturas

  def descricao(self):
    print("\n\n------ Reinos ------------------------------\n\n")
    for i in range(len(self.reinos)):
      print(self.reinos[i].Descricao())
    print("\n\n------ Monstros ------------------------------\n\n")
    for i in range(len(self.monstros)):
      print(self.monstros[i].Descricao())
    print("\n\n------ Raças ------------------------------\n\n")
    for i in range(len(self.racas)):
      print(self.racas[i].Descricao())
    print("\n\n------ Regiões ------------------------------\n\n")
    for i in range(len(self.regioes)):
      print(self.regioes[i].Descricao())

class Regioes:
  def __init__(self,nome,tipo,animais,reinos,temperatura,vegetacao,riqueza_mineral):
    self.nome = nome
    self.tipo = tipo
    self.animais = animais
    self.vegetacao = vegetacao
    self.riqueza_mineral = riqueza_mineral
    self.reinos = reinos
    self.temperatura = temperatura

  def monstrarAnimais(self):
    text = ""
    for animal in self.animais:
      animal = animal()
      text += f"\n- {animal.nome}"
    return text
    
  def Descricao(self):
    text = self.monstrarAnimais()
    txt = f"Região: {self.nome},\n Tipo: {self.tipo['nome']},\n Animais: {text}\n Vegetação: {self.vegetacao} \nTemperatura: {self.temperatura},\n Reinos"
    for i in range(len(self.reinos)):
      txt += "\n - "+self.reinos[i].nome
    txt += "\n\n"
    
    return txt

class Relogio:
  def __init__(self):
      self.dia = 1
      self.hora = 6
      self.minuto = 0
      self.mes = 1
      self.ano = 0

  def passar_tempo(self,cidadaos):
      """Avança um segundo no tempo e atualiza as horas, minutos, dias."""
      self.minuto += 1 #random.randint(5,10)

      # Se passaram 60 minutos, aumentamos as horas
      if self.minuto >= 60:
          self.minuto = 0
          self.hora += 1

      # Se passaram 24 horas, aumentamos o dia
      if self.hora >= 24:
          self.hora = 0
          self.dia += 1
      
      if self.dia >= 365:
          for h in cidadaos:
            h.idade += 1
          self.mes = 0
          self.ano += 1

  def mostrar_hora(self):
      """Exibe a hora no formato Dia: Hora:Minuto:Segundos"""
      return f"{self.hora:02d}:{self.minuto:02d}"
    
  def mostrar_data(self):
      """Exibe a data no formato Dia: Hora:Minuto:Segundos"""
      return f"Dia {self.dia:02d} do ano {self.ano:02d}"

class Eventos_Historicos:
  def __init__(self,nome,participante1, participante2,tipo,ano):
      self.nome = nome
      self.participante1 = participante1
      self.participante2 = participante2
      self.tipo = tipo
      self.causa = ""
      self.acontecimento = ""
      self.ano = ano

  def Causa(self):
    causas = ["conflito racial","conflito religioso","conflito cultura","recursos","dominancia regional"]
    self.causa = random.choice(causas)

  def Definir_resultado(self):
     return

  def gerar_Situacao(self):
    self.Causa()
    self.Definir_resultado()

class Guerra_evento(Eventos_Historicos):
    def __init__(self, participante1, participante2, ano):
      super().__init__(f"Guerra {participante1.nome}-{participante2.nome}", participante1, participante2,"Guerra", ano)
      self.Vencedor= None
      self.Perdedor = None

class Evento_guerra_reinos(Guerra_evento):
    def __init__(self, participante1, participante2, ano):
      super().__init__(participante1, participante2, ano)
    
    def Definir_resultado(self):

      def participante(participante,outro):
        tem = False
        for i, item in enumerate(participante.relacoes_reinos):
          if item["Nome"] == outro:
            item["Afinidade"] -= 50
            tem = True
        if tem is not True:
          participante.relacoes_reinos.append({"Nome":outro,"Afinidade":-50})
      
      peso_ouro = 0.5  # Ajuste conforme a importância do ouro

      poder1 = (self.participante1.populacao * self.participante1.raca.dano) + (self.participante1.ouro * peso_ouro)
      poder2 = (self.participante2.populacao * self.participante2.raca.dano) + (self.participante2.ouro * peso_ouro)

      if poder1 > poder2:
          self.Vencedor = self.participante1
          self.Perdedor = self.participante2
      else:
          self.Vencedor = self.participante2
          self.Perdedor = self.participante1
      
      participante(self.Vencedor,self.Perdedor )
      participante(self.Perdedor ,self.Vencedor)

class Evento_guerra_civil(Guerra_evento):
  def __init__(self, participante1, participante2, ano):
    super().__init__(participante1, participante2, ano)

  def Causa(self):
    causas = ["fome","decadencia da liderança","opressao"]
    self.causa = random.choice(causas)
    
  def Definir_resultado(self):
    def participante(participante,outro):
        tem = False
        for i, item in enumerate(participante.faccoes_reino):
          if item["Nome"] == outro:
            item["Afinidade"] -= 50
            tem = True
        if tem is not True:
          participante.faccoes_reino.append({"Nome":outro,"Afinidade":-50})
    
    def pontuacao_racial(raca):
        return (
          raca.vida +
          raca.dano +
          raca.forca +
          raca.destreza +
          raca.inteligencia +
          raca.carisma +
          raca.constituicao
        )
    poder1 = pontuacao_racial(self.participante1.raca) * len(self.participante1.exercito.exercito)
    poder2 = pontuacao_racial(self.participante2.raca) * len(self.participante2.exercito.exercito)

    if poder1 > poder2:
      self.Vencedor = self.participante1
      self.Perdedor = self.participante2
    else:
      self.Vencedor = self.participante2
      self.Perdedor = self.participante1
    
    participante(self.participante1,self.participante2)
    participante(self.participante2,self.participante1)

class Evento_guerra_racial(Guerra_evento):
    def __init__(self, participante1, participante2,ano):
      super().__init__(participante1, participante2, ano)
    
    def Definir_resultado(self):
      def participante(participante,outro):
        tem = False
        for i, item in enumerate(participante.relacao_racas):
          if item["Nome"] == outro:
            item["Afinidade"] -= 50
            tem = True
        if tem is not True:
          participante.relacao_racas.append({"Nome":outro,"Afinidade":-50})
      
      def pontuacao_racial(raca):
        return (
          raca.vida +
          raca.dano +
          raca.forca +
          raca.destreza +
          raca.inteligencia +
          raca.carisma +
          raca.constituicao
        )

      pont1 = pontuacao_racial(self.participante1)
      pont2 = pontuacao_racial(self.participante2)

      if pont1 > pont2:
        self.Vencedor = self.participante1
        self.Perdedor = self.participante2
      else:
        self.Vencedor = self.participante2
        self.Perdedor = self.participante1

      participante(self.participante1,self.participante2)
      participante(self.participante2,self.participante1)

class Alianca_evento(Eventos_Historicos):
  def __init__(self, participante1, participante2, ano):
      super().__init__(f"Aliança {participante1.nome}-{participante2.nome}", participante1, participante2,"Alianca", ano)
      self.Membro1= None
      self.Membro2 = None
  
  def Causa(self):
    causas = ["Comercial","Militar","Cultural"]
    self.causa = random.choice(causas)

  def Definir_resultado(self):
    def participante(participante,outro):
        tem = False
        for i, item in enumerate(participante.relacoes_reinos):
          if item["Nome"] == outro:
            item["Afinidade"] += 50
            tem = True
        if tem is not True:
          participante.relacoes_reinos.append({"Nome":outro,"Afinidade":50})
    
    self.Membro1 = self.participante1
    self.Membro2 = self.participante2

    participante(self.participante1,self.participante2)
    participante(self.participante2,self.participante1)    

class Invasao_Monstro(Eventos_Historicos):
  def __init__(self, participante1, monster, ano):
    super().__init__(f"Ataque de {monster.nome} a {participante1.nome}", participante1, monster, "Invasao Monstro", ano)
    self.vitoria_reino = False
  
  def Causa(self):
    causas = ["mandato divino","fome insaciavel da fera","espiritos malignos"]
    self.causa = random.choice(causas)
  
  def Definir_resultado(self):
    def participante(participante,outro):
        tem = False
        for i, item in enumerate(participante.relacoes_reinos):
          if item["Nome"] == outro:
            item["Afinidade"] -= 50
            tem = True
        if tem is not True:
          participante.relacoes_reinos.append({"Nome":outro,"Afinidade":-50})
    
    def pontuacao_racial(raca):
            return (
              raca.vida +
              raca.dano +
              raca.forca +
              raca.destreza +
              raca.inteligencia +
              raca.carisma +
              raca.constituicao
            )

      
    poder1 = pontuacao_racial(self.participante1.raca)
    poderMonst = pontuacao_racial(self.participante2)

    if poder1 > poderMonst:
      self.vitoria_reino = True
    
    participante(self.participante1,self.participante2)

class Historia:
  def __init__(self,mundo,ano):
    self.mundo = mundo
    self.ano = ano
    self.anoPrimeiro = 1
    self.eventos = []
    self.historia_completo = ""
  
  def gerarGenesis(self):
    txt = "Numa era em que o tempo não existia, os deuses nasceram\n"
    self.historia_completo += txt
  
  def GerrarEvento(self,ano):
    def guerra():
      def determinar():
        escolha = random.choice(["Racial","Reino"])
        match escolha:
          case "Reino":
            particiantes = random.sample(self.mundo.reinos,2)
            classe_usada = Evento_guerra_reinos
          case "Racial":
            particiantes = random.sample(self.mundo.racas,2)
            classe_usada = Evento_guerra_racial
        
        return particiantes, classe_usada

      participantes, classes = determinar()
      
      guerra = classes(participantes[0],participantes[1],ano)
      guerra.gerar_Situacao()
      txt = (
          f"\n• No ano {Fore.LIGHTYELLOW_EX}{ano}{Style.RESET_ALL},"
          f"a tensão entre {Fore.RED}{guerra.participante1.nome}{Style.RESET_ALL} e {Fore.RED}{guerra.participante2.nome}{Style.RESET_ALL} atingiu o auge,\n"
          f"culminando em uma {Fore.RED}guerra motivada por {guerra.causa}{Style.RESET_ALL}.\n"
          f"Após confrontos brutais, {Fore.YELLOW}{guerra.Vencedor.nome}{Style.RESET_ALL} emergiu vitorioso sobre {Fore.LIGHTMAGENTA_EX}{guerra.Perdedor.nome}{Style.RESET_ALL}."
      )

      if  isinstance(classes,Evento_guerra_reinos):
        participantes[0].historia_reino += txt
        participantes[1].historia_reino += txt

      self.historia_completo += txt

      self.eventos.append({"Evento":guerra, "Ano": ano, "Hitoria": txt})
  
    def Alianca():
      participantes = random.sample(self.mundo.reinos,2)
      
      alianca = Alianca_evento(participantes[0],participantes[1],ano)
      alianca.gerar_Situacao()
      txt = (
          f"\n• No ano {Fore.LIGHTYELLOW_EX}{ano}{Style.RESET_ALL}, "
          f"{Fore.LIGHTCYAN_EX}{alianca.Membro1.nome}{Style.RESET_ALL} e {Fore.LIGHTCYAN_EX}{alianca.Membro2.nome}{Style.RESET_ALL} selaram uma {Fore.GREEN}aliança {alianca.causa.lower()}{Style.RESET_ALL}.\n"
          f"Unidos por interesses comuns, os dois reinos passaram a caminhar lado a lado em seus destinos."
      )

      self.historia_completo += txt

      participantes[0].historia_reino += txt
      participantes[1].historia_reino += txt

      self.eventos.append({"Evento":alianca, "Ano": ano, "Hitoria": txt})
    
    def Monstro_invasao():
      participante = random.choice(self.mundo.reinos)
      monstro = random.choice(self.mundo.monstros)
      
      luta = Invasao_Monstro(participante,monstro,ano)
      luta.gerar_Situacao()

      if luta.vitoria_reino:
        resultado = (
            f"{Fore.LIGHTGREEN_EX}Com muitos sacrifícios{Style.RESET_ALL}, "
            f"o povo de {Fore.LIGHTCYAN_EX}{luta.participante1.nome}{Style.RESET_ALL} "
            f"ergueu-se contra a ameaça e conseguiu repelir a criatura {Fore.LIGHTRED_EX}{luta.participante2.nome}{Style.RESET_ALL}.\n"
            f"Feridos, mas orgulhosos, os sobreviventes cantaram sua vitória nas ruínas fumegantes."
        )
      else:
          resultado = (
              f"O poder do {Fore.LIGHTRED_EX}{luta.participante2.nome}{Style.RESET_ALL} "
              f"foi {Fore.RED}avassalador{Style.RESET_ALL}. "
              f"As forças de {Fore.LIGHTCYAN_EX}{luta.participante1.nome}{Style.RESET_ALL} tombaram uma a uma,\n"
              f"e os poucos sobreviventes fugiram, levando nos olhos o terror e na alma as cicatrizes do desastre."
          )
      
      txt = (
        f"\n• No ano {Fore.LIGHTYELLOW_EX}{ano}{Style.RESET_ALL}, "
        f"um presságio antigo se cumpriu: a criatura {Fore.LIGHTRED_EX}{luta.participante2.nome}{Style.RESET_ALL} "
        f"emergiu das trevas e marchou contra {Fore.LIGHTCYAN_EX}{luta.participante1.nome}{Style.RESET_ALL}"
        f"atraída por {Fore.LIGHTMAGENTA_EX}{luta.causa.lower()}{Style.RESET_ALL}.\n"
        f"{resultado}"
      )

      participante.historia_reino += txt
      
      self.historia_completo += txt

      self.eventos.append({"Evento":luta, "Ano": ano, "Hitoria": txt})
    
    def Guerra_civil():
      participante = random.choice(self.mundo.reinos)
      tipos_faccoes = [
        "Clã Tribal",
        "Ordem Religiosa",
        "Sociedade Secreta",
        "Guilda Mercantil",
        "Conselho de Magos",
        "Milícia Popular",
        "Casa Nobre Dissidente",
        "Aliança de Cidades Livres",
        "Irmandade de Assassinos",
        "Seita Profética",
        "Legião Deserdada",
        "Círculo Druídico",
        "Confraria de Ladrões",
        "Corte Sombria",
        "Coalizão de Exilados",
        "Rebelião Camponesa",
        "Corporação de Mercenários",
        "Templo dos Ancestrais",
        "Assembleia de Hereges",
        "Pacto de Sangue"
      ]

      faccao = Faccoes()
      faccao.criar_Faccao(participante.raca, random.choice(tipos_faccoes), participante)

      guerra_civil = Evento_guerra_civil(participante, faccao, ano)
      guerra_civil.gerar_Situacao()

      txt = (
          f"\n• No ano {Fore.LIGHTYELLOW_EX}{ano}{Style.RESET_ALL}, "
          f"{Fore.LIGHTCYAN_EX}{participante.nome}{Style.RESET_ALL} mergulhou em caos e discórdia.\n"
          f"Motivado por {Fore.LIGHTMAGENTA_EX}{guerra_civil.causa.lower()}{Style.RESET_ALL}, "
          f"a facção {Fore.RED}{faccao.nome}{Style.RESET_ALL}, liderada por {Fore.LIGHTWHITE_EX}{faccao.lider.nome}{Style.RESET_ALL}, "
          f"ergueu-se contra o rei {Fore.YELLOW}{participante.rei.nome}{Style.RESET_ALL}, declarando guerra civil.\n"
      )

      if guerra_civil.Vencedor == faccao:
          participante.faccoes_reino.append({"Nome": participante.Faccao_Rei, "Afinidade": -100})
          txt += (
              f"Após batalhas sangrentas e traições veladas, "
              f"{Fore.LIGHTWHITE_EX}{faccao.lider.nome}{Style.RESET_ALL} "
              f"emergiu vitorioso, assumindo o trono de {Fore.LIGHTCYAN_EX}{participante.nome}{Style.RESET_ALL}.\n"
          )
          participante.rei = faccao.lider
          participante.Faccao_Rei = faccao
      else:
          txt += (
              f"A rebelião foi esmagada pelas forças leais ao rei, e {Fore.RED}{faccao.nome}{Style.RESET_ALL} "
              f"foi forçada à clandestinidade.\n"
              f"Mesmo derrotados, seus membros ainda murmuram promessas de vingança nas sombras."
          )
          participante.faccoes_reino.append({"Nome": faccao, "Afinidade": -100})

      participante.historia_reino += txt
      self.historia_completo += txt
      self.eventos.append({"Evento": guerra_civil, "Ano": ano, "Hitoria": txt})

    
    chance_evento = 0.6

    sucesso = random.random()

    if sucesso <= chance_evento:
      evento = [guerra,Alianca,Monstro_invasao,Guerra_civil]
      fazer_evento = random.choice(evento)()
    
  def IniciarHistoria(self):
    self.gerarGenesis()
    while self.anoPrimeiro < self.ano:
      self.GerrarEvento(self.anoPrimeiro)
      self.anoPrimeiro+=1

