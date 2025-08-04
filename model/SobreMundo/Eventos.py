import random
from model.Estoque.estoque import Estoque
from model.SobreMundo.Reinos import Exercito
from model.Animais.animal_sapiente import Animal_Sapien
from model.Animais.animal import Animal_domestico
from model.Meteriais.construcao import Armazem
from model.SobreMundo.Reinos import Combate
import msvcrt
import os
from colorama import Fore, Style, init

tamanho = 30

class Evento:
  def __init__(self):
    self.ativo = True
    self.ultimo_evento_dia = -1
    self.timer = 0.5

  def getch(self):
    return msvcrt.getch().decode('utf-8')
  
  def getRaca_Aleatoria(self,mundo):
    raca = random.choice(mundo.racas)
    return raca

  def CriarExercitoInvasao(self,mundo):
    raca = self.getRaca_Aleatoria(mundo)
    exercito = Exercito()
    Soldados = exercito.CriarExercito_Invasao(raca)
    return Soldados

  def pegarMonstro(self,mundo):
    return random.choice(mundo.monstros)
  
  def gerarPessoa(self,raca):
    vida = random.randint(1,10)
    dano = random.randint(1,5)
    idade = random.randint(18, 30)
    return Animal_Sapien(raca.simbolo,vida,dano,idade,raca,0,0)

  def getRegiaoJogador(self,mundo,jogador):
    for Regiao in mundo.regioes :
      if jogador in Regiao.reinos:
        return Regiao
  
  def getRegiao(self,mundo):
    return random.choice(mundo.regioes)
  
  def getReinoRegiao(self,regiao):
    return random.choice(regiao.reinos)
  
  def getAnimal(self,Regiao):
    animal = random.choice(Regiao.animais)
    return animal

  def evento_estacional(self, mundo, jogador,mapa):
      while self.ativo:
        print("\n[Evento Estacional]")

        # Evento: Animais perdidos
        def evento_animais_perdidos():
            regiao = self.getRegiaoJogador(mundo, jogador)
            animal = self.getAnimal(regiao)()
            quantidade = random.randint(10, 15)
            dono = self.getReinoRegiao(regiao)

            return {
                "descricao": lambda: f"Você encontra {quantidade} animais do tipo '{animal.nome}' vagando pela região. Eles parecem ter dono.",
                "opcoes": [
                    (
                        f"Pegar os animais (+{quantidade} {animal.nome})",
                        lambda j: self.pegar_animais(j, animal, quantidade, dono)
                    ),
                    (
                        f"Procurar o dono (ganha afinidade com {dono.nome})",
                        lambda j: self.procurar_dono(j, dono)
                    )
                ]
            }

        def evento_Exercito_inimigos():
            raca = random.choice(mundo.racas)

            exercito_invasor = Exercito()

            exercito_invasor.CriarExercito_Invasao(raca,mundo.religiao.deuses,jogador)
            
            exercito_invasor.selecionar_soldados_ativos()
            
            jogador.exercito.selecionar_soldados_ativos()
            quantidade_ativos = self.contar_ativos(jogador.exercito.exercito)

            if quantidade_ativos >0:
              return {
                  "descricao": lambda: f"O {Fore.RED}{exercito_invasor.nome}{Style.RESET_ALL}, um exercito de {Fore.RED} {len(exercito_invasor.exercito)} {raca.nome} {Style.RESET_ALL} marchão em sua direção.\nCom o ataque, dos {Fore.GREEN}{len(jogador.exercito.exercito)}{Style.RESET_ALL}, conseguimos reunir {Fore.GREEN}{quantidade_ativos}{Style.RESET_ALL}.\nO que devemos fazer?",
                  "opcoes": [
                      (
                          f"Avançar",
                          lambda j: self.Combater(jogador.exercito,exercito_invasor,"Avançar",jogador,mapa)
                      ),
                      (
                          f"Manter posição",
                          lambda j: self.Combater(jogador.exercito,exercito_invasor,"Manter posição",jogador,mapa)
                      ),
                      (
                          f"Berserker",
                          lambda j: self.Combater(jogador.exercito,exercito_invasor,"Berserker",jogador,mapa)
                      )
                  ]
              }
            else:
              combate = Combate()

              return {
                  "descricao": lambda: f"O {Fore.RED}{exercito_invasor.nome}{Style.RESET_ALL}, um exercito de {Fore.RED} {len(exercito_invasor.exercito)} {raca.nome} {Style.RESET_ALL} marchão em sua direção.\nPor conta de não ter soldados preparados para o ataque, os invasores arrazaram, sem ressitencia, o reino.",
                  "opcoes": [
                      (
                          f"Relatorio das perdas",
                          lambda j: combate.Metodo_derrota(jogador,exercito_invasor,mapa)
                      ),
                  ]
              }
        # Evento: Pessoa quer entrar no reino
        def evento_pessoa_pede_moradia():
            regiao = self.getRegiaoJogador(mundo, jogador)
            raca = random.choice(mundo.racas)
            pessoa = self.gerarPessoa(raca)

            return {
                "descricao": lambda: f"{pessoa.nome} ,um {raca.nome} deseja se juntar ao seu reino.",
                "opcoes": [
                    ("Aceitar (ela entra no seu reino)", lambda j: self.aceitar_pessoa(j, pessoa,mundo)),
                    ("Recusar educadamente", lambda j: print("Você recusa. A pessoa parte sem ressentimentos.")),
                    ("Testar habilidades antes", lambda j: self.testar_pessoa(j, pessoa,mundo))
                ]
            }

        def evento_passagem():
            regiao = self.getRegiaoJogador(mundo, jogador)
            raca = random.choice(mundo.racas)
            pessoa = self.gerarPessoa(raca)

            return {
                "descricao": lambda: f"Um grupo de {raca.nome} aparece em seu territorio\nEles querem permissão para passar, em troca eles oferecem um de três presentes:",
                "opcoes": [
                    ("Riquezas", lambda j: self.Passagem_metodo(1,raca,jogador,mapa,regiao,mundo)),
                    ("Alguns Animais", lambda j: self.Passagem_metodo(2,raca,jogador,mapa,regiao,mundo)),
                    ("Uma Benção", lambda j: self.Passagem_metodo(3,raca,jogador,mapa,regiao,mundo)),
                    ("Recusar e atacar", lambda j: self.Passagem_metodo(4,raca,jogador,mapa,regiao,mundo))
                ]
            }

        eventos = [
            #(evento_animais_perdidos, 10),
            #(evento_pessoa_pede_moradia, 5),
            (evento_Exercito_inimigos,10)#,
            #(evento_passagem,15)
        ]

        escolhido = random.choices(eventos, weights=[peso for _, peso in eventos])[0][0]
        evento = escolhido()

        print(evento["descricao"]())

        if not evento["opcoes"]:
            print("Nada a fazer neste turno.")
            return

        for i, (texto_opcao, _) in enumerate(evento["opcoes"]):
            print(f"{i+1}) {texto_opcao}")

        escolha = input("Sua decisão: ")

        #try:
        _, acao = evento["opcoes"][int(escolha) - 1]
        acao(jogador)
        self.ativo = False
        print(f"{Fore.YELLOW}---------------------------------------{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}>>Pressione qualquer tecla para continuar{Style.RESET_ALL}")
        self.getch()
        #except (IndexError, ValueError):
            #print("Escolha inválida. Nada foi feito.")

  def contar_ativos(self,exercito):
    quantidade = 0
    for soldado in exercito:
       if soldado['Ativo']:
          quantidade +=1 
    return quantidade

  # Auxiliares do evento de pessoa
  def aceitar_pessoa(self, jogador, pessoa,mundo):
      deus = random.choice(mundo.religiao.deuses)
      pessoa.deus_adorado = deus

      pessoa.definir_XY(tamanho)
      jogador.cidadaos.append(pessoa)  # assume que jogador.habitantes existe
      jogador.populacao += 1
      print(f"{pessoa.nome} agora faz parte do seu reino!")

  def testar_pessoa(self, jogador, pessoa,mundo):
      nota = pessoa.forca + pessoa.destreza + pessoa.inteligencia
      if nota >= 15:
          self.aceitar_pessoa(jogador,pessoa,mundo)
          print(f"{pessoa.nome} demonstrou grande potencial e foi aceito!")
      else:
          print(f"{pessoa.nome} não passou nos testes. Você decide não aceitá-lo.")

  def RelacaoIntensidade(self,dono,jogador):
    for relacao in dono.relacoes_reinos:
      if jogador == relacao['Reino']:      
        relacao['Afinidade'] -= 2
        return
    dono.relacoes_reinos.append({"Reino": jogador, "Relacao": "Neutro", "Afinidade":-2})
  
  def acharArmazem(self, construcoes):
    for construcao in construcoes:
        if isinstance(construcao, Armazem):
            return construcao
    return None  # adiciona retorno explícito para evitar erro se não houver armazém

  def checarAnimais(self, construcoes, animal_adicao, quantidade):
    construcao = self.acharArmazem(construcoes)
    if not construcao:
        print("Nenhum armazém encontrado! Os animais foram perdidos.")
        return

    for item in construcao.inventario:
        if isinstance(item['Nome'], type(animal_adicao)):
            item['Quantidade'] += quantidade
            return

    construcao.inventario.append(Estoque(animal_adicao,quantidade))

  # Métodos auxiliares
  def pegar_animais(self, jogador, animal, quantidade, dono):
    print(jogador.construcoes)
    self.checarAnimais(jogador.construcoes,animal,quantidade)
    chance = random.random()
    if chance < 0.2:  # 20% de chance do dono descobrir e perder afinidade
      dono.Comida -= quantidade//2
      self.RelacaoIntensidade(dono,jogador)
          
      print(f"O dono ({dono.nome}) descobriu! Afinidade reduzida.")
    else:
      print(f"Os animais foram adicionados sem problemas.")

  def procurar_dono(self, jogador, dono):
      jogador.afinidade[dono] = min(100, jogador.afinidade.get(dono, 50) + 10)
      print(f"Você devolve os animais. {dono.nome} está agradecido! Afinidade aumentada.")
  
  def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
  
  def Combater(self,jogador,inimigo,tatica_jogador,reino_jogador,mapa):
    
    combate = Combate()

    tatica_ = ["Berserker","Avançar","Manter posição"]
    pesos =  [50,       30,       15] 

    tatica_inimigo = random.choices(tatica_, weights=pesos, k=1)[0]

    self.limpar_tela()
    combate.rodada(jogador, inimigo, tatica_jogador=tatica_jogador, tatica_inimigo=tatica_inimigo,jogador=reino_jogador,mapa=mapa)
  
  def Passagem_metodo(self,escolha,raca,jogador,mapa,regiao,mundo):
    match escolha:
      case 1:
          ouro_add = random.randint(5,30)
          jogador.ouro += ouro_add
          print(f"Eles te presentiaram com {ouro_add} de ouro")
      case 2:
          
          quantidade_animais = random.randint(10,20)
          animais = [obj for obj in regiao.animais]
          animal_escolhido = random.choice(animais)()
          print(f"Eles te presentearam com {quantidade_animais} {animal_escolhido.nome}")
          self.checarAnimais(jogador.construcoes, animal_escolhido, quantidade_animais)

      case 3:
          magia_quantidade = 1
          print(f"Eles realizaram ritos com insenso e sacrificios. As nuvens se afastaram do centro do ritual, em um circulo perfeito.\nVocê ganhou {magia_quantidade} de magia")  
          jogador.magia+= magia_quantidade
      case 4:
        exercito_invasor = Exercito()

        exercito_invasor.CriarExercito_Invasao(raca,mundo.religiao.deuses,jogador)
              
        exercito_invasor.selecionar_soldados_ativos()
              
        jogador.exercito.selecionar_soldados_ativos()
        
        quantidade_ativos = self.contar_ativos(jogador.exercito.exercito)
        if quantidade_ativos >0:
          array = {
                    "descricao": lambda: f"Os {Fore.RED}{len(exercito_invasor.exercito)} {raca.nome}s {Style.RESET_ALL} se preparam para lutar.\nCom o ataque, dos {Fore.GREEN}{len(jogador.exercito.exercito)}{Style.RESET_ALL}, conseguimos reunir {Fore.GREEN}{quantidade_ativos}{Style.RESET_ALL}.\nO que devemos fazer?",
                    "opcoes": [
                        (
                            f"Avançar",
                            lambda j: self.Combater(jogador.exercito,exercito_invasor,"Avançar",jogador,mapa)
                        ),
                        (
                            f"Manter posição",
                            lambda j: self.Combater(jogador.exercito,exercito_invasor,"Manter posição",jogador,mapa)
                        ),
                        (
                            f"Berserker",
                            lambda j: self.Combater(jogador.exercito,exercito_invasor,"Berserker",jogador,mapa)
                        )
                    ]
                }
          
          
        else:
          combate = Combate()

          array = {
            "descricao": lambda: f"O {Fore.RED}{exercito_invasor.nome}{Style.RESET_ALL}, um exercito de {Fore.RED} {len(exercito_invasor.exercito)} {raca.nome} {Style.RESET_ALL} marchão em sua direção.\nPor conta de não ter soldados preparados para o ataque, os invasores arrazaram, sem ressitencia, o reino.",
            "opcoes": [
              (
                f"Relatorio das perdas",
                lambda j: combate.Metodo_derrota(jogador,exercito_invasor,mapa)
              ),
            ]
          }
        
        print(array["descricao"]())
        for i, (texto_opcao, _) in enumerate(array["opcoes"]):
          print(f"{i+1}) {texto_opcao}")

        escolha = input("Sua decisão: ")

        #try:
        _, acao = array["opcoes"][int(escolha) - 1]
        acao(jogador)
        self.ativo = False
        print("Evento concluído com sucesso.")

