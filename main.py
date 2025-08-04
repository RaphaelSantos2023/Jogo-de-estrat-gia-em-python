from model.SobreMundo.Religiao import Religiao
from model.Meteriais.construcao import (
    Armazem_Comida, ConstruirCabana, ConstruirPlantacao,
    Armazem,ConstruirCasa,ConstruirTaverna,ConstruirTemplo,
    ConstruirArmazem,ConstruirArmazem_Comida,ConstruirArmazem_materiais,ConstruirQuartel,Quartel,
    Armazem_materiais, Plantacao,Demanda_tempo,ConstruirTorre,ConstruirMina)
from model.Meteriais.comida import (
    cultivo_maca, cultivo_trigo, cultivo_laranja, cultivo_uva,
    cultivo_morango, cultivo_tomate, cultivo_cenoura, cultivo_alface,
    cultivo_batata, cultivo_abobora, cultivo_pepino,
    cultivo_beterraba, cultivo_rabanete, cultivo_mandioca, cultivo_inhame,
    cultivo_cebola, cultivo_abacaxi, cultivo_melancia, cultivo_manga,
    cultivo_pimentao, cultivo_espinafre, cultivo_coco, cultivo_azeitona
)
from colorama import Fore, Style, init
from model.SobreMundo.Racas import Raca, Criatura
from control import Control
from model.Animais.animal_sapiente import personalidade
from model.SobreMundo.mundo import Relogio
from model.SobreMundo.Reinos import Equipe_exploracao
import select
from model.Estoque.estoque import Membro_espedicao
from model.Animais.profisoes import Minerador, Lenhador, Pescador, Fazendeiro
#from construcoes import *

    
init(autoreset=True)

import os
import sys

import random
import msvcrt
import time

