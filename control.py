from model.Estoque.estoque import Estoque,Estoque_semente,Dado_espedicao
from model.Meteriais.planta import Arvore, Macieira, Arbusto
from model.Meteriais.Cenario import Pedregulho
from model.Meteriais.construcao import Posto_Comercio, Armazem,Armazem_Comida,Armazem_materiais,Demanda_tempo,Templo
from model.Meteriais.material import Pedra,Madeira
from model.Meteriais.Itens import (espada)
from model.Meteriais.comida import (
    Maca, Banana, Frutinha, Cogumelo, Queijo, Pao, Carne, Pescado,
    Trigo, Laranja, Uva, Morango, Tomate, Cenoura, Alface,
    Batata, Abobora, Pepino,
    Beterraba, Rabanete, Mandioca, Inhame, Cebola,
    Abacaxi, Melancia, Manga, Pimentao, Espinafre, Coco, Azeitona
)
from model.Meteriais.comida import (
    cultivo_maca, cultivo_trigo, cultivo_laranja, cultivo_uva,
    cultivo_morango, cultivo_tomate, cultivo_cenoura, cultivo_alface,
    cultivo_batata, cultivo_abobora, cultivo_pepino,
    cultivo_beterraba, cultivo_rabanete, cultivo_mandioca, cultivo_inhame,
    cultivo_cebola, cultivo_abacaxi, cultivo_melancia, cultivo_manga,
    cultivo_pimentao, cultivo_espinafre, cultivo_coco, cultivo_azeitona
)

from model.SobreMundo.Eventos import Evento
from model.SobreMundo.Reinos import Reino,Cultura,Ruinas_antigas,Reino_perdido,Exploracao,Tribo_Encontro,Roubo_item,localizacao_Especial
from model.SobreMundo.Racas import Raca, Criatura
from model.SobreMundo.Religiao import Religiao
from model.SobreMundo.mundo import Mundo, Regioes,Historia

from model.Animais.animal_sapiente import Animal_Sapien
from model.Animais.monstro import Monstros
from model.Animais.animal import (
    Porco, Galinha, Cavalo,Gado, Gato, 
    Cachorro, Coelho, Veado, Raposa, 
    Urso, Coruja, Cobra, Camelo, 
    Jacare, Sapo, Tartaruga, Lobo, 
    Cabra, Tigre, Leao, Elefante, 
    Anta, Ganso, Pato, Rato, 
    Morcego, Ovelha, Pavao, GansoDomestico,
    Lhama, Peru, Burro, Javali, Onca, 
    Tamandua, BichoPreguica, Cervo, Falcao
)


import random
import string
import os
import msvcrt
from colorama import Fore, Style, init

class Control:
    def __init__(self, raca_humana, n_regioes, 
                 n_racas, n_monstros):
        
        self.raca_humana = raca_humana
        self.Mundo_criado = None
        self.evento = Evento()

        self.Ano = random.randint(100,250)

        self.n_regioes = n_regioes
        self.RegioesList = []

        self.Cultura_Lista = []

        self.n_vegetacao = 0
        self.n_pedras = 0
        self.chance_minerio = 0.05

        self.chance_reproducao = 0.1
        self.chance_reproducao_original = 0.1
        self.Turnos_reproducao = 0

        self.chance_melhora_soldado_treino = 0.2
        self.chance_melhora_soldado_treino_original = 0.2
        self.Turnos_chance_melhora_soldado_treino = 0
        self.chance_encontrar_estrutura = 0.35

        self.dia_treino = 0

        self.n_racas = n_racas
        orc = Raca(
            nome="Orc",
            simbolo=f"{Fore.GREEN}O{Style.RESET_ALL}",
            vida=random.randint(120,135),
            dano=random.randint(12,20),
            altura="Robusto",
            aparencia="Brutal",
            forca=3, destreza=2, inteligencia=1, carisma=1, constituicao=2
        )

        anao = Raca(
            nome="Anão",
            simbolo=f"{Fore.YELLOW}â{Style.RESET_ALL}",
            vida=random.randint(100,110),
            dano=random.randint(10,15),
            altura="Baixo",
            aparencia="Barbudo",
            forca=2, destreza=1, inteligencia=2, carisma=1, constituicao=3
        )

        elfo = Raca(
            nome="Elfo",
            simbolo=f"{Fore.LIGHTYELLOW_EX}ê{Style.RESET_ALL}",
            vida=random.randint(100,120),
            dano=random.randint(10,14),
            altura="Esbelto",
            aparencia="Elegante",
            forca=1, destreza=3, inteligencia=2, carisma=2, constituicao=1
        )

        goblin = Raca(
            nome="Goblin",
            simbolo=f"{Fore.LIGHTGREEN_EX}g{Style.RESET_ALL}",
            vida=random.randint(70, 90),
            dano=random.randint(5, 12),
            altura="Pequeno",
            aparencia="Esquisito",
            forca=1, destreza=3, inteligencia=2, carisma=1, constituicao=1
        )
        self.Racas = [raca_humana,orc,anao,elfo,goblin]

        self.n_monstros = n_monstros
        self.MonstrosList = []

        self.n_reinos = self.n_regioes * 4
        self.Reinos = []

        self.Religiao_mundo = None
        self.Objetos = []

    # Métodos Get
    def getRacas(self):
        return self.Mundo_criado.racas

    def getReligiao(self):
        return self.Mundo_criado.religiao

    def getRegioes(self):
        return self.Mundo_criado.regioes

    def getReinos(self):
        return self.Mundo_criado.reinos

    def getMonstros(self):
        return self.Mundo_criado.monstros

    def getCultura(self):
        return self.Mundo_criado.culturas
    
    def getHistoria(self):
        print(f"{self.historia.historia_completo}")

    # Limpar tela
    @staticmethod
    def limpar_tela():
        os.system('cls' if os.name == 'nt' else 'clear')

    def getch(self):
        return msvcrt.getch().decode('utf-8')
    
