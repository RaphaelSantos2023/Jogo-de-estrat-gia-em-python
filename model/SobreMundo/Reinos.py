import random
from model.Animais.animal_sapiente import Animal_Sapien
from model.Meteriais.comida import Comida
from model.SobreMundo.tradicao import Tradicao
from model.Meteriais.construcao import (
    Quartel,Plantacao,Armazem_Comida,Armazem_materiais,Armazem,
    Templo,Posto_Comercio,Murro,Taverna,Casa,Cabana,Mina
)
from model.Meteriais.material import (Madeira,Pedra,Ferro,Cobre,Estanho,Prata,Ouro,Platina,Níquel,Titânio)
from colorama import Fore, Style, init
import time
import msvcrt

vestimenta = ['Toga', 'Túnica', 'Roupão', 'Vestido']

class Reino:
    def __init__(self, raca):
        self.nome = ""
        self.raca = raca
        self.rei = None
        self.ordens = []
        self.tem_Torre_vigilha = False
        
        self.ouro = 0
        self.populacao = 0
        self.Comida = 0
        self.animais = 0
        self.magia = 0
        self.exercito = Exercito()
        self.sacerdotes = []

        self.faccoes_reino = []
        self.Faccao_Rei = None

        self.Caracteristicas = []
        self.construcoes = []
        
        self.relacoes_reinos = []

        self.historia_reino = "Historia:\n"
        
        self.cidadaos = []
        self.cultura = None

    def gerarCultura(self,temperatura):
        self.cultura = Cultura()
        self.cultura.definir_vestimenta(temperatura)
        self.cultura.gerarNome(self)
        return self.cultura
    
    def gerarRei(self):
      rei = Animal_Sapien(self.raca.simbolo,100,5,random.randint(18,30),self.raca,0,0)
      rei.GerarPersonalidade()

      self.rei = rei

    def setCidadoes(self,array):
        self.cidadaos = array
      
    def gerar_nome(self):
        nomes_reinos = [
            "Cidadela Sombria",
            "Fortaleza de Ferro",
            "Bastião do Norte",
            "Refúgio da Alvorada",
            "Castelo de Cinzas",
            "Solar das Brumas",
            "Muralha Eterna",
            "Cúpula de Jade",
            "Torre de Vigília",
            "Domínio de Sangue",
            "Círculo de Pedra",
            "Guarnição do Oeste",
            "Vale Proibido",
            "Trono do Trovão",
            "Corte Esquecida",
            "Forte das Tempestades",
            "Reduto do Fim",
            "Templo de Gelo",
            "Pico da Vigília",
            "Encosta dos Reis"
        ]
        nomes_possiveis = ["Aeterna", "Valoria", "Eldoria", "Thaloria", "Celestia", "Astraea", "Luminara", "Serenara", "Radiantia", "Aurora","Avernia", "Drakonia", "Valemont", "Zarath", "Tarnhelm"]

        self.nome = random.choice(nomes_reinos) + " de " + random.choice(nomes_possiveis)

    def getConstrucoes(self):
        quantidade = random.randint(10,90)
        array = [Quartel,Armazem_Comida,Armazem_materiais,Armazem,
    Templo,Posto_Comercio,Murro,Taverna,Casa,Cabana,Mina]
        
        materiais = [Madeira,Pedra,Ferro,Cobre,Estanho,Prata,Ouro,Platina,Níquel,Titânio]
        pesos = [0.8, 0.8, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]

        construcoes = random.choices(array,k=quantidade)

        for construcao in construcoes:
            material = random.choices(materiais, weights=pesos, k=1)[0]
            self.construcoes.append(construcao(0,0,material()))

    def criar_faccao_rei(self):
        faccao = Faccoes()
        faccao.criar_Faccao(self.raca,"Por direito",self)
        faccao.lider = self.rei
        
        self.Faccao_Rei = faccao

    def gerar_valores_aleatorios(self):
        
        caracteristicas_possiveis = ["Beligerante","Diplomatico","Religioso","Comerciante","Escrevista"]
      
        self.gerar_nome()
        self.gerarRei()
        
        
        self.ouro = random.randint(100, 300)
        self.populacao = random.randint(20, 100)
        self.Comida = random.randint(50, 200)
        self.Equipamento_militar = random.randint(1,self.populacao//2)
        self.exercito.CriarExercito(self.raca,self)

        self.getConstrucoes()
        self.criar_faccao_rei()
        self.Caracteristicas = random.choice(caracteristicas_possiveis)
        
    def calcular_total_comida(self):
        total = 0
        for construcao in self.construcoes:
            if construcao.nome == "Armazem de comida":
                for item in construcao.inventario:
                    if isinstance(item["Nome"], Comida):
                        total += item["Quantidade"]
        return total

    def calcular_total_animal(self):
        total = 0
        for construcao in self.construcoes:
            if construcao.nome == "Armazem":
                for item in construcao.inventario:
                    total += item["Quantidade"]
        return total

    def criarRelacao(self, reino):
        #reinos["Reino"] == self.reino:
        #reinos.["Relacao"]
        afinidade = random.randint(-100, 100)
        if afinidade > 70:
            relacao = "Aliado"
        elif afinidade > 0:
            relacao = "Neutro"
        else:
            relacao = "Inimigo"
        
        self.relacoes_reinos.append({"Reino": reino, "Afinidade":afinidade})
    
    def adicionar_cidadao(self, cidadao):
        self.cidadaos.append(cidadao)
    
    def criarReino(self,ouro,populacao,comida,Equipamento_militar,nome_reino):

        self.gerar_nome()
        self.gerarRei()
        
        self.ouro = ouro
        self.populacao = populacao
        self.Comida = comida
        self.Equipamento_militar = Equipamento_militar
        self.nome = nome_reino
        self.Caracteristicas = "nenhum"
    
    def MostratStatusCidadaos(self):
        feridos= 0
        doentes = 0
        felicidade_geral = 0

        for cidadao in self.cidadaos:
            if cidadao.Ferido == True:
                feridos += 1
            if cidadao.Doente == True:
                doentes += 1
            felicidade_geral += cidadao.felicidade
        
        quantidade_cidadao = len(self.cidadaos)

        if quantidade_cidadao == 0:
            print("Nenhum cidadão na cidade.")
            return
    
        felicidade_media= int(felicidade_geral/quantidade_cidadao)

        if felicidade_media < 20:
            humor = f"{Fore.RED}Revoltados"
        elif felicidade_media < 40:
            humor = f"{Fore.LIGHTBLACK_EX}Tristes"
        elif felicidade_media < 60:
            humor = f"Indiferentes"
        elif felicidade_media < 80:
            humor = f"{Fore.LIGHTGREEN_EX}Felizes"
        else:
            humor = f"{Fore.LIGHTYELLOW_EX}Eufóricos"
        
        print(f"• Quantidade total: {quantidade_cidadao}")
        print(f"• Quantidade de feridos: {Fore.LIGHTRED_EX}{feridos}")
        print(f"• Quantidade de doentes: {Fore.LIGHTMAGENTA_EX}{doentes}")
        print(f"• Felicidade média: {humor}")

    def MostrarRelacoes(self):
        txt = "\n\nRelações com outros reinos:\n"
        for relacao in self.relacoes_reinos:

            if relacao['Afinidade'] >= 50:
                relacao_caso = f"{Fore.GREEN}Aliado"
            elif relacao['Afinidade'] >= 0:
                relacao_caso = f"{Fore.LIGHTCYAN_EX}Neutro"
            else:
                relacao_caso = f"{Fore.RED}Inimigo"
            
            if isinstance(relacao['Nome'],Reino):
                cor_nome = Fore.LIGHTBLACK_EX
            else:
                cor_nome = Fore.LIGHTRED_EX

            txt += f"• {cor_nome}{relacao['Nome'].nome}{Style.RESET_ALL}, Relacao: {relacao_caso}{Style.RESET_ALL}, Numero: {relacao['Afinidade']}\n"
        return txt
    
    def Mostrar_Faccoes(self):
        txt = "• Facções:"
        if len(self.faccoes_reino) != 0:
            for faccao in self.faccoes_reino:
                txt += f"\n- {faccao['Nome'].nome}, Lider: {faccao['Nome'].lider.nome}, Numero: {faccao['Afinidade']}"
        else:
            txt += " Nenhuma"
        return txt

    def Descricao(self):
        descricao = f"🏰 **{self.nome}**\n"
        descricao += f"• Raça dominante: {self.raca.nome}\n"
        descricao += f"• Soberano atual: {self.rei.nome}\n"
        descricao += f"• População total: {self.populacao} habitantes\n"
        descricao += f"• Tesouro do reino: {self.ouro} peças de ouro\n"
        descricao += f"• Reservas alimentares: {self.Comida} unidades de comida\n"
        descricao += f"• Estruturas erguidas: {len(self.construcoes)} construções\n"
        descricao += f"• Exército ativo: {len(self.exercito.exercito)} soldados\n"
        descricao += f"• Tendência cultural: {self.Caracteristicas}\n"
        
        if self.cultura:
            descricao += f"• Cultura predominante: {self.cultura.nome}\n"
            descricao += f"  - Estilo de vestimenta: {self.cultura.vestimenta}\n"
            descricao += f"  - Tradições: {self.cultura.tradicao.Descricao()}\n"
            descricao += f"• Facção chefe: {Fore.GREEN}{self.Faccao_Rei.nome}{Style.RESET_ALL}\n"

        descricao += self.Mostrar_Faccoes()
        descricao += self.MostrarRelacoes()
        descricao += self.historia_reino
        return descricao

class Cultura:
    def __init__(self):
        self.nome = ''
        self.tradicao = Tradicao()
        self.tradicao.formarTradicao()
        self.vestimenta = ''

    def definir_vestimenta(self, temperatura):
        dados = temperatura[0]  # Pega o dicionário dentro da lista
        temp_max = dados["tempMax"]
        temp_min = dados["tempMin"]

        if temp_max > 35:
            self.vestimenta = (
                "Roupas leves e soltas, feitas de tecidos respiráveis como linho, "
                "com acessórios para proteção contra o sol forte."
            )
        elif temp_max > 20:
            self.vestimenta = (
                "Roupas versáteis e adaptáveis, incluindo mantos removíveis e tecidos "
                "de média espessura para conforto em variações climáticas."
            )
        elif temp_max > 10:
            self.vestimenta = (
                "Vestimentas típicas de clima temperado, combinando proteção leve com "
                "isolamento térmico moderado para dias frescos."
            )
        else:
            self.vestimenta = (
                "Roupas pesadas e camadas múltiplas, usando peles e tecidos grossos "
                "para isolamento térmico em ambientes frios."
            )
    
    def gerarNome(self,reino):
        self.nome = f"Cultura {reino.nome}"
    
    def Descricao(self):
        descricao = (
            f"--- Cultura: {self.nome} ---\n"
            f"Vestimenta típica: {self.vestimenta}\n\n"
            f"Tradições e símbolos:\n{self.tradicao.Descricao()}\n"
        )
        return descricao

prefixos = ["Batalhão", "Bando de Guerra", "Gangue", "Companhia", "Milícia", "Legião", "Tropa", "Clã", "Esquadrão", "Ordem"]
sufixos = ["do Falcão", "Saqueadores de Corpos", "da Morte", "dos Sem Rosto", "das Sombras", "do Machado Rubro", "de Ferro", "da Tempestade", "do Vazio", "dos Ossos"]

class Exercito:

    def __init__(self):
        self.nome = random.choice(prefixos) + " " + random.choice(sufixos)
        self.exercito = []
        self.preparo = 1

    def CriarSoldado(self,raca):
        vida = random.randint(1,10)
        dano = random.randint(1,5)
        idade = random.randint(18, 30)
        soldado = Animal_Sapien(raca.simbolo,vida,dano,idade,raca,0,0)
        soldado.servico_militar = True
        return soldado
    
    def CriarExercito(self,raca,reino):
        self.Quantidade_pessoas = random.randint(2, reino.populacao // 2)
        exercito = []
        for i in range(self.Quantidade_pessoas):
            Soldado = self.CriarSoldado(raca)
            exercito.append({"Soldado":Soldado,"Ativo": False})
        self.exercito = exercito
    
    def CriarExercito_Invasao(self,raca,reino):
        Quantidade_pessoas = random.randint(2, len(reino.cidadaos))
        
        for i in range(Quantidade_pessoas):
            Soldado = self.CriarSoldado(raca)
            self.exercito.append({"Soldado":Soldado,"Ativo": False})
    
    def selecionar_soldados_ativos(self):
        selecionados = []

        # Garante que a porcentagem vai de 50% até 100% baseado no preparo
        preparo_max = 10  # pode ajustar conforme escala desejada
        percentual = 0.5 + min(self.preparo / preparo_max, 0.5)  # vai de 0.5 a 1.0

        quantidade_ativa = int(len(self.exercito) * percentual)

        # Seleciona soldados únicos aleatoriamente
        candidatos = random.sample(self.exercito, min(quantidade_ativa, len(self.exercito)))
        
        for soldado in candidatos:
            if soldado["Soldado"].Ferido == False and soldado["Soldado"].Doente == False:
                soldado["Ativo"] = True
                selecionados.append(soldado)
        
        if selecionados != []:
            # Define o restante como inativo
            for soldado in self.exercito:
                if soldado not in selecionados:
                    soldado["Ativo"] = False
                    selecionados.append(soldado)

        return selecionados
    
    def Treinar_exercito(self):
        chance = random.random()
        if chance > 0.6:
            self.preparo += 1
            print("O exercito melhorou seu preparo")
        else:
            print("O treino não foi muito frutifero")

class Combate:
    def __init__(self):
        self.timer = 0.5

        self.moral_inimigo = 100
        self.Energia_inimigo = 100

        self.moral_jogador = 100
        self.Energia_jogador = 100
    
    def getch(self):
        return msvcrt.getch().decode('utf-8')

    def rodada(self, reino, inimigo, tatica_jogador, tatica_inimigo,jogador,mapa):

        def Metodo_derrota():
            ouro = 0
            if jogador.ouro > 0:
                ouro = random.randint(1,jogador.ouro//3)
                jogador.ouro -= ouro
                
            total = jogador.calcular_total_comida()
            quantidade_comida = random.randint(total // 6, total // 5)

            construcoes_destruidas = 0
            for construcao in jogador.construcoes:
                if construcao.nome != "Armazem de comida" and construcao.nome != "Armazem de materiais":
                    construcao.vida -= media_inimigo
                    if construcao.vida <= 0:
                        construcoes_destruidas += 1
                        mapa[construcao.x][construcao.y] = "_"
                        jogador.construcoes.remove(construcao)
                
            print(f"\n{Fore.RED + Style.BRIGHT}======|            DERROTA           |======{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}Você perdeu {ouro} de ouro.")
            print(f"{Fore.MAGENTA}Você perdeu {quantidade_comida} de comida.")
            print(f"{Fore.MAGENTA}{construcoes_destruidas} construções foram destruídas.{Style.RESET_ALL}")

            self.tirar_comida(quantidade_comida,jogador)
        
        if inimigo != [] and reino != []:
            resultado = self.resultado_tatica(tatica_jogador, tatica_inimigo)
            print(f"\n{Fore.YELLOW + Style.BRIGHT}======|      A BATALHA COMEÇOU!      |======{Style.RESET_ALL}\n")

            if resultado == 1:
                self.moral_inimigo -= 10
                self.Energia_inimigo -= 5
                print(f"{Fore.GREEN}>> Jogador levou vantagem tática!")
            elif resultado == -1:
                self.moral_jogador -= 10
                self.Energia_jogador -= 5
                print(f"{Fore.RED}>> Inimigo levou vantagem tática!")
            else:
                print(f"{Fore.CYAN}>> Táticas se equilibraram.")
            
            media_jogador = self.definir_vitoria(reino)
            media_inimigo = self.definir_vitoria(inimigo)
            
            print(f"{Fore.RED}---> Dano Inimigo: {int(media_inimigo)}\n{Fore.GREEN}---> Dano Jogador: {int(media_jogador)} {Style.RESET_ALL} {Fore.YELLOW}")
            print("\n")
            print(f"{Fore.YELLOW}===>>> {Fore.RED}Inimigo: {int(self.moral_inimigo)} {Fore.YELLOW}x {Fore.GREEN}{int(self.moral_jogador)} Jogador{Style.RESET_ALL} {Fore.YELLOW}<<<===\n")
            
            resultado = self.Resultado()
            
            while resultado == None:

                balanca_jogador = random.random()
                evento_especial_chances = random.random()
                evento_especial_chances_inimigo = random.random()

                time.sleep(self.timer)
                
                balanca_inimigo = 1 - balanca_jogador 
                            
                if balanca_jogador > balanca_inimigo:
                    self.moral_inimigo -= media_jogador
                    self.Energia_inimigo -= 5
                    print(f"{Fore.GREEN}-> Seu exército pressiona e força o inimigo a recuar!{Style.RESET_ALL}")

                elif balanca_jogador < balanca_inimigo:
                    self.moral_jogador -= media_inimigo
                    self.Energia_jogador -= 5
                    print(f"{Fore.RED}-> O inimigo avança! Seu exército está sendo pressionado.{Style.RESET_ALL}")

                else:
                    print(f"{Fore.CYAN}-> Forças equilibradas. Nenhum avanço significativo.{Style.RESET_ALL}")
                
                if evento_especial_chances >= 0.5 and reino:
                    self.EventoEspecial(reino,inimigo,media_jogador,media_inimigo,"Jogador",Fore.LIGHTBLUE_EX,Fore.RED)
                
                if evento_especial_chances_inimigo >= 0.5 and inimigo:
                    self.EventoEspecial(inimigo,reino,media_inimigo,media_jogador,"Inimigo",Fore.LIGHTMAGENTA_EX,Fore.GREEN)
            
                print(f"{Fore.YELLOW}===>>> {Fore.RED}Inimigo: {int(self.moral_inimigo)} {Fore.YELLOW}x {Fore.GREEN}{int(self.moral_jogador)} Jogador{Style.RESET_ALL} {Fore.YELLOW}<<<===\n")
                #print("\n")
                resultado = self.Resultado()

            if not resultado:
                ouro = random.randint(50,100)
                comida_Add = random.randint(20,50)

                print(f"\n{Fore.YELLOW + Style.BRIGHT}======|            VITÓRIA!          |======{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Você saqueou {ouro} moedas de ouro\nVocê coletou {comida_Add} unidades de comida.{Style.RESET_ALL}")
                
                self.add_comida(comida_Add,jogador)
                jogador.ouro += ouro

            else:
                Metodo_derrota()
                
        else:
            Metodo_derrota()
        
        self.desativer_Exercito(reino)

    def desativer_Exercito(self,exercito):
        for soldado in exercito:
            soldado['Ativo'] = False
    
    def EventoEspecial(self,jogador,inimigo,media_jogador,media_inimigo,tipo,fore,fore_inimigo):

        if not jogador or not inimigo:
            return  # evita erro se algum lado estiver sem soldados
    
        soldado = random.choice(jogador)
        soldadoInimigo = random.choice(inimigo)

        if soldado['Soldado'].forca >= soldadoInimigo['Soldado'].destreza or soldado['Soldado'].destreza >= soldadoInimigo['Soldado'].forca:
            self.Dano_especial(tipo,soldado['Soldado'])

            print(f"{Style.BRIGHT}{fore}|__ {soldado['Soldado'].nome} realiza um ataque especial em {fore_inimigo}{soldadoInimigo['Soldado'].nome}!{Style.RESET_ALL}")
            soldado['Soldado'].Atacar(soldadoInimigo['Soldado'])
            if soldadoInimigo['Soldado'].Ferido != True:
                soldadoInimigo['Soldado'].Ferido = True
            
            if soldadoInimigo['Soldado'].vida<= 0:
                print(f"{Fore.RED}|_____ {soldadoInimigo['Soldado'].nome} foi incapacitado!{Style.RESET_ALL}")
                soldadoInimigo['Ativo'] = False
                soldadoInimigo['Soldado'].acao_momento = ['Trabalhar']
                if len(inimigo)>0:
                    media_inimigo = self.definir_vitoria(inimigo)
        else:
            print(f"{Fore.LIGHTBLACK_EX}|__ {Style.BRIGHT}{fore}{soldado['Soldado'].nome}{Style.RESET_ALL}{Fore.LIGHTBLACK_EX} tentou um ataque especial, mas foi impedido.{Style.RESET_ALL}")
    
    def Dano_especial(self,tipo,soldado):
        match tipo:
            case "Jogador":
                self.moral_inimigo -= soldado.dano
                self.Energia_jogador -= 5
            case "Inimigo":
                self.moral_jogador -= soldado.dano
                self.Energia_inimigo -= 5
    
    def tirar_comida(self,quantidade,reino):
        for construcao in reino.construcoes:
            if construcao.nome == "Armazem de comida":
                for item in construcao.inventario:
                    if isinstance(item["Nome"], Comida) and item['Quantidade'] > 0 and quantidade >0 :
                        quantidade_tirada = random.randint(1,item['Quantidade'])
                        item["Quantidade"] -= quantidade_tirada
                        quantidade -= quantidade_tirada
    
    def add_comida(self,quantidade,reino):
        for construcao in reino.construcoes:
            if construcao.nome == "Armazem de comida":
                for item in construcao.inventario:
                    if isinstance(item["Nome"], Comida) and quantidade >0 :
                        quantidade_tirada = random.randint(0,item['Quantidade'])
                        item["Quantidade"] += quantidade_tirada
                        quantidade -= quantidade_tirada 
    
    def definir_vitoria(self, exercito):
        dano = 0
        def definir_n(exercito):
            numero = 0
            for soldado in exercito:
                if soldado["Ativo"]:
                    numero +=1
            return numero
        
        n = definir_n(exercito)

        for p in exercito:
            if p['Ativo']:
                dano += p['Soldado'].dano

        medias = dano/len(exercito)
        return medias


    def resultado_tatica(self, tatica1, tatica2):
        if tatica1 == tatica2:
            return 0  # empate
        elif (tatica1 == "Berserker" and tatica2 == "Manter posição") or \
            (tatica1 == "Manter posição" and tatica2 == "Avançar") or \
            (tatica1 == "Avançar" and tatica2 == "Berserker"):
            return 1  # tatica1 vence
        else:
            return -1  # tatica2 vence
    
    def Resultado(self):
        if self.moral_inimigo <=0 :
            return False
        elif self.moral_jogador <= 0:
            return True
        return None

faccoes_formatadas = [
    {"nome": "Irmandade", "sobrenome": "Varran"},
    {"nome": "Casa", "sobrenome": "Durnhald"},
    {"nome": "Mantos", "sobrenome": "de Selvaria"},
    {"nome": "Conclave", "sobrenome": "de Halbor"},
    {"nome": "Aliança", "sobrenome": "Vorstag"},
    {"nome": "Asas", "sobrenome": "de Mirkallen"},
    {"nome": "Clã", "sobrenome": "Orvalth"},
    {"nome": "Círculo", "sobrenome": "dos Nove Tronos"},
    {"nome": "Véus", "sobrenome": "de Thalindra"},
    {"nome": "Cavaleiros", "sobrenome": "de Brannhölm"},
    {"nome": "Casa", "sobrenome": "Karethor"},
    {"nome": "Julgo", "sobrenome": "de Farendir"},
    {"nome": "Senhores", "sobrenome": "do Véu Rubro"},
    {"nome": "Ordem", "sobrenome": "de Eldenmark"},
    {"nome": "Voz", "sobrenome": "de Nurthein"},
    {"nome": "Conselho", "sobrenome": "dos Espinhos"},
    {"nome": "Corte", "sobrenome": "Esmeralda de Vilkar"},
    {"nome": "Lâminas", "sobrenome": "de Droskar"},
    {"nome": "Chama", "sobrenome": "de Anvar"},
    {"nome": "Pacto", "sobrenome": "da Lua Quebrada"}
]


class Faccoes:
    def __init__(self):
        self.nome = random.choice(faccoes_formatadas)["nome"] + " " + random.choice(faccoes_formatadas)["sobrenome"]
        self.lider = None
        self.raca = None
        self.faccoes_reino = []
        self.tipo = ""
        self.exercito = Exercito()

    def criar_lider(self):
        lider = Animal_Sapien(self.raca.simbolo,100,5,random.randint(18,30),self.raca,0,0)
        lider.GerarPersonalidade()
        self.lider = lider

    def criar_Faccao(self,raca,tipo,reino):
        self.raca = raca
        self.tipo = tipo

        self.criar_lider()
        self.exercito.CriarExercito(self.raca,reino)