class main:
    def __init__(self):
        self.control = None
        self.Profissoes = [Minerador(),Lenhador(),Pescador(),Fazendeiro()]

        self.regiao_jogador = None

        self.matriz = []
        self.tamanho = 30
        self.Ano = 0
        self.relogio = Relogio()


        self.QuantidadeHumanos = 8
        self.humanos = []
        self.reino_Jogador = None

        self.QuantidadeObjetos = random.randint(self.tamanho, self.tamanho * 2)
        self.Objetos = []

        self.array_cultivo = [
            cultivo_maca, cultivo_trigo, cultivo_laranja, cultivo_uva,
        cultivo_morango, cultivo_tomate, cultivo_cenoura, cultivo_alface,
        cultivo_batata, cultivo_abobora, cultivo_pepino,
        cultivo_beterraba, cultivo_rabanete, cultivo_mandioca, cultivo_inhame,
        cultivo_cebola, cultivo_abacaxi, cultivo_melancia, cultivo_manga,
        cultivo_pimentao, cultivo_espinafre, cultivo_coco, cultivo_azeitona
        ]

        self.timer = 0.5

    def getch(self):
        return msvcrt.getch().decode('utf-8')

    if os.name == 'nt':

        def input_disponivel(self):
            return msvcrt.kbhit()
    else:
        import select

        def input_disponivel(self):
            return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

    def atualizarMapa( self,matriz, tamanho):
        reino = self.reino_Jogador
        Mapa = [linha[:] for linha in matriz]

        self.barra_principal(reino,self.relogio)
        
        self.control.AcoesMapa(reino,Mapa,matriz, tamanho, self.relogio,self.pausado,self.regiao_jogador)

        MapaStr = "\n".join(" ".join(linha) for linha in Mapa)
        print(MapaStr)

        for i in range(len(self.reino_Jogador.cidadaos)):
            for j in range(i + 1, len(self.reino_Jogador.cidadaos)):
                h1 = self.reino_Jogador.cidadaos[i]
                h2 = self.reino_Jogador.cidadaos[j]
                if self.control.VerificarProximidade(h1, h2) and h2.acao_momento[0] == "Socializar" and h1.explorando is False and h2.explorando is False and h1.acao_momento[0] == "Socializar":
                    H1 = h1
                    h1.Socializar(h2,self.reino_Jogador)
                    h2.Socializar(H1,self.reino_Jogador)

        self.barra_inferior(reino)

        self.relogio.passar_tempo(self.reino_Jogador.cidadaos)

    def barra_principal(self,reino,relogio):
        print(f"{Fore.GREEN}{'═'*60}")
        print(f"{Fore.YELLOW}Reino: {reino.nome}{Style.RESET_ALL}\n{'Data':<10} {relogio.mostrar_data()}   {'Horas':<15} {relogio.mostrar_hora()}")
        print(f"{'═'*60}{Style.RESET_ALL}")

    def barra_inferior(self,reino):
        print(f"{'═'*60}{Style.RESET_ALL}")
        print(f"{'Civis':<10} {reino.populacao}  {'Ouro:':<10} {reino.ouro}   {'Comida:':<10} {reino.calcular_total_comida()}   {'Magia:':<9} {reino.magia}")
        print(f"{'═'*60}{Style.RESET_ALL}")

    def escutar_tecla(self):
        while True:
            tecla = self.getch()
            if tecla == ' ':
                self.pausado = not self.pausado
                if self.pausado:
                    self.menu_jogo()

    def RunGame(self):
        
        self.pausado = False
        Anos = 500
        while self.relogio.ano <= Anos:
            self.limpar_tela()
            if not self.pausado:
                self.atualizarMapa(self.matriz, self.tamanho)
                time.sleep(self.timer)
                if self.input_disponivel():
                    tecla = self.getch()
                    if tecla == ' ':
                        self.pausado = True
            else:
                self.menu_jogo()
                self.pausado = False

    def menu_jogo(self):
        while True:
            self.limpar_tela()
            self.tituloDoMenu("🏰 Menu do Reino")
            print(f"{Fore.CYAN}1.{Style.RESET_ALL} 👥 Cidadãos")
            print(f"{Fore.CYAN}2.{Style.RESET_ALL} 🛡️ Ordens")
            print(f"{Fore.CYAN}3.{Style.RESET_ALL} 📜 Serviços especiais")
            print(f"{Fore.CYAN}4.{Style.RESET_ALL} 🏗️ Construções")
            print(f"{Fore.CYAN}5.{Style.RESET_ALL} 🌍 Ver o mundo")
            print(f"{Fore.CYAN}6.{Style.RESET_ALL} 🔙 Voltar ao jogo")
            print(f"{Fore.GREEN}{'═'*60}{Style.RESET_ALL}")

            #try:
            opcao = int(input(f"{Fore.YELLOW}Escolha uma opção: {Style.RESET_ALL}"))
            self.limpar_tela()
            match opcao:
                case 1:
                    self.cidadaoMenu()
                case 2:
                    self.ordemMenu()
                case 3:
                    self.menu_servicos_especiais()
                case 4:
                    self.construcaoMenu()
                case 5:
                    self.verMundo()
                case 6:
                    break
                case _:
                    print("Opção inválida.")
                    self.getch()
            #except:
                #print("Entrada inválida.")
                #getch()

    def tituloDoMenu(self,text):
        print(f"{Fore.GREEN}{'═'*60}")
        print(f"{Fore.YELLOW}{text.center(60)}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'═'*60}{Style.RESET_ALL}")

    def SubMenuTitulo(self,text):
        print(f"\n{Fore.YELLOW}{text}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'-'*60}{Style.RESET_ALL}")

    def cidadaoMenu(self):
        while True:
            self.limpar_tela()
            self.tituloDoMenu("👥 Menu de Cidadãos")
            print(f"{Fore.CYAN}1.{Style.RESET_ALL} 🔍 Ver cidadão específico")
            print(f"{Fore.CYAN}2.{Style.RESET_ALL} 🤝 Relações")
            print(f"{Fore.CYAN}3.{Style.RESET_ALL} 🔍 Ver Status")
            print(f"{Fore.CYAN}4.{Style.RESET_ALL} 🔙 Voltar")
            print(f"{Fore.GREEN}{'-'*40}{Style.RESET_ALL}")

            #try:
            opcao = int(input(f"{Fore.YELLOW}Escolha uma opção: {Style.RESET_ALL}"))
            self.limpar_tela()
            match opcao:
                case 1:
                    self.verDadoCidadao()
                case 2:
                    self.ListarCidadaos()
                case 3:
                    self.MostarStatus()
                case 4:
                    break
                case _:
                    print("Opção inválida.")
            #except:
                #print("Entrada inválida.")
                #self.getch()

    # ---> Lista de cidadãos

    def printCidadao(self):
        cidadaos = []
        for i, h in enumerate(self.reino_Jogador.cidadaos):
            if not h.explorando:
                cidadaos.append(h)

        for i, h in enumerate(cidadaos):
            print(f"{Fore.CYAN}{i}{Style.RESET_ALL}. {h.nome}")
        print(f"{Fore.RED}{len(cidadaos)}{Style.RESET_ALL}. Voltar")
        print(f"{Fore.GREEN}{'-'*40}{Style.RESET_ALL}")

        return cidadaos

    def verDadoCidadao(self):
        self.SubMenuTitulo("🔍 Escolha um cidadão para ver os dados")
        cidadaos = self.printCidadao()
        #try:
        opcao = int(input('R: '))
        if opcao == len(cidadaos):
            return
        self.limpar_tela()
        self.DescricaoCidadao(opcao)
        self.getch()
        #except:
            #print("Entrada inválida.")
            #self.getch()

    def DescricaoCidadao(self,id):
        print(f"{Fore.BLUE}📋 Dados de {self.reino_Jogador.cidadaos[id].nome}:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'-'*40}{Style.RESET_ALL}")
        print(self.reino_Jogador.cidadaos[id].Descricao())

    def ListarCidadaos(self):
        self.SubMenuTitulo(f"👥 Lista de Cidadãos: {len(self.reino_Jogador.cidadaos)}")
        cidadaos = self.printCidadao()
        #try:
        opcao = int(input(f"{Fore.YELLOW}Escolha um cidadão para ver relações: {Style.RESET_ALL}"))
        if opcao == len(cidadaos):
            print("Voltando...")
            self.getch()
        else:
            self.limpar_tela()
            self.mostrarRelacoes(opcao,cidadaos)
            self.getch()
        #except:
            #print("Entrada inválida.")
            #getch()
    def MostarStatus(self):

        self.limpar_tela()
        self.SubMenuTitulo(f"👥 Status do reino: ")
        self.reino_Jogador.MostratStatusCidadaos()
        print(f"{Fore.GREEN}{'-'*40}{Style.RESET_ALL}")
        self.getch()
        

    def mostrarRelacoes(self,id,cidadaos):
        print(f"{Fore.BLUE}🤝 Relações de {cidadaos[id].nome}:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}{'-'*40}{Style.RESET_ALL}")
        if len(cidadaos[id].conhecidos) > 0:
            for i, relacao in enumerate(cidadaos[id].conhecidos):
                pessoa, pontos, status = relacao
                print(f"[{i}] {pessoa} | Afinidade: {pontos} | Status: {status}")
        else:
            print('Nenhuma relação encontrada.')

    # ---> Lista de Ordem

    def ordemMenu(self):
        while True:
            self.tituloDoMenu("🛡️ Menu de Ordens")
            print(f"{Fore.CYAN}1{Style.RESET_ALL}. Designar Profissão")
            print(f"{Fore.CYAN}2{Style.RESET_ALL}. Criar Ordens")
            print(f"{Fore.RED}3. Voltar")

            #try:
            opcao = int(input('R: '))
            self.limpar_tela()
            match opcao:
                case 1:
                    self.DesignarProfissao()
                case 2:
                    self.DarOrdens()
                case 3:
                    break
            #except:
                #print("Entrada inválida.")
                #self.getch()

    def DesignarProfissao(self):
        self.limpar_tela()
        self.tituloDoMenu("👥 Cidadãos do Reino")
        cidadaos = self.printCidadao()

        try:
            opcao = int(input('Escolha um cidadão: '))
            if opcao == len(cidadaos):
                print("Voltando...")
            else:
                self.limpar_tela()
                self.definirProfissao(opcao,cidadaos)
        except:
            print("Entrada inválida.")
            self.getch()

    def definirProfissao(self,cidadao,cidadaos):
        self.tituloDoMenu("🧰 Designar Profissão")
        for i in range(len(self.Profissoes)):
            print(f"[{Fore.CYAN}{i}{Style.RESET_ALL}] {self.Profissoes[i].nome}")
        print(f"[{Fore.RED}{len(self.Profissoes)}{Style.RESET_ALL}] Voltar")

        try:
            opcao = int(input('R: '))
            if opcao == len(self.Profissoes):
                print("Voltando...")
            else:
                self.limpar_tela()
                print(f"{Fore.BLUE}Profissão de {cidadaos[cidadao].nome}:{Style.RESET_ALL}")
                print("-" * 40)
                self.control.DesginarCidadaoAProfissao(opcao, cidadao, self.Profissoes, cidadaos)
                self.getch()
        except:
            print("Entrada inválida.")
            self.getch()

    def DarOrdens(self):
        self.limpar_tela()
        self.tituloDoMenu("📜 Gerenciar Ordens")

        print(f"{Fore.CYAN}1{Style.RESET_ALL}. Adicionar ordem")
        print(f"{Fore.CYAN}2{Style.RESET_ALL}. Ver ordem")
        print(f"{Fore.CYAN}3{Style.RESET_ALL}. Cancelar ordem")
        print(f"{Fore.RED}4{Style.RESET_ALL}. Voltar")

        #try:
        opcao = int(input('R: '))
        match opcao:
            case 1:
                self.definirTipoTrabalho()
            case 2:
                self.verOrdens()
                self.getch()
            case 3:
                self.cancelarOrdem()
                print("Todas as ordens foram canceladas.")
                self.getch()
            case 4:
                return
        #except:
            #print("Entrada inválida.")
            #self.getch()

    def definirTipoTrabalho(self):
        intencao = "Area"
        self.limpar_tela()
        max_x,min_x,max_y,min_y = self.selectionar_area()
        self.colocarOrdem(intencao,max_y,max_x,min_y,min_x)
        
    def colocarOrdem(self,intencao,max_x=-1,max_y=-1,min_x=-1,min_y=-1):
        self.limpar_tela()
        Profissoes = self.mostrarOrdens()
        #try:
        opcao = int(input('Escolha uma ordem: '))
        if opcao == len(Profissoes):
            print("Voltando...")
        else:
            self.limpar_tela()
            ordem = Profissoes[opcao]
            print(f"ordem = Profissoes[opcao] {ordem}")
            for cidadao in self.reino_Jogador.cidadaos:
                if type(cidadao.profissos[0]) == type(ordem):
                    cidadao.acao_momento[0] = "Trabalhar"
                    cidadao.intencao =intencao

                    cidadao.max_x = max_x
                    cidadao.min_x = min_x
                    cidadao.max_y = max_y
                    cidadao.min_y = min_y

                print(f"{cidadao.nome} foi designado para {ordem.nome}")
            self.reino_Jogador.ordens.append(ordem)
            print(f"✅ Ordem de {ordem.nome} adicionada com sucesso.")        
            self.getch()
        #except:
            #print("Entrada inválida.")
            #self.getch()

    def  selectionar_area(self):
        self.exibir_mapa_com_coordenadas(self.matriz)
        x1 = int(input(f"{Fore.BLUE}x1{Style.RESET_ALL}: "))
        x2 = int(input(f"{Fore.BLUE}x2{Style.RESET_ALL}: "))
        y1 = int(input(f"{Fore.GREEN}y1{Style.RESET_ALL}: "))
        y2 = int(input(f"{Fore.GREEN}y2{Style.RESET_ALL}: "))
        if x1>x2 :
            max_x = x1
            min_x = x2
        else:
            max_x = x2
            min_x = x1
        
        if y1>y2 :
            max_y = y1
            min_y = y2
        else:
            max_y = y2
            min_y = y1
        
        return max_x,min_x,max_y,min_y

    def verOrdens(self):
        self.tituloDoMenu("🔎 Ordens Ativas")
        for cidadao in self.reino_Jogador.cidadaos:
            if cidadao.acao_momento[0] == "Trabalhar":
                print(f"{cidadao.nome} - {cidadao.profissos[0].acao}")
        print("-" * 40)

    def cancelarOrdem(self):
        for ordem in self.reino_Jogador.ordens:
            for cidadao in self.reino_Jogador.cidadaos:
                if cidadao.profissos[0] == ordem:
                    cidadao.acao_momento[0] = "Socializar"
        self.reino_Jogador.ordens.clear()

    def mostrarOrdens(self):
        Profissoes = self.reino_Jogador.getProfissoes()
        self.tituloDoMenu("➕ Selecionar Ordem")

        for i in range(len(Profissoes)):
            print(f"{Fore.CYAN}{i}{Style.RESET_ALL}. {Profissoes[i].nome}")
        print(f"{Fore.RED}{len(Profissoes)}{Style.RESET_ALL}. Voltar")
        return Profissoes

    # ---> Lista de Serviços especiais

    def menu_servicos_especiais(self):
        opcao = -1
        while opcao != 4:
            self.limpar_tela()

            self.tituloDoMenu("🏰 Serviços especiais do Reino")
            print(f"{Fore.BLUE}1.{Style.RESET_ALL} Militar")
            print(f"{Fore.BLUE}2.{Style.RESET_ALL} Religioso")
            print(f"{Fore.BLUE}3.{Style.RESET_ALL} Explorar")
            print(f"{Fore.RED}4.{Style.RESET_ALL} Sair")

            opcao = int(input("R:"))

            self.limpar_tela()

            match opcao:
                case 1:
                    self.Militar_menu()
                case 2:
                    self.religiao_menu()
                case 3:
                    self.Tela_Expedicao()
                case 4:
                    print("Voltando...")
                case _:
                    print("Comando invalido...")

    def religiao_menu(self):
        opcao = -1
        while opcao != 3:
            self.limpar_tela()
            
            self.tituloDoMenu("Religião")
            print(f"{Fore.CYAN}1{Style.RESET_ALL}. Templos")
            print(f"{Fore.CYAN}2{Style.RESET_ALL}. Fieis")
            print(f"{Fore.RED}3{Style.RESET_ALL}. Voltar")

            opcao = int(input("R:"))

            match opcao:
                case 1:
                    self.Religioso()
                case 2:
                    self.limpar_tela()
                    self.SubMenuTitulo("Seguidores dos deuses")
                    self.control.numerar_numero_seguidores(self.reino_Jogador.cidadaos)
                    print(f"{Fore.GREEN}{'-'*60}{Style.RESET_ALL}")
                case 3:
                    print("Voltando...")
            self.getch()

    def Religioso(self):
        templos = [obj for obj in self.reino_Jogador.construcoes if obj.tipo == "Religioso"]

        if templos == []:
            print("Não há templos erguidos")
        else:
            opcao = -1

            while opcao != len(templos):
                self.limpar_tela()
                self.tituloDoMenu("⛩️  Templos 🏛️")
            
                for i in range(len(templos)):
                    print(f"{Fore.CYAN}{i}{Style.RESET_ALL}. {templos[i].nome_individual} - Divindade da(o) {templos[i].Divindade.dominio}{Style.RESET_ALL}")
                print(f"{Fore.RED}{len(templos)}. Voltar")

                opcao = int(input("R:"))

                self.limpar_tela()
                if opcao != len(templos):
                    self.Bencao_religiao(templos[opcao])

    def Bencao_religiao(self,templo):
        
        self.tituloDoMenu("✨ Bençãos 💀")

        def Bencao(quantidade_sacrificada_total):
            if quantidade_sacrificada_total != 0:
                intensidade = Calcular_intensidade(quantidade_sacrificada_total,templo.Divindade)

                match opcao_bensao:
                    case 1:
                        templo.Divindade.GetBencao(self.reino_Jogador,"Ordem",quantidade_sacrificada_total,intensidade)
                    case 2:
                        templo.Divindade.GetBencao(self.control,"Neutro",quantidade_sacrificada_total,intensidade)
                    case 3:
                        for i in range(len(self.control.getReinos())):
                            print(f"{Fore.CYAN}{i}{Style.RESET_ALL}. {self.control.getReinos()[i].nome}")
                        
                        reino_escolhido = int(input("R: "))
                        templo.Divindade.GetBencao(self.control.getReinos()[reino_escolhido],"Caos",quantidade_sacrificada_total,intensidade)
            else:
                print("Sem sacrificios, não tem como realizar a cerimonia")
        
        def Calcular_intensidade(animais,divindade):
            intensidade = animais // divindade.Quantidade_animais
            return intensidade
        
        def pegar_Construcao():
            for construcao in self.reino_Jogador.construcoes:
                if construcao.nome == "Armazem":
                    return construcao
        
        def quantidadePega(opcao_quantidade_pega,construcao_com_animal):
            quantidade_sacrificada_total = 0

            while opcao_quantidade_pega != len(construcao_com_animal.inventario):
                self.limpar_tela()
                print(f"{Fore.GREEN}{'═'*60}")
                print(f"{Fore.RED}X Sacrificios X{Style.RESET_ALL}")
                print(f"{'═'*60}{Style.RESET_ALL}")

                for i in range(len(construcao_com_animal.inventario)):
                    print(f"{Fore.CYAN}{i}. {construcao_com_animal.inventario[i]['Nome'].nome}")
                print(f'{Fore.RED}{len(construcao_com_animal.inventario)}. Continuar')
                opcao_quantidade_pega = int(input("R: "))

                if opcao_quantidade_pega != len(construcao_com_animal.inventario):
                    print(f"Animais selecionados: {construcao_com_animal.inventario[opcao_quantidade_pega]['Nome'].nome} - {construcao_com_animal.inventario[opcao_quantidade_pega]['Quantidade']}")
                    print(f"0. Voltar")
                    quantidade_sacrificada = int(input("Quantos será pego? "))

                    if quantidade_sacrificada != 0:
                        construcao_com_animal.inventario[opcao_quantidade_pega]['Quantidade'] -= quantidade_sacrificada
                        quantidade_sacrificada_total += quantidade_sacrificada
                self.limpar_tela()
            Bencao(quantidade_sacrificada_total)
        
        
        print(f"{Fore.LIGHTGREEN_EX}1{Style.RESET_ALL}. {templo.Divindade.Bencao_Descricao["Ordem"]}")
        print(f"{Fore.LIGHTBLACK_EX}2{Style.RESET_ALL}. {templo.Divindade.Bencao_Descricao["Neutro"]}")
        print(f"{Fore.LIGHTMAGENTA_EX}3{Style.RESET_ALL}. {templo.Divindade.Bencao_Descricao["Caos"]}")

        opcao_bensao = int(input("R: "))

        
        #print(f"Quantos animais irá sacrificar?")
        #quantidade = int(input("R: "))
        #quantidade_pega = quantidade

        construcao_com_animal = pegar_Construcao()
        quantidade_sacrificada_total = 0

        quantidadePega(quantidade_sacrificada_total,construcao_com_animal)
        self.getch()
    
    def Tela_Expedicao(self):
        self.limpar_tela()
        self.tituloDoMenu(" Exploração ")

        print(f"{Fore.CYAN}1{Style.RESET_ALL}. Realizar expedição")
        print(f"{Fore.CYAN}2{Style.RESET_ALL}. Ver expedições em andamento")
        print(f"{Fore.RED}3{Style.RESET_ALL}. Voltar")

        opcao = int(input("R:"))

        match opcao:
            case 1:
                self.Fazer_Expedicao()
            case 2:
                self.limpar_tela()
                self.tituloDoMenu("Expedições em andamento")
                self.reino_Jogador.mostrarExpedicao()
                self.getch()

    def Fazer_Expedicao(self):
        opcao = -1
        Equipe = Equipe_exploracao(self.reino_Jogador)

        def ver_status(pessoa,Equipe):
            self.limpar_tela()
            print(f"Candidato: {pessoa.nome}")
            pessoa.ShowStatus()
            print("-"*60)
            print(f"{Fore.CYAN}1{Style.RESET_ALL}. Indicar")
            print(f"{Fore.RED}2. Voltar")
            opcao_aceitar = int(input("R: "))

            if opcao_aceitar == 1:
                print("Adicionou")
                if Equipe.membros == []:
                    Equipe.membros.append(Membro_espedicao(pessoa,"Lider"))
                else:
                    Equipe.membros.append(Membro_espedicao(pessoa,"Membro"))
            
            self.getch()
        
        def Pegar_Quem_Explora():
            exploradores_potencial = []

            for pessoa in self.reino_Jogador.cidadaos:
                if pessoa.servico_militar is False and pessoa.explorando is False:
                    exploradores_potencial.append(pessoa)
            return exploradores_potencial
        
        exploradores_potencial = Pegar_Quem_Explora()

        while opcao !=  len(exploradores_potencial):
            self.limpar_tela()
            self.tituloDoMenu(" Exploração ")
            print("Quem será parte dessa espedição?")

            for i,pessoa in enumerate(exploradores_potencial):
                if any(m.pessoa == pessoa for m in Equipe.membros):
                    cor = Fore.LIGHTBLACK_EX
                else:
                    cor = Fore.CYAN
                
                print(f"{cor}{i}. {pessoa.nome}")
            print(f"{Fore.LIGHTRED_EX}{len(exploradores_potencial)} Voltar")
            if Equipe.membros != []:
                print(f"{Fore.LIGHTYELLOW_EX}{len(exploradores_potencial)+1} Continuar")
            
            opcao = int(input("R: "))

            if opcao < len(exploradores_potencial):
                ver_status(exploradores_potencial[opcao],Equipe)
            elif opcao == len(exploradores_potencial)+1 and Equipe.membros != []:
                self.limpar_tela()
                self.tituloDoMenu(" Região ")
                self.control.escolher_regiao(Equipe,self.reino_Jogador,self.relogio)
                exploradores_potencial = Pegar_Quem_Explora()
                Equipe = Equipe_exploracao(self.reino_Jogador)
        
    def Militar_menu(self):
        opcao = -1
        while opcao != 3:
            self.limpar_tela()
            self.tituloDoMenu("🏰 Exercito do Reino")
            print(f"{Fore.CYAN}1{Style.RESET_ALL}. Recrutar")
            print(f"{Fore.CYAN}2{Style.RESET_ALL}. Treinar")
            print(f"{Fore.RED}3{Style.RESET_ALL}. Voltar")

            opcao = int(input("R:"))
            match opcao:
                case 1:
                    self.Militar()
                case 2:
                    tem = any(isinstance(obj, Quartel) for obj in self.reino_Jogador.construcoes)
                    if tem == True:
                        self.control.Treinar(self.reino_Jogador.exercito,self.relogio.dia)
                    else:
                        print("Precisa ter um quartel para treinar os soldados")
                case 3:
                    print("Voltando...")
            
            self.getch()

    def Militar(self):
        opcao = -12

        def pegarCandidados():
                cidadaos = []
                for cidadao in self.reino_Jogador.cidadaos:
                    if cidadao.explorando is False:
                        cidadaos.append(cidadao)
                return cidadaos
        
        cidadaos = pegarCandidados()

        while opcao != len(cidadaos):
            
                
            self.limpar_tela()
            self.tituloDoMenu("🏰 Soldados")
            for i in range(len(cidadaos)):
                txt = f"{Fore.CYAN}{i}{Style.RESET_ALL}. {cidadaos[i].nome} - "

                if cidadaos[i].servico_militar:
                    fore = Fore.GREEN
                    estado = "Recrutado"
                else:
                    fore = Fore.RED
                    estado = "Civil"
                txt += f"{fore}{estado}{Style.RESET_ALL}"
                print(txt)

            print(f"{Fore.RED}{len(cidadaos)}{Style.RESET_ALL}. Voltar")
                
            opcao = int(input('R: '))
            
            if opcao != len(cidadaos):
                if not cidadaos[opcao].servico_militar:
                    if self.reino_Jogador.retornarEspadasN() > len(self.reino_Jogador.exercito.exercito):
                        self.SubMenuTitulo(f"{cidadaos[opcao].nome} foi recrutado")
                        cidadaos[opcao].servico_militar = True
                        self.reino_Jogador.exercito.exercito.append({"Soldado":cidadaos[opcao],"Ativo": False})
                    else:
                        print("> Não tem equipamento o bastante")
            
                elif cidadaos[opcao].servico_militar:
                   cidadaos[opcao].servico_militar = False
                   self.reino_Jogador.exercito.exercito.remove({"Soldado":cidadaos[opcao],"Ativo": False})
            
    # ---> Contruções

    def construcaoMenu(self):
        while True:
            self.limpar_tela()
            self.tituloDoMenu("🏰 Menu de Construções")
            print(f"{Fore.CYAN}1{Style.RESET_ALL}. Ver Construções")
            print(f"{Fore.CYAN}2{Style.RESET_ALL}. Construir")
            print(f"{Fore.RED}3{Style.RESET_ALL}. Voltar")
            try:
                opcao = int(input('R: '))
                match opcao:
                    case 1:
                        self.verConstrucoes()
                    case 2:
                        self.construir()
                    case 3:
                        print("Voltando...")
                        break
                    case _:
                        print("Opção inválida.")
                        self.getch()
            except ValueError:
                print("Entrada inválida. Digite um número.")
                self.getch()

    def verConstrucoes(self):
        reino = self.reino_Jogador

        while True:
            self.limpar_tela()
            self.SubMenuTitulo("🏰 Construções do Reino")
            for i, construcao in enumerate(reino.construcoes):
                print(f"{Fore.CYAN}{i}{Style.RESET_ALL}. {construcao.nome}")
            print(f"{Fore.RED}{len(reino.construcoes)}{Style.RESET_ALL}. Voltar")

            try:
                opcao = int(input('R: '))
                if opcao == len(reino.construcoes):
                    print("Voltando...")
                    self.getch()
                    break
                elif 0 <= opcao < len(reino.construcoes):
                    self.limpar_tela()
                    print(f"{Fore.BLUE}📘 Dados de {reino.construcoes[opcao].nome}:{Style.RESET_ALL}")
                    print("-" * 40)
                    print(reino.construcoes[opcao].Descricao())
                    self.getch()
                else:
                    print("Opção inválida.")
                    self.getch()
            except ValueError:
                print("Entrada inválida. Digite um número.")
                self.getch()

    def construir(self):
        construcoes =[ConstruirCabana,
                    ConstruirCasa,
                    ConstruirTaverna,
                    ConstruirPlantacao,
                    ConstruirMina,
                    ConstruirArmazem,
                    ConstruirArmazem_Comida,
                    ConstruirArmazem_materiais,
                    ConstruirTemplo,
                    ConstruirTorre,
                    ConstruirQuartel]
        self.limpar_tela()
        self.tituloDoMenu("🏰 Construções")
        for i in range(len(construcoes)):
            construcao = construcoes[i]()
            if self.reino_Jogador.tem_Torre_vigilha and construcao.nome == "Torre de vigilha":
                print(f"{Fore.RED}{i}{Style.RESET_ALL}. {construcao.nome}")
            else:
                print(f"{Fore.CYAN}{i}{Style.RESET_ALL}. {construcao.nome}")
        print(f"{Fore.RED}{len(construcoes)}{Style.RESET_ALL}. Voltar")
        opcao = int(input('R: '))
        if opcao != len(construcoes):
            constr = construcoes[opcao]()
            if constr.nome != "Torre de vigilha" or self.reino_Jogador.tem_Torre_vigilha:

                if isinstance(constr,ConstruirPlantacao):
                    self.limpar_tela()
                    cultivo = self.determinarTipo_Cultivo()
                    constr.setConstrucao(cultivo,self.relogio.dia)
                
                elif isinstance(constr,ConstruirTorre):
                    self.reino_Jogador.tem_Torre_vigilha = True
                    self.reino_Jogador.exercito.preparo += 2
                
                if isinstance(constr,ConstruirTemplo):
                    self.limpar_tela()
                    self.tituloDoMenu("Deuses")
                    
                    deuses_panteao = self.control.getReligiao().deuses
                    for i in range(len(deuses_panteao)):
                        print(f"{Fore.CYAN}{i}{Style.RESET_ALL}. {deuses_panteao[i].nome} - {deuses_panteao[i].dominio}")
                    opcao = int(input("R: "))
                    divindade = deuses_panteao[opcao]
                
                self.ColocarMateriais(constr)

                if isinstance(constr,ConstruirTemplo):
                    self.reino_Jogador.construcoes[len(self.reino_Jogador.construcoes)-1].definir_deus(divindade)
                
            else:
                print("Não pode colocar torre mais que uma vez")
            self.limpar_tela()

    def determinarTipo_Cultivo(self):
        cultivos = []

        def Checar_semente(semente):
            for construcao in self.reino_Jogador.construcoes:
                if construcao.nome == "Armazem de comida":
                    for item in construcao.inventario:
                        if isinstance(item.nome, type(semente)):
                            return True
            return False
        
        self.tituloDoMenu("O que deve ser cultivado?")

        for i in range(len(self.array_cultivo)):
            cult = self.array_cultivo[i]()
            if Checar_semente(cult.semente):
                cultivos.append(cult)
        
        for i in range(len(cultivos)):
            print(f"{Fore.BLUE}{i}{Style.RESET_ALL}. "+cultivos[i].nome)
        print(f"{Fore.RED}{len(cultivos)}{Style.RESET_ALL}. Voltar")

        opcao = int(input('R: '))
        if opcao != len(cultivos):
            return cultivos[opcao]


    def PegarMateriais(self):
        materiais_list =[]
        for construcao in self.reino_Jogador.construcoes:
            if isinstance(construcao,Armazem_materiais):
                for i in range(len(construcao.inventario)):
                    if construcao.inventario[i] not in materiais_list:
                        materiais_list.append(construcao.inventario[i])
                    else:
                        for material in materiais_list:
                            if material.nome.nome == construcao.inventario[i].nome.nome:
                                material.quantidade += construcao.inventario[i].quantidade
                
        return materiais_list

    def MostrarMateriais(self,materiais):
        for i in range(len(materiais)):
            print(f"{Fore.CYAN}{i}{Style.RESET_ALL}. {materiais[i].nome.nome} - {materiais[i].quantidade}")

    def selecionarMateriais(self,materiais_list,quantidade):
        
        print("Escolha o material para construir:")
        self.MostrarMateriais(materiais_list)
        print(f"Quantidade de materiais necessários: {quantidade}")
        opcao = int(input('R: '))

        return materiais_list[opcao]

    def ColocarMateriais(self,construcao):
        self.limpar_tela()
        print(f"{Fore.BLUE}📘 Dados de {construcao.nome}:{Style.RESET_ALL}")
        if self.reino_Jogador.ouro >= construcao.preco_ouro:
            
            print(f"Ouro necessária: {Fore.LIGHTYELLOW_EX}{construcao.preco_ouro}")
            print(f"Seu banco: {Fore.LIGHTYELLOW_EX}{self.reino_Jogador.ouro}")
            print(f"{Fore.YELLOW}{'_'*60}")

            print(f"{Fore.CYAN}1{Style.RESET_ALL}. Proseguir")
            print(f"{Fore.RED}2{Style.RESET_ALL}. Voltar")
            opcao = int(input('R: '))
        
            match opcao:
                case 1:
                    print(f"construcao: {construcao}")
                    self.limpar_tela()
                    materiais_list = self.PegarMateriais()
                    if materiais_list != []:
                        material = None
                        
                        if not isinstance(construcao,ConstruirPlantacao):
                            material = self.selecionarMateriais(materiais_list,construcao.quantidade_materiais)
                            self.limpar_tela()
                        
                        self.ColocarConstrucao(construcao,material)
                    else:
                        print("Você não tem materiais suficientes para construir essa construção.")
                    self.getch()
                case 2:
                    print("Voltando...")
        else:
            print("Você não tem ouro suficiente para construir essa construção.")
            print("Voltando...")
            print("-"*60)
            self.getch()

    def exibir_mapa_com_coordenadas(self,matriz):
        Mapa = [linha[:] for linha in matriz]  # Cópia da matriz

        # Cabeçalho com coordenadas X (azul)
        header = "   " + " ".join(f"{Fore.BLUE}{i}{Style.RESET_ALL}" for i in range(len(Mapa[0])))

        # Corpo do mapa com coordenadas Y (verde)
        linhas_numeradas = []
        for i, linha in enumerate(Mapa):
            linha_str = " ".join(linha)
            linhas_numeradas.append(f"{Fore.GREEN}{i}{Style.RESET_ALL}  {linha_str}")

        MapaStr = header + "\n" + "\n".join(linhas_numeradas)
        print(MapaStr)

    def ColocarConstrucao(self,construcao,material):
        print("Digite a posição para ser construida a construção:")
        self.exibir_mapa_com_coordenadas(self.matriz)
        
        x = int(input(f"{Fore.BLUE}x{Style.RESET_ALL}: "))
        y = int(input(f"{Fore.GREEN}y{Style.RESET_ALL}: "))
        
        if self.matriz[y][x] != ".":
            print("Posição já ocupada.")
        else:
            construcao.requisicao(self.reino_Jogador.ouro,self.matriz,self.reino_Jogador,material,y,x)

    # ---> Ver mundo

    def verMundo(self):
        while True:
            self.limpar_tela()
            self.tituloDoMenu("🌍 Ver o Mundo")
            print(f"{Fore.CYAN}1{Style.RESET_ALL}. Regiões")
            print(f"{Fore.CYAN}2{Style.RESET_ALL}. Reinos")
            print(f"{Fore.CYAN}3{Style.RESET_ALL}. Deuses")
            print(f"{Fore.CYAN}4{Style.RESET_ALL}. Raças")
            print(f"{Fore.CYAN}5{Style.RESET_ALL}. Monstros")
            print(f"{Fore.CYAN}6{Style.RESET_ALL}. Culturas")
            print(f"{Fore.CYAN}7{Style.RESET_ALL}. Historia")
            print(f"{Fore.RED}8{Style.RESET_ALL}. Voltar")

            try:
                opcao = int(input("R: "))
                match opcao:
                    case 1:
                        self.listarRegioes(self.control.getRegioes())
                    case 2:
                        self.listarReinos(self.control.getReinos())
                    case 3:
                        self.listarReligiao(self.control.getReligiao())  # Ajuste para getReligioes() se necessário
                    case 4:
                        self.listarRacas(self.control.getRacas())
                    case 5:
                        self.listarMonstros(self.control.getMonstros())
                    case 6:
                        self.listarCultura(self.control.getCultura())
                    case 7:
                        self.limpar_tela()
                        self.SubMenuTitulo("Historia")
                        self.control.getHistoria()
                        print(f"{Fore.YELLOW}---------------------------------------{Style.RESET_ALL}")
                        print(f"{Fore.YELLOW}>>Pressione qualquer tecla para continuar{Style.RESET_ALL}")
                        self.getch()
                    case 8:
                        print("Voltando...")
                        break
                    case _:
                        print("Opção inválida.")
                        self.getch()
            except ValueError:
                print("Entrada inválida. Use apenas números.")
                self.getch()

    # --------- Função Genérica ---------
    def listarEntidades(self,titulo, lista, get_nome, get_desc):
        while True:
            self.limpar_tela()
            self.tituloDoMenu(titulo)
            for i, item in enumerate(lista):
                print(f"{Fore.CYAN}{i}{Style.RESET_ALL}. {get_nome(item)}")
            print(f"{Fore.RED}{len(lista)}{Style.RESET_ALL}. Voltar")

            try:
                opcao = int(input('R: '))
                if opcao == len(lista):
                    print("Voltando...")
                    self.getch()
                    break
                elif 0 <= opcao < len(lista):
                    self.limpar_tela()
                    print(f"{Fore.BLUE}📘 Dados de {get_nome(lista[opcao])}:{Style.RESET_ALL}")
                    print("-" * 40)
                    print(get_desc(lista[opcao]))
                    self.getch()
                else:
                    print("Opção inválida.")
                    self.getch()
            except ValueError:
                print("Entrada inválida. Use apenas números.")
                self.getch()

    # --------- Funções Específicas ---------
    def listarRegioes(self,regios):
        self.listarEntidades("🌄 Regiões do Mundo", regios, lambda x: x.nome, lambda x: x.Descricao())

    def listarReinos(self,reinos):
        self.listarEntidades("🏰 Reinos do Mundo", reinos, lambda x: x.nome, lambda x: x.Descricao())

    def listarReligiao(self,religioes):
        while True:
            self.limpar_tela()
            self.tituloDoMenu("⛪ Religiões do Mundo")
            for i in range(len(religioes.deuses)):
                print(f"{Fore.CYAN}{i}.{Style.RESET_ALL} {religioes.deuses[i].nome}")
            print(f"{Fore.RED}{len(religioes.deuses)}.{Style.RESET_ALL} Voltar")

            try:
                opcao = int(input('R: '))
                if opcao == len(religioes.deuses):
                    print("Voltando...")
                    self.getch()
                    break
                elif 0 <= opcao < len(religioes.deuses):
                    self.limpar_tela()
                    print(f"{Fore.BLUE}📘 Dados de {religioes.deuses[opcao].nome}:{Style.RESET_ALL}")
                    print("-" * 40)
                    print(religioes.deuses[opcao].Descricao())
                    self.getch()
                else:
                    print("Opção inválida.")
                    self.getch()
            except ValueError:
                print("Entrada inválida. Use apenas números.")
                self.getch()

    def listarRacas(self,racas):
        self.listarEntidades("🧬 Raças do Mundo", racas, lambda x: x.nome, lambda x: x.Descricao())

    def listarMonstros(self,monstros):
        self.listarEntidades("👾 Monstros do Mundo", monstros, lambda x: x.nome, lambda x: x.Descricao())

    def listarCultura(self,Cultura):
        self.listarEntidades("♞ Cultura do Mundo", Cultura, lambda x: x.nome, lambda x: x.Descricao())

    # ---> Início do jogo

    def InicioJogador(self):
        
        while True:
            self.limpar_tela()
            print(f"{Fore.MAGENTA}{'═'*50}")
            print(f"{'HUMAN FORTRESS':^50}")
            print(f"{'═'*50}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}1. Jogar")
            print(f"{Fore.CYAN}2. Carregar")
            print(f"{Fore.RED}3. Sair")

            #try:
            opcao = int(input('Escolha uma opção: '))
            match opcao:
                case 1:
                    self.DefinirParametro()
                case 2:
                    print('Carregar ainda não implementado.')
                    time.sleep(2)
                case 3:
                    print('Saindo...')
            #except ValueError:
            print("Entrada inválida. Use números.")
            time.sleep(1)

    def DefinirParametro(self):
        def escolher_opcao(lista_opcoes, titulo):
            print("\n" + Fore.CYAN + "=" * 40)
            print(f"{Fore.YELLOW}{titulo.center(40)}")
            print(Fore.CYAN + "=" * 40)
            
            for i, item in enumerate(lista_opcoes):
                print(f"{Fore.GREEN} {i+1}. {Style.BRIGHT} {item['Descricao']}")

            while True:
                try:
                    escolha = int(input(f"{Fore.BLUE}→ Digite o número da opção desejada: "))-1
                    if 0 <= escolha < len(lista_opcoes):
                        print(f"{Fore.GREEN}✔ Você escolheu: {lista_opcoes[escolha]['Descricao']}\n")
                        return lista_opcoes[escolha]
                    else:
                        print(f"{Fore.RED}✖ Escolha um número entre 0 e {len(lista_opcoes)-1}.")
                except ValueError:
                    print(f"{Fore.RED}✖ Entrada inválida. Digite um número válido.")

        # Listas de parâmetros
        tamanho_mundo = [
            {"Descricao": "Pequeno", "Tamanho": 4},
            {"Descricao": "Médio", "Tamanho": 8},
            {"Descricao": "Grande", "Tamanho": 16}
        ]
        diversidade_racas = [
            {"Descricao": "Modesta", "Quantidade": 4},
            {"Descricao": "Moderada", "Quantidade": 6},
            {"Descricao": "Diversa", "Quantidade": 10}
        ]
        nivel_selvageria = [
            {"Descricao": "Baixa", "Quantidade": 10},
            {"Descricao": "Média", "Quantidade": 15},
            {"Descricao": "Alta", "Quantidade": 20}
        ]

        # Escolhas do jogador
        self.limpar_tela()
        escolha_tamanho = escolher_opcao(tamanho_mundo, "Tamanho do Mundo")
        self.limpar_tela()
        escolha_diversidade = escolher_opcao(diversidade_racas, "Diversidade de Raças")
        self.limpar_tela()
        escolha_selvageria = escolher_opcao(nivel_selvageria, "Nível de Selvageria")

        # Atribuição dos parâmetros
        n_regioes = escolha_tamanho["Tamanho"]
        n_racas = escolha_diversidade["Quantidade"]
        n_monstros = escolha_selvageria["Quantidade"]

        # Exibição final
        print(Fore.MAGENTA + "\n✔ Parâmetros definidos com sucesso:")
        print(Fore.YELLOW + f"  → Regiões: {n_regioes}")
        print(Fore.YELLOW + f"  → Raças: {n_racas}")
        print(Fore.YELLOW + f"  → Monstros: {n_monstros}\n")

        raca_humana = Raca("Humano", f"{Fore.BLUE}H{Style.RESET_ALL}", 0, 10, "Médio", "Esquisitos", 2, 2, 2, 2, 2)

        self.control = Control(raca_humana, n_regioes, n_racas, n_monstros)
        self.Ano = self.control.Ano
        self.relogio.ano = self.Ano

        self.ContinuarJogo()

    def ContinuarJogo(self):
        self.control.GerarMundo()
        self.limpar_tela()
        nome = self.criarRei()
        self.limpar_tela()
        self.criarReino(nome)
        self.control.MapaGerar(self.matriz, self.tamanho)
        self.control.ColocarObjetos(self.matriz, self.tamanho, self.QuantidadeObjetos,self.regiao_jogador, self.reino_Jogador)
        humanos = self.control.criarCidadãos(self.reino_Jogador, self.tamanho)
        self.reino_Jogador.cidadaos = humanos

        self.control.Definir_Soldados(self.reino_Jogador)
        self.control.Definir_Sacerdote(self.reino_Jogador)
        self.control.colocarReligiao(self.reino_Jogador.cidadaos)
        self.RunGame()

    def criarRei(self):
        
        print(f"{Fore.YELLOW}👑 Criação do Rei{Style.RESET_ALL}")
        nome = input('Digite seu nome: ')
        
        return nome

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def criarReino(self,nome):
        
        dados_dificuldade = [
            {"dificuldade": "Fácil", "ouro": 100,"comida": 800, "populacao": 10},
            {"dificuldade": "Normal", "ouro": 50, "comida": 520, "populacao": 7},
            {"dificuldade": "Difícil", "ouro": 25, "comida": 250, "populacao": 5}
        ]
        
        print(f"{Fore.YELLOW}👑 Digite o nome do reino{Style.RESET_ALL}")
        nome_reino = input('R: ')

        persona_reino = [{"Nome":"Beligerante","Descrição": "A moral e o preparo do seu exercito é maior"},
                         {"Nome":"Diplomatico","Descrição": "Te Favorece politicamente com outros reinos"},
                         {"Nome":"Religioso","Descrição": "Sua relação com a magia é maior"},
                         {"Nome":"Comerciante","Descrição": "Seus acordos e trocas comerciais são mais beneficas"},
                         {"Nome":"Escrevista","Descrição": "Leva parte de exercitos derrotados como escravos"}
                         ]

        self.limpar_tela()
        
        print(f"{Fore.YELLOW}👑 Pelo que seu reino é conhecido?{Style.RESET_ALL}")
        for i, item in enumerate(persona_reino):
            print(f"{Fore.CYAN}{i+1}{Style.RESET_ALL}. {item["Nome"]}, {item["Descrição"]}")        
        personalidade_reino = int(input('R: '))

        while True:
            self.limpar_tela()
            print(f"{Fore.GREEN}Escolha a dificuldade:{Style.RESET_ALL}")
            for i, item in enumerate(dados_dificuldade):
                print(f"{i+1}. {item['dificuldade']} (ouro: {item['ouro']}, comida: {item['comida']}, populacao: {item['populacao']})")
            try:
                opcao = int(input('R: '))
                if 1 <= opcao <= len(dados_dificuldade):
                    break
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Digite um número válido.")
        
        reino = self.control.setReinoJogador(
            dados_dificuldade[opcao - 1]["ouro"],
            dados_dificuldade[opcao - 1]["populacao"],
            dados_dificuldade[opcao - 1]["comida"],
            4,
            nome,
            persona_reino[personalidade_reino-1]["Nome"],
            self.humanos,nome_reino
        )
        
        self.reino_Jogador = reino
        self.regiao_jogador = self.control.SelecionarRegiao(self.reino_Jogador)

# Início do jogo
jogo = main()
jogo.InicioJogador()