#---> Funções de preencher o mapa
    def ColocarObjetos(self,matriz, tamanho,QuantidadeObjetos,regiao_jogador, reino_Jogador):

        self.colocarPedra(matriz, tamanho,regiao_jogador)
        self.colocarVegetacao(matriz, tamanho,regiao_jogador)
        self.colocarConstrucoes(matriz, tamanho,reino_Jogador)
        self.colocarItens(regiao_jogador, reino_Jogador)
        self.colocarAgua(matriz, tipo="lago", quantidade=3, tamanho_max=15)

    def colocarPedra(self,matriz, tamanho,regiao_jogador):
        
        QuantidadePedras = random.randint(regiao_jogador.tipo["pedrasMin"], regiao_jogador.tipo["pedrasMax"])
        for _ in range(QuantidadePedras):
            x = random.randint(0, tamanho - 1)
            y = random.randint(0, tamanho - 1)

            while matriz[x][y] != ".":
                x = random.randint(0, tamanho - 1)
                y = random.randint(0, tamanho - 1)

            pedregulho = Pedregulho(x,y)
            matriz[x][y] = pedregulho.simbolo
            self.Objetos.append(pedregulho)

    def colocarVegetacao(self,matriz, tamanho,regiao_jogador):
        
        QuantidadeVegetacao = random.randint(regiao_jogador.tipo["vegetacaoMin"], regiao_jogador.tipo["vegetacaoMax"])

        for _ in range(QuantidadeVegetacao):

            # Escolhe uma posição aleatória na matriz
            x = random.randint(0, tamanho - 1)
            y = random.randint(0, tamanho - 1)

            while matriz[x][y] != ".":
                x = random.randint(0, tamanho - 1)
                y = random.randint(0, tamanho - 1)

            arvore = random.choice([Arvore(x, y),Macieira(x,y),Arbusto(x,y)])
            matriz[x][y] = arvore.simbolo
            self.Objetos.append(arvore)

    def colocarConstrucoes(self,matriz, tamanho,reino_Jogador):

        margem = int(tamanho * 0.35)  # 35% de margem nas bordas
        tamanho_reduzido = int(tamanho * 0.3) 
        
        for construcao in reino_Jogador.construcoes:
            construcao.x = random.randint(margem,margem + tamanho_reduzido - 1)
            construcao.y = random.randint(margem,margem + tamanho_reduzido - 1)
            matriz[construcao.x][construcao.y] = construcao.simbolo

    def colocarItens(self,regiao_jogador, reino_Jogador):
        
        for animal in regiao_jogador.animais:
            animal_escolhido = animal()
            if animal_escolhido.tipo == "Domestico":
                quantidade = random.randint(80,880)
                reino_Jogador.construcoes[1].inventario.append(Estoque(animal_escolhido,quantidade))
        self.Colocar_Vegetal(regiao_jogador, reino_Jogador)
        self.Colocar_Material(regiao_jogador, reino_Jogador)
        self.colocarSemente(reino_Jogador,regiao_jogador)
        self.Colocar_animal(reino_Jogador)

    def Colocar_animal(self, reino_Jogador):
        animais_base = [Porco, Galinha, Ovelha, Gado]  # Gado precisa existir como classe
        armazem = reino_Jogador.construcoes[1].inventario

        for AnimalClasse in animais_base:
            quantidade = random.randint(10, 25)
            encontrado = False

            for entrada in armazem:
                print(entrada)
                if isinstance(entrada.nome, AnimalClasse):
                    entrada.quantidade += quantidade
                    encontrado = True
                    break

            # Se não encontrou, adiciona novo item ao inventário
            if not encontrado:
                estoque = Estoque(AnimalClasse(),quantidade)
                armazem.append(estoque)


    def colocarAgua(self,matriz, tipo="lago", quantidade=1, tamanho_max=20):
        altura = len(matriz)
        largura = len(matriz[0])

        for _ in range(quantidade):
            # Ponto inicial aleatório
            x = random.randint(0, altura - 1)
            y = random.randint(0, largura - 1)

            agua_restante = random.randint(5, tamanho_max)
            visitados = set()
            fronteira = [(x, y)]

            while agua_restante > 0 and fronteira:
                atual = fronteira.pop(0)
                if atual in visitados:
                    continue
                visitados.add(atual)
                i, j = atual

                if 0 <= i < altura and 0 <= j < largura and matriz[i][j] == '.':
                    matriz[i][j] = f"{Fore.CYAN}={Style.RESET_ALL}"
                    agua_restante -= 1

                    # Sorteia os próximos blocos
                    vizinhos = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
                    random.shuffle(vizinhos)

                    # Chance de expandir em cada direção
                    for viz in vizinhos:
                        if random.random() < 0.8:  # 80% de chance de crescer
                            fronteira.append(viz) 
    def Colocar_Material(self,regiao_jogador, reino_Jogador):
        
        item_material = [Pedra,Madeira]
        
        for item in item_material:
            item = item()
            quantidade = random.randint(1,20)

            reino_Jogador.construcoes[3].inventario.append(Estoque(item,quantidade))
    
    def Definir_Soldados(self,reino_Jogador):
        Exercito = []
        total_cidadaos = len(reino_Jogador.cidadaos)
        quantidade_minima = int(len(reino_Jogador.cidadaos)*0.6)
        quantidade_soldados = random.randint(quantidade_minima,(len(reino_Jogador.cidadaos)//2)+2)#int(total_cidadaos * 0.6)

        for i in range(quantidade_soldados):
            cidadao = reino_Jogador.cidadaos[i]
            cidadao.servico_militar = True
            Exercito.append({"Soldado":cidadao,"Ativo": False})

        reino_Jogador.exercito.exercito = Exercito

        for construcao in reino_Jogador.construcoes:
            if isinstance(construcao,Armazem_materiais):
                construcao.inventario.append(Estoque(espada(Pedra()),len(Exercito)))
    
    def Definir_Sacerdote(self,reino_Jogador):
        n_sacerdotes = 2
        filtrados = [obj for obj in reino_Jogador.cidadaos if not obj.servico_militar]
        sacerdote = random.sample(filtrados,n_sacerdotes)

        sacerdote[0].servico_religioso = True
        sacerdote[1].servico_religioso = True

        reino_Jogador.sacerdotes = sacerdote

    def colocarSemente(self,reino_Jogador,regiao_jogador):
        semente = [
        cultivo_maca, cultivo_trigo, cultivo_laranja, cultivo_uva,
        cultivo_morango, cultivo_tomate, cultivo_cenoura, cultivo_alface,
        cultivo_batata, cultivo_abobora, cultivo_pepino,
        cultivo_beterraba, cultivo_rabanete, cultivo_mandioca, cultivo_inhame,
        cultivo_cebola, cultivo_abacaxi, cultivo_melancia, cultivo_manga,
        cultivo_pimentao, cultivo_espinafre, cultivo_coco, cultivo_azeitona
        ]


        for seed in semente:
            seed = seed()
            for vegetacao in regiao_jogador.vegetacao:
                vegetacao = vegetacao()
                if isinstance(seed.resultado,type(vegetacao)):
                    reino_Jogador.construcoes[2].inventario.append(Estoque_semente(seed.semente,random.randint(1,10),seed))

    def Colocar_Vegetal(self, regiao_jogador, reino_Jogador):
        n_comida = reino_Jogador.Comida
        total_itens = len(regiao_jogador.vegetacao) + 4  # 4 itens na lista Comida
        comida_por_item = max(n_comida // total_itens, 1)  # garantir pelo menos 1

        # Adiciona vegetais
        for vegetal_class in regiao_jogador.vegetacao:
            vegetal = vegetal_class()
            quantidade = min(comida_por_item, n_comida)
            n_comida -= quantidade
            reino_Jogador.construcoes[2].inventario.append(Estoque(vegetal,quantidade))

        # Adiciona outras comidas
        self.Colocar_comida(reino_Jogador, n_comida, comida_por_item)

    def Colocar_comida(self, reino_Jogador, n_comida_restante, comida_por_item):
        Comida = [Queijo, Pao, Carne, Pescado]

        for comida_class in Comida:
            quantidade = min(comida_por_item, n_comida_restante)
            n_comida_restante -= quantidade
            reino_Jogador.construcoes[2].inventario.append(Estoque(comida_class(),quantidade))
    
    def MapaGerar(self,matriz, tamanho):  
        matriz.clear()  # Limpa a matriz antes de criar uma nova
        for _ in range(tamanho):
            Linha = []
            for _ in range(tamanho):
                Linha.append(".")
            matriz.append(Linha)
    
    def tela(self,texto):
        self.limpar_tela()
        print(f"\033[33m=\033[0m"*60)
        print(f"{f'{Fore.YELLOW}{texto}':^50}")
        print(f"\033[33m=\033[0m"*60)

    def AcoesMapa(self,reino,Mapa,matriz, tamanho, relogio,pausado,regiao):
        self.Evento_Definir(reino,relogio,pausado,matriz)
        
        for expedicao in reino.expedicoes:
            if relogio.dia - expedicao.Dia_inicio == expedicao.tempo and expedicao.grupo.Explorando:
                
                if isinstance(expedicao.local,localizacao_Especial):
                    self.tela("Exploração")
                expedicao.local.Aventura(expedicao.grupo)

                expedicao.grupo.Explorando = False
                expedicao.grupo.Voltando = True

                if isinstance(expedicao.local,localizacao_Especial):
                    print(f"{Fore.LIGHTYELLOW_EX}> Pressione qualquer tecla para continuar")
                    self.getch()

            elif relogio.dia - expedicao.Dia_inicio == expedicao.tempo*2 and expedicao.grupo.Voltando:
                self.tela("O Bom filho volta a casa!")

                print(f"> A equipe voltou ao reino")
                
                if not isinstance(expedicao.local, localizacao_Especial):
                    expedicao.local.Aventura(expedicao.grupo)
                if expedicao.grupo.loot != None:
                    expedicao.grupo.loot()
                else:
                    for integrante in expedicao.grupo.membros:
                        if integrante.posicao == "Lider":
                            lider = integrante.pessoa.nome
                    print(f"> O grupo liderado pelo(a) {Fore.LIGHTYELLOW_EX}{lider}{Style.RESET_ALL} não teve muita sorte na expedição")

                for integrante in expedicao.grupo.membros:
                    integrante.pessoa.Dentro_estrutura = False
                    integrante.pessoa.explorando = False
                
                reino.expedicoes.remove(expedicao)
                print(f"{Fore.LIGHTYELLOW_EX}> Pressione qualquer tecla para continuar")
                self.getch()
        
        for humano in reino.cidadaos:
            if humano.explorando is False:
                self.Diminuir_Fome(humano,reino)
                self.Definir_sono(humano,relogio,reino)
                self.Acao_conforme_necessidade(reino,humano)
                if not humano.Dentro_estrutura:
                    humano.movimentar(tamanho,relogio, matriz,reino,self.Objetos)
                    Mapa[humano.x][humano.y] = humano.simbolo

        for construcao in reino.construcoes:
            if isinstance(construcao,Demanda_tempo):
                construcao.acao_tempo(reino,matriz,relogio,regiao)
        
        self.Reproduzir_animais(reino,relogio)

    def Evento_Definir(self,reino, relogio, pausado,Mapa):
        if relogio.dia % 1 == 0 and self.evento.ultimo_evento_dia != relogio.dia:
            self.evento.ultimo_evento_dia = relogio.dia
            self.tela("Evento")
            self.evento.evento_estacional(self.Mundo_criado, reino,Mapa)
            self.limpar_tela()
        else:
            self.evento.ativo = True

    def necessidades_Pessoas(self,humano):
        chance_religiao = random.random()
        chance_diversao = random.random()
        chance_socializar = random.random()

        if humano.emTemplo == False and chance_religiao > 0.7:
            humano.necessidades["Fé"] += 1
        if humano.seDivertindo == False and chance_diversao > 0.7:
            humano.necessidades["Diversão"] += 1
        if humano.acao_momento[0] != "Socializar" and chance_socializar > 0.7:
            humano.necessidades["Socializar"] += 1
    
    def Acao_conforme_necessidade(self,reino,humano):

        self.necessidades_Pessoas(humano)

        if humano.necessidades["Fé"] >= 50 and humano.acao_momento[0] == "Socializar":
            templo = self.Saber_Templo_Deus(reino,humano)
            if templo != None:
                humano.acao_momento[0] = "Rezar"
                if humano.felicidade < 100:
                    humano.felicidade += 35
            elif humano.felicidade >0:
                humano.felicidade -=1
        
        if humano.necessidades["Diversão"] >= 50 and humano.acao_momento[0] == "Socializar":
            local = self.saber_diversao(reino)
            if local != None:
                humano.acao_momento[0] = "Se Divertir"
                if humano.felicidade < 100:
                    humano.felicidade += 35
            elif humano.felicidade >0:
                humano.felicidade -=1
        if humano.necessidades["Socializar"] >=50 and humano.felicidade >0:
            humano.felicidade -= 1

    def Saber_Templo_Deus(self,reino,humano):
        for construcao in reino.construcoes:
            if isinstance(construcao,Templo):
                if construcao.Divindade == humano.deus_adorado and construcao.quantidadeP< construcao.quantidadePMax:
                    return construcao
        return None

    def saber_diversao(self,reino):
        for construcao in reino.construcoes:
            if construcao.tipo == "Socializar":
                if construcao.quantidadeP > 0:
                    return construcao
        return None

    def Diminuir_Fome(self,humano,reino):
        if humano.fome > 0 and random.random() < 0.4 and humano.acao_momento[0] == "Socializar":
            humano.fome -= random.randint(1, 2)
            if reino.calcular_total_comida()>0 :
                if humano.fome < (humano.fomeMax * 0.3) and humano.acao_momento[0] == "Socializar":
                    humano.acao_momento[0] = "Comer"
                    if humano.felicidade < 100:
                        humano.felicidade += 35
            else:
                if humano.felicidade >0:
                    humano.felicidade -= 1
    
    def Definir_sono(self,humano,relogio,reino):

        tem_diponivel = self.construcao_disponivel(reino)
        
        if humano.acao_momento[0] == "Socializar" and relogio.hora <= 21 and relogio.hora >= 20 and tem_diponivel:
            humano.acao_momento[0] = "Descançar"
            if humano.felicidade < 100:
                humano.felicidade += 35

        
        elif not humano.Dentro_estrutura and relogio.hora > 21 and humano.acao_momento[0] != "Trabalhar":
        
            humano.acao_momento[0] = "Socializar"
            if humano.felicidade >0:
                humano.felicidade -= 2
        
        elif relogio.hora == 5 and humano.acao_momento[0] != "Trabalhar":
            for construcao in reino.construcoes:
                if humano in construcao.inventario:
                    construcao.inventario.remove(humano)
                    construcao.quantidadeP += 1
            
            humano.Dentro_estrutura = False
            humano.acao_momento[0] = "Socializar"
    
    def Reproduzir_animais(self,reino,relogio):
        for construcao in reino.construcoes :
            if construcao.nome == "Armazem":
                for animal in construcao.inventario:
                    if animal.quantidade >1 and relogio.dia % animal.nome.Tempo_reproducao == 0:
                        chance = random.random()
                        if chance <= self.chance_reproducao:
                            animal.quantidade += animal.quantidade // 2
        
                            if self.chance_reproducao != self.chance_reproducao_original and self.Turnos_reproducao != 0:
                                self.Turnos_reproducao -= 1
        
        if self.Turnos_reproducao == 0:
            self.chance_reproducao = self.chance_reproducao_original

    def construcao_disponivel(self,reino):
        
        for construcao in reino.construcoes:
            if construcao.tipo == "Habitacional" and construcao.quantidadeP > 0:
                return True
        return False
    
    def gerarMonstrons(self):
        for i in range(self.n_monstros):
            monstro = Monstros(0,0)
            self.MonstrosList.append(monstro)
    
    def SelecionarRegiao(self,reino):
        regiao = -1  # inicializa com valor inválido para entrar no loop

        while regiao < 0 or regiao >= len(self.RegioesList):
            self.limpar_tela()
            print("Selecione a região que deseja explorar:")
            for i in range(len(self.RegioesList)):
                estado = f"  • {Fore.LIGHTBLACK_EX}Pedras: {(self.RegioesList[i].tipo["pedrasMin"]+self.RegioesList[i].tipo["pedrasMax"])/2}{Style.RESET_ALL} \n  • {Fore.LIGHTGREEN_EX}Vegetação: {(self.RegioesList[i].tipo["vegetacaoMin"]+self.RegioesList[i].tipo["vegetacaoMax"])/2}{Style.RESET_ALL}"
                
                print(f"{Fore.LIGHTCYAN_EX}{i+1}{Style.RESET_ALL}. {self.RegioesList[i].nome} \n{estado}\n  • {Fore.LIGHTWHITE_EX}Riqueza mineral: {self.RegioesList[i].riqueza_mineral}\n")
            #try:
            regiao = int(input('R: ')) - 1
            if regiao < 0 or regiao >= len(self.RegioesList):
                print("Opção inválida, escolha um número da lista.")
            #except ValueError:
                #print("Por favor, digite um número válido.")
        
        regiao_jogador = self.RegioesList[regiao]
        self.limpar_tela()
        print(regiao_jogador.Descricao())
        self.RegioesList[regiao].reinos.append(reino)

        return regiao_jogador
    
    def VerificarProximidade(self,h1, h2):
        return abs(h1.x - h2.x) <= 1 and abs(h1.y - h2.y) <= 1

    def DesginarCidadaoAProfissao(self,opcao, cidadao_id, Profissoes, cidadaos):
        # Acessando o cidadão pelo índice (cidadao_id)
        cidadao = cidadaos[cidadao_id]

        # Mostrando a profissão atual (caso já tenha uma profissão)
        if hasattr(cidadao, 'profissao'):
            print(f"Profissão atual: {cidadao.profissao.nome if cidadao.profissao else 'Nenhuma'}")
        else:
            print("O cidadão ainda não tem profissão.")

        # Designando a nova profissão
        cidadao.profissao = Profissoes[opcao] # Atribuindo a profissão ao cidadão

        print(f"{cidadao.nome} agora é um(a) {cidadao.profissao.nome}")  # Exibindo a nova profissão

    def numerar_numero_seguidores(self,cidadaos):
        def contagem():
            dicionario_deuses = []

            for divindade in self.Religiao_mundo.deuses:
                dicionario_deuses.append({"Nome":divindade.nome,"Quantidade": 0})
            
            for cidadao in cidadaos:
                for divindade_quant in dicionario_deuses:
                    if divindade_quant["Nome"] == cidadao.deus_adorado.nome:
                        divindade_quant["Quantidade"] += 1
            return dicionario_deuses

        array = contagem()

        for entrada in array:
            print(f"• {entrada["Nome"]}: {entrada["Quantidade"]} ")

    def Treinar(self,exercito,dia):

        if dia != self.dia_treino:
            self.dia_treino = dia
            sucesso = random.random()
            if sucesso < self.chance_melhora_soldado_treino:
                exercito.preparo += 1
                print("O exercito ficou mais preparado para o combate")
            else:
                print("O exercito está treinando...")
        else:
            print("Os soldados estão cansados demais para treinar por hoje....")
    
    def escolher_regiao(self,grupo,reino,relogio):

        for i, item in enumerate(self.RegioesList):
            print(f"{Fore.CYAN}{i}. {item.nome}")
        print(f"{Fore.RED}{len(self.RegioesList)}.voltar")
        opcao = int(input("R:"))

        tempo = 1#random.randint(5,20)

        chance_encontro = random.random()

        grupo.regiao = self.RegioesList[opcao]

        for pessoa in grupo.membros:
            pessoa.pessoa.Dentro_estrutura = True
            pessoa.pessoa.explorando = True

        if chance_encontro <= self.chance_encontrar_estrutura:
            local = random.choice(self.RegioesList[opcao].Estruturas)           
        else:
            local = Exploracao(self.Mundo_criado)
        
        reino.expedicoes.append(Dado_espedicao(grupo,local,tempo,relogio.dia,relogio.ano,relogio.mostrar_data()))

        print("> O grupo saiu em viagem...")

    def gerarCriatura(self):
        nomes = [
            {"vida": random.randint(100,150), "dano": random.randint(40,45), "altura": "Alto", "aparencia": "Rude", "forca":3, "destreza":1, "inteligencia":1, "carisma":1, "constituicao":2},
            {"vida": random.randint(150,175), "dano": random.randint(40,50), "altura": "Enorme", "aparencia": "Amedrontador", "forca":4, "destreza":1, "inteligencia":1, "carisma":1, "constituicao":3},
            {"vida": random.randint(100,120), "dano": random.randint(10,20), "altura": "Médio", "aparencia": "Escamoso", "forca":2, "destreza":2, "inteligencia":1, "carisma":1, "constituicao":2},
            {"vida": random.randint(50,100), "dano": random.randint(10,30), "altura": "Médio", "aparencia": "Pálido", "forca":2, "destreza":3, "inteligencia":2, "carisma":3, "constituicao":1},
            {"vida": random.randint(60, 90), "dano": random.randint(20, 35), "altura": "Etéreo", "aparencia": "Sombrio", "forca":1, "destreza":3, "inteligencia":3, "carisma":2, "constituicao":1},
            {"vida": random.randint(140, 160), "dano": random.randint(30, 40), "altura": "Muito alto", "aparencia": "Feio", "forca":4, "destreza":1, "inteligencia":1, "carisma":1, "constituicao":4},
            {"vida": random.randint(110, 140), "dano": random.randint(30, 45), "altura": "Alto", "aparencia": "Bestial", "forca":3, "destreza":3, "inteligencia":1, "carisma":1, "constituicao":3},
            {"vida": random.randint(110, 140), "dano": random.randint(20, 35), "altura": "Alto", "aparencia": "Mitológico", "forca":3, "destreza":3, "inteligencia":2, "carisma":2, "constituicao":2},
            {"vida": random.randint(120, 150), "dano": random.randint(30, 40), "altura": "Grande", "aparencia": "Intimidante", "forca":4, "destreza":2, "inteligencia":1, "carisma":1, "constituicao":3},
            {"vida": random.randint(50, 80), "dano": random.randint(10, 20), "altura": "Médio", "aparencia": "Descarnado", "forca":1, "destreza":2, "inteligencia":1, "carisma":1, "constituicao":1},
            {"vida": random.randint(60, 90), "dano": random.randint(15, 25), "altura": "Desajeitado", "aparencia": "Apodrecido", "forca":2, "destreza":1, "inteligencia":1, "carisma":1, "constituicao":2},
            {"vida": random.randint(90, 120), "dano": random.randint(20, 30), "altura": "Ágil", "aparencia": "Aracnídeo", "forca":2, "destreza":4, "inteligencia":2, "carisma":1, "constituicao":2},
            {"vida": random.randint(100, 130), "dano": random.randint(40, 55), "altura": "Vibrante", "aparencia": "Incandescente", "forca":3, "destreza":3, "inteligencia":3, "carisma":2, "constituicao":3},
            {"vida": random.randint(100, 130), "dano": random.randint(35, 50), "altura": "Frio", "aparencia": "Cristalino", "forca":3, "destreza":2, "inteligencia":3, "carisma":2, "constituicao":3},
            {"vida": random.randint(120, 160), "dano": random.randint(30, 45), "altura": "Alto", "aparencia": "Dracônico", "forca":4, "destreza":2, "inteligencia":2, "carisma":2, "constituicao":3},
            {"vida": random.randint(70, 100), "dano": random.randint(25, 35), "altura": "Sombrio", "aparencia": "Eterizado", "forca":1, "destreza":4, "inteligencia":3, "carisma":1, "constituicao":2},
            {"vida": random.randint(80, 110), "dano": random.randint(15, 25), "altura": "Leve", "aparencia": "Plumado", "forca":1, "destreza":4, "inteligencia":2, "carisma":2, "constituicao":2},
            {"vida": random.randint(130, 160), "dano": random.randint(25, 40), "altura": "Massivo", "aparencia": "Terroso", "forca":3, "destreza":1, "inteligencia":2, "carisma":1, "constituicao":4},
            {"vida": random.randint(90, 120), "dano": random.randint(20, 35), "altura": "Sinistro", "aparencia": "Macabro", "forca":2, "destreza":2, "inteligencia":4, "carisma":1, "constituicao":2}
        ]

        racas_fantasia = [
            # Tradicionais
            "Elfo", "Anão", "Orc", "Goblin", "Troll", "Humano", "Draconiano", "Meio-Elfo",
            "Halfling", "Tiefling", "Gnomo", "Centauro", "Minotauro", "Fada", "Sátiro",

            # Mitologias do mundo real
            "Jotunn",         # Gigantes da mitologia nórdica
            "Nephilim",       # Híbridos da Bíblia
            "Rakshasa",       # Demônios ilusórios do hinduísmo
            "Kami",           # Espíritos divinos do xintoísmo
            "Naga",           # Serpentes mitológicas do sul da Ásia
            "Bastetinos",     # Homenagem à deusa-gato egípcia Bastet
            "Garuda",         # Pássaro divino hindu
            "Valquírias",     # Guerreiras nórdicas
            "Djinnari",       # Derivado de "Djinn", do folclore árabe
            "Lamiae",         # Monstros femininos da mitologia greco-romana

            # Lovecraftianas / Originais
            "Yithiano",       # Inspirado nos "Grandes da Raça de Yith"
            "Tcho-Tcho",      # Tribo canibal do universo Lovecraft
            "Xha’thari",      # Nome original inspirado no idioma de Lovecraft
            "Umbralith",      # Raça do Vazio Sombrio
            "Nyog’Serathi",   # Nome inventado no estilo dos deuses exteriores
            "Abissal",        # Genérico para seres do mar profundo/loucos
            "Nihilith",       # Entidades da entropia total
            "Ek’Zhuril",      # Criação original, soa alienígena
            "Sussurrantes",   # Raça que se comunica por sussurros da loucura
            "Thren-Kai",      # Inventada, lembra o som de uma civilização antiga

            # Extras mistos
            "Cinzar",         # Raça feita de névoa ou cinzas
            "Pyraxi",         # Seres de fogo inteligente
            "Velkar",         # Nomádicos do éter
            "Nocturnos",      # Seres noturnos, etéreos
        ]

        sobrenomes_raciais = [
            "da Névoa", "do Abismo", "dos Antigos", "da Luz Eterna", "Sussurro-Velho",
            "Quebrador de Correntes", "do Olho Infinito", "Guardião do Limiar", "Andarilho Sombrio",
            "Vento Negro", "Toca-Rocha", "Raiz-Partida", "Sangue-Dourado", "Dente de Prata",
            "Sombra-Sussurrante", "Chamado do Mar", "Voz do Vácuo", "Fragmento do Tempo",
            "Chama-Eterna", "do Templo Velado", "Coração-de-Pedra", "Olhar da Lua",
            "Círculo das Marés", "Sombras de Nyarl", "Dançarino de Ossos", "Eco do Caos",
            "Filho de Ymir", "da Linhagem de Bastet", "da Tempestade Solar", "da Névoa Ancestral"
        ]

        criaturas = []
        for dados in nomes:
            criatura = Criatura(**dados)
            criatura.nome = random.choice(racas_fantasia) + " "+ random.choice(sobrenomes_raciais)
            criaturas.append(criatura)
        return criaturas
    
    def gerarRaca(self):
        nomes = self.gerarCriatura()
        cores = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
        cor = random.choice(cores)
        simbolo = cor + random.choice(string.ascii_lowercase) + f"{Style.RESET_ALL}"
        primeiro = random.choice(nomes)
        segundo = random.choice(nomes)
        
        nome = primeiro.nome

        vida = primeiro.vida
        dano = segundo.dano
        altura = primeiro.altura
        aparencia = segundo.aparencia

        atributos = random.choice([primeiro, segundo])
        forca = atributos.forca
        atributos = random.choice([primeiro, segundo])
        destreza = atributos.destreza
        atributos = random.choice([primeiro, segundo])
        inteligencia = atributos.inteligencia
        atributos = random.choice([primeiro, segundo])
        carisma = atributos.carisma
        atributos = random.choice([primeiro, segundo])
        constituicao = atributos.constituicao

        return nome, simbolo, vida, dano, altura, aparencia, forca, destreza, inteligencia, carisma, constituicao

    def CriarRacas(self):
        for _ in range(self.n_racas):
            nome, simbolo, vida, dano, altura, aparencia, forca, destreza, inteligencia, carisma, constituicao = self.gerarRaca()
            raca = Raca(nome, simbolo, vida, dano, altura, aparencia, forca, destreza, inteligencia, carisma, constituicao)
            self.Racas.append(raca)

    def criarCidadãos(self,reino_jogador, tamanho):
        humanos = []

        # Definindo a faixa para a geração de x e y (30% do tamanho)
        margem = int(tamanho * 0.35)  # 35% de margem nas bordas
        tamanho_reduzido = int(tamanho * 0.3)  # 30% do tamanho original para a área central

        for _ in range(reino_jogador.populacao):
            # Ajustando x e y para a região central com 30% do tamanho
            x = random.randint(margem, margem + tamanho_reduzido - 1)
            y = random.randint(margem, margem + tamanho_reduzido - 1)

            humano = Animal_Sapien(
                self.raca_humana.simbolo, 100, 5,
                random.randint(18, 30), self.raca_humana, x, y
            )
            humanos.append(humano)

        return humanos
    
    def CriarReinos(self):
        reinos = []
        for i in range(self.n_reinos):
            raca = random.choice(self.Racas)
            reino = Reino(raca)
            reino.gerar_valores_aleatorios()
            reinos.append(reino)
            self.Reinos.append(reino)
        return reinos

    def CriarReligiao(self):
        self.Religiao_mundo = Religiao()
        self.Religiao_mundo.criarReligiao(self.Racas)
    
    def colocarReligiao(self,humanos):
        for humano in humanos:
            deus = random.choice(self.Religiao_mundo.deuses)
            humano.deus_adorado = deus


    def setReinoJogador(self,ouro,populacao,comida,Equipamento_militar,nome,personalidade,humanos,nome_reino):

        def Gerar_Caracteristicas():
            match personalidade:
                case "Beligerante":
                    reino_jogador.exercito.moral += 25
                    reino_jogador.exercito.preparo += 1
                    reino_jogador.exercito.moralMax += 25
                case "Religioso":
                    reino_jogador.magia += 2
                        
        reino_jogador = Reino(self.raca_humana)
        reino_jogador.criarReino(ouro,populacao,comida,Equipamento_militar,nome_reino)
        reino_jogador.gerarRei()
        reino_jogador.construcoes.append(Posto_Comercio(Madeira(),0,0))
        reino_jogador.construcoes.append(Armazem(Madeira(),0,0))
        reino_jogador.construcoes.append(Armazem_Comida(Madeira(),0,0))
        reino_jogador.construcoes.append(Armazem_materiais(Madeira(),0,0))
        
        reino_jogador.rei.nome = nome
        reino_jogador.Caracteristicas = personalidade
        Gerar_Caracteristicas()

        reino_jogador.setCidadoes(humanos)
        return reino_jogador

    def selecionarReinos(self):
        reinos = random.sample(self.Reinos, k=min(len(self.Reinos), random.randint(1, 3)))
        return reinos
    
    def criarTipoRegião(self):
        tipos_regiao =[
        {"nome": "Arquipélago", "pedrasMin": 15, "pedrasMax": 35, "vegetacaoMin": 20, "vegetacaoMax": 50, "minerios": 30},
        {"nome": "Montanhas", "pedrasMin": 20, "pedrasMax": 50, "vegetacaoMin": 3, "vegetacaoMax": 10, "minerios": 85},
        {"nome": "Montes", "pedrasMin": 18, "pedrasMax": 45, "vegetacaoMin": 5, "vegetacaoMax": 12, "minerios": 75},
        {"nome": "Florestas", "pedrasMin": 5, "pedrasMax": 20, "vegetacaoMin": 30, "vegetacaoMax": 60, "minerios": 25},
        {"nome": "Ilha", "pedrasMin": 10, "pedrasMax": 25, "vegetacaoMin": 15, "vegetacaoMax": 40, "minerios": 35},
        {"nome": "Continente", "pedrasMin": 30, "pedrasMax": 70, "vegetacaoMin": 25, "vegetacaoMax": 55, "minerios": 70},
        {"nome": "Península", "pedrasMin": 15, "pedrasMax": 40, "vegetacaoMin": 15, "vegetacaoMax": 35, "minerios": 40},
        {"nome": "Deserto", "pedrasMin": 10, "pedrasMax": 30, "vegetacaoMin": 0, "vegetacaoMax": 5, "minerios": 60},
        {"nome": "Planície", "pedrasMin": 8, "pedrasMax": 25, "vegetacaoMin": 20, "vegetacaoMax": 50, "minerios": 30},
        {"nome": "Pântano", "pedrasMin": 5, "pedrasMax": 15, "vegetacaoMin": 25, "vegetacaoMax": 55, "minerios": 15},
        {"nome": "Vale", "pedrasMin": 15, "pedrasMax": 40, "vegetacaoMin": 20, "vegetacaoMax": 45, "minerios": 50},
        {"nome": "Caverna", "pedrasMin": 40, "pedrasMax": 70, "vegetacaoMin": 0, "vegetacaoMax": 3, "minerios": 80},
        {"nome": "Vulcão", "pedrasMin": 50, "pedrasMax": 70, "vegetacaoMin": 0, "vegetacaoMax": 5, "minerios": 90},
        {"nome": "Cordilheira", "pedrasMin": 40, "pedrasMax": 65, "vegetacaoMin": 3, "vegetacaoMax": 10, "minerios": 85},
        {"nome": "Tundra", "pedrasMin": 20, "pedrasMax": 40, "vegetacaoMin": 0, "vegetacaoMax": 10, "minerios": 40},
        {"nome": "Taiga", "pedrasMin": 15, "pedrasMax": 35, "vegetacaoMin": 20, "vegetacaoMax": 45, "minerios": 35},
        {"nome": "Savana", "pedrasMin": 10, "pedrasMax": 25, "vegetacaoMin": 15, "vegetacaoMax": 40, "minerios": 20},
        {"nome": "Pantanal", "pedrasMin": 5, "pedrasMax": 15, "vegetacaoMin": 25, "vegetacaoMax": 55, "minerios": 15},
        {"nome": "Chapada", "pedrasMin": 15, "pedrasMax": 40, "vegetacaoMin": 10, "vegetacaoMax": 25, "minerios": 55},
        {"nome": "Altiplano", "pedrasMin": 20, "pedrasMax": 45, "vegetacaoMin": 5, "vegetacaoMax": 20, "minerios": 65},
        {"nome": "Cânion", "pedrasMin": 30, "pedrasMax": 60, "vegetacaoMin": 0, "vegetacaoMax": 10, "minerios": 75},
        {"nome": "Geleira", "pedrasMin": 20, "pedrasMax": 40, "vegetacaoMin": 0, "vegetacaoMax": 2, "minerios": 10},
        {"nome": "Selva", "pedrasMin": 5, "pedrasMax": 20, "vegetacaoMin": 30, "vegetacaoMax": 60, "minerios": 25},
        {"nome": "Costa", "pedrasMin": 10, "pedrasMax": 30, "vegetacaoMin": 15, "vegetacaoMax": 40, "minerios": 35},
        {"nome": "Mar Interior", "pedrasMin": 10, "pedrasMax": 25, "vegetacaoMin": 10, "vegetacaoMax": 35, "minerios": 30},
        {"nome": "Reino Subterrâneo", "pedrasMin": 50, "pedrasMax": 70, "vegetacaoMin": 0, "vegetacaoMax": 0, "minerios": 95},
        {"nome": "Terras Altas", "pedrasMin": 25, "pedrasMax": 55, "vegetacaoMin": 10, "vegetacaoMax": 30, "minerios": 60},
        {"nome": "Planalto", "pedrasMin": 15, "pedrasMax": 40, "vegetacaoMin": 15, "vegetacaoMax": 35, "minerios": 55},
        {"nome": "Cratera", "pedrasMin": 40, "pedrasMax": 70, "vegetacaoMin": 0, "vegetacaoMax": 10, "minerios": 85},
        {"nome": "Ruínas Antigas", "pedrasMin": 35, "pedrasMax": 60, "vegetacaoMin": 5, "vegetacaoMax": 20, "minerios": 70},
        {"nome": "Campos de Lava", "pedrasMin": 50, "pedrasMax": 70, "vegetacaoMin": 0, "vegetacaoMax": 0, "minerios": 90},
        {"nome": "Região Abissal", "pedrasMin": 25, "pedrasMax": 45, "vegetacaoMin": 0, "vegetacaoMax": 0, "minerios": 80},
        {"nome": "Estepes", "pedrasMin": 15, "pedrasMax": 40, "vegetacaoMin": 10, "vegetacaoMax": 30, "minerios": 30},
        {"nome": "Bosque Encantado", "pedrasMin": 10, "pedrasMax": 30, "vegetacaoMin": 30, "vegetacaoMax": 55, "minerios": 25},
        {"nome": "Terras Gélidas", "pedrasMin": 20, "pedrasMax": 45, "vegetacaoMin": 5, "vegetacaoMax": 15, "minerios": 35},
        {"nome": "Cinturão de Tempestades", "pedrasMin": 15, "pedrasMax": 35, "vegetacaoMin": 5, "vegetacaoMax": 20, "minerios": 40},
        {"nome": "Floresta Submersa", "pedrasMin": 5, "pedrasMax": 20, "vegetacaoMin": 25, "vegetacaoMax": 55, "minerios": 25},
        {"nome": "Zona de Penumbra", "pedrasMin": 10, "pedrasMax": 30, "vegetacaoMin": 10, "vegetacaoMax": 25, "minerios": 45},
        {"nome": "Ilhas Flutuantes", "pedrasMin": 10, "pedrasMax": 25, "vegetacaoMin": 15, "vegetacaoMax": 40, "minerios": 35},
        {"nome": "Terra Sagrada", "pedrasMin": 15, "pedrasMax": 40, "vegetacaoMin": 25, "vegetacaoMax": 50, "minerios": 50},
        {"nome": "Círculo de Pedra", "pedrasMin": 40, "pedrasMax": 70, "vegetacaoMin": 5, "vegetacaoMax": 15, "minerios": 80},
        {"nome": "Região Costeira", "pedrasMin": 15, "pedrasMax": 40, "vegetacaoMin": 20, "vegetacaoMax": 45, "minerios": 40},
        {"nome": "Desfiladeiro", "pedrasMin": 35, "pedrasMax": 60, "vegetacaoMin": 5, "vegetacaoMax": 15, "minerios": 70},
        {"nome": "Mar de Dunas", "pedrasMin": 25, "pedrasMax": 50, "vegetacaoMin": 0, "vegetacaoMax": 5, "minerios": 55},
        {"nome": "Oásis", "pedrasMin": 5, "pedrasMax": 15, "vegetacaoMin": 20, "vegetacaoMax": 50, "minerios": 20},
        {"nome": "Terra Erma", "pedrasMin": 10, "pedrasMax": 30, "vegetacaoMin": 5, "vegetacaoMax": 15, "minerios": 35},
        {"nome": "Reduto Escarpado", "pedrasMin": 35, "pedrasMax": 60, "vegetacaoMin": 10, "vegetacaoMax": 20, "minerios": 75},
        {"nome": "Abismo", "pedrasMin": 40, "pedrasMax": 70, "vegetacaoMin": 0, "vegetacaoMax": 5, "minerios": 90}
        ]

        tipo = random.choice(tipos_regiao)
        return tipo

    def temporaturaRegiao(self):
        temperaturaMax = random.randint(1,50)
        temperaturaMin = random.randint(-50,-1)
        return [{"tempMax":temperaturaMax, "tempMin":temperaturaMin}]

    def gerarNome(self,tipo, temperatura):
        self.media_temp = (temperatura[0]["tempMax"] + temperatura[0]["tempMin"]) / 2

        if self.media_temp < -20:
            clima = ["Congelada", "Gélida", "Glacial", "Ártica"]
        elif -20 <= self.media_temp < 0:
            clima = ["Fria", "Nevada", "Sombria"]
        elif 0 <= self.media_temp < 20:
            clima = ["Temperada", "Nebulosa", "Brumosa"]
        elif 20 <= self.media_temp < 35:
            clima = ["Quente", "Agradável", "Soleada"]
        else:
            clima = ["Escaldante", "Tórrida", "Abrangente"]

        adjetivo = random.choice(clima)
        return f"{tipo['nome']} {adjetivo}"
    def VegetacaoRegiao(self):
        if self.media_temp < -20:
            vegetal_list = [Uva, Alface, Cebola, Espinafre]  # resistentes ao frio
        elif -20 <= self.media_temp < 0:
            vegetal_list = [Maca, Cenoura, Batata, Beterraba, Rabanete, Inhame]  # raízes e maçã
        elif 0 <= self.media_temp < 20:
            vegetal_list = [Tomate, Morango, Uva, Manga, Pimentao, Espinafre]  # clima ameno
        elif 20 <= self.media_temp < 35:
            vegetal_list = [Laranja, Banana, Pepino, Abobora, Abacaxi, Melancia, Mandioca, Coco]
        else:
            vegetal_list = [Abobora, Banana, Pepino, Azeitona, Coco, Melancia]  # calor extremo

        return vegetal_list

    def selecionarAnimais(self):
        if self.media_temp < -20:
            # Frio extremo (tundra, gelo, nevasca)
            animais = [Urso, Lobo, Coruja, Veado, BichoPreguica, Cervo]

        elif -20 <= self.media_temp < 0:
            #Frio moderado (montanhas, floresta alpina)
            animais = [Urso, Lobo, Coruja, Veado, Cabra, Javali, Cervo, Falcao]

        elif 0 <= self.media_temp < 20:
            # Temperado (floresta, campo, colinas)
            animais = [
                Porco, Galinha, Coelho, Raposa, Coruja, Veado, Lobo, Gato, 
                Cachorro, Ovelha, Pato, Tamandua, Morcego
            ]

        elif 20 <= self.media_temp < 35:
            # Quente (savana, floresta tropical, pantanal, deserto leve)
            animais = [
                Leao, Elefante, Tigre, Anta, Cavalo, Cobra, Camelo, Sapo, 
                Tartaruga, Jacare, Ganso, Pato, Lhama, Peru, Burro, Onca, 
                Tamandua
            ]

        else:
            # Calor extremo (deserto escaldante, regiões áridas e cavernas)
            animais = [Camelo, Cobra, Jacare, Morcego, Onca, Falcao]

        return animais


    def gerarNomeMundo(self):

        prefixos_lugar = [
            "Mundo",
            "Terras",
            "O Lar de",
            "As Ilhas de",
            "Reino de",
            "Domínio de",
            "Vale de",
            "Montanhas de",
            "Floresta de",
            "Planícies de",
            "Cidades de",
            "Província de",
            "Ilhas de",
            "Região de",
            "Território de"
        ]

        nomes_adjetivos = [
            "Eterna",
            "Sombrio",
            "Dourado",
            "Esquecido",
            "Sagrado",
            "Místico",
            "Perdido",
            "Celestial",
            "Silencioso",
            "Tempestuoso",
            "Encantado",
            "Glorioso",
            "Próspero",
            "Antigo",
            "Ferro",
            "Vento",
            "Água",
            "Fogo",
            "Raiz",
            "Luz",
            "Sombra",
            "Brisa"
        ]

        prefixo = random.choice(prefixos_lugar)
        nome = random.choice(nomes_adjetivos)
        return f"{prefixo} {nome}"

    def criarMundo(self):

        nome = self.gerarNomeMundo()
        reinos = self.Reinos
        monstros = self.MonstrosList
        racas = self.Racas
        regioes = self.RegioesList
        return Mundo(nome,reinos,monstros,racas,regioes,self.Religiao_mundo,self.Cultura_Lista,self.retornarCriaturas())

    def retornarCriaturas(self):
        # Criaturas Míticas
        dragao = Raca(
            nome="Dragão",
            simbolo="🔥",
            vida=300,
            dano=50,
            altura="5m a 20m",
            aparencia="corpo imenso coberto por escamas, asas gigantescas, olhos brilhantes",
            forca=10,
            destreza=6,
            inteligencia=8,
            carisma=7,
            constituicao=10
        )

        quimera = Raca(
            nome="Quimera",
            simbolo="🐉🦁🐐",
            vida=220,
            dano=40,
            altura="3m",
            aparencia="corpo com partes de leão, cabra e serpente",
            forca=9,
            destreza=5,
            inteligencia=4,
            carisma=2,
            constituicao=8
        )

        griffo = Raca(
            nome="Grifo",
            simbolo="🦅🦁",
            vida=180,
            dano=30,
            altura="2.5m",
            aparencia="corpo de leão com cabeça e asas de águia",
            forca=7,
            destreza=9,
            inteligencia=6,
            carisma=5,
            constituicao=6
        )

        # Criaturas das Sombras
        hidra = Raca(
            nome="Hidra",
            simbolo="🐍🐍🐍",
            vida=250,
            dano=45,
            altura="4m",
            aparencia="serpente gigante com várias cabeças regenerativas",
            forca=9,
            destreza=4,
            inteligencia=3,
            carisma=2,
            constituicao=10
        )

        espectro = Raca(
            nome="Espectro",
            simbolo="👻",
            vida=120,
            dano=25,
            altura="1.8m (etéreo)",
            aparencia="figura fantasmagórica envolta em névoa negra",
            forca=2,
            destreza=8,
            inteligencia=7,
            carisma=6,
            constituicao=3
        )

        basilisco = Raca(
            nome="Basilisco",
            simbolo="🐍👁️",
            vida=210,
            dano=38,
            altura="3m",
            aparencia="lagarto gigante com olhar petrificante",
            forca=7,
            destreza=6,
            inteligencia=5,
            carisma=1,
            constituicao=9
        )

        # Bestas Elementais
        elemental_fogo = Raca(
            nome="Elemental do Fogo",
            simbolo="🔥",
            vida=160,
            dano=40,
            altura="2m a 4m",
            aparencia="ser feito inteiramente de chamas vivas",
            forca=6,
            destreza=7,
            inteligencia=6,
            carisma=4,
            constituicao=6
        )

        elemental_gelo = Raca(
            nome="Elemental do Gelo",
            simbolo="❄️",
            vida=170,
            dano=35,
            altura="2.2m",
            aparencia="figura humanoide cristalizada com vapor frio ao redor",
            forca=5,
            destreza=6,
            inteligencia=7,
            carisma=3,
            constituicao=7
        )

        # Bestas Terrenas
        troll = Raca(
            nome="Troll",
            simbolo="🪨",
            vida=250,
            dano=28,
            altura="2.8m",
            aparencia="criatura gigante, de pele esverdeada e músculos grossos",
            forca=9,
            destreza=3,
            inteligencia=2,
            carisma=1,
            constituicao=9
        )

        arakora = Raca(
            nome="Arakora",
            simbolo="🦅",
            vida=140,
            dano=22,
            altura="1.9m",
            aparencia="ser alado com traços de águia e corpo humanoide",
            forca=5,
            destreza=9,
            inteligencia=6,
            carisma=6,
            constituicao=4
        )

        minotauro = Raca(
            nome="Minotauro",
            simbolo="🐂",
            vida=230,
            dano=33,
            altura="2.5m",
            aparencia="corpo humanoide musculoso com cabeça de touro",
            forca=10,
            destreza=4,
            inteligencia=3,
            carisma=2,
            constituicao=8
        )
    
        return [dragao,quimera,griffo,hidra,espectro,basilisco,elemental_fogo,elemental_gelo,troll,arakora,minotauro]



    def criarRegioes(self):
        temperaturas = []

        for i in range(self.n_regioes):
            
            tipo = self.criarTipoRegião()
            temperatura = self.temporaturaRegiao()
            nome = self.gerarNome(tipo,temperatura)
            animais = self.selecionarAnimais()
            vegetal = self.VegetacaoRegiao()
            reinos = self.selecionarReinos()

            riqueza_mineral = tipo["minerios"]/100
            temperaturas.append(temperatura)

            quantidade_criatura = random.randint(3,len(self.retornarCriaturas())-1)
            
            criaturas = random.sample(self.retornarCriaturas(),quantidade_criatura)
            regiao = Regioes(nome,tipo,animais,reinos,temperatura,vegetal,riqueza_mineral,criaturas)
            self.RegioesList.append(regiao)
        
        for regiao in self.RegioesList:
            for reino in regiao.reinos:
                cultura_criada = reino.gerarCultura(regiao.temperatura)
                self.Cultura_Lista.append(cultura_criada)

    def gerarEstruturas(self):
        for regiao in self.RegioesList:
            def gerar_local(regiao):
                quantidade = random.randint(10,30)
                #Reino_perdido,Tribo_Encontro,
                locais = [Ruinas_antigas,Roubo_item]

                for i in range(quantidade):
                    local = random.choice(locais)
                    raca = random.choice(self.Racas)
                    regiao.Estruturas.append(local(raca,self.Mundo_criado))
            gerar_local(regiao)

    def GerarHistoria(self):
        self.historia = Historia(self.Mundo_criado,self.Ano)
        self.historia.IniciarHistoria()

    def GerarMundo(self):
        
        self.gerarMonstrons()
        self.CriarRacas()
        self.Reinos = self.CriarReinos()
        self.criarRegioes()
        self.CriarReligiao()
        self.Mundo_criado = self.criarMundo()
        self.gerarEstruturas()
        self.GerarHistoria()

    # Outras funções devem seguir a mesma lógica
    # self.Metodo(...) ou self.atributo onde necessário
