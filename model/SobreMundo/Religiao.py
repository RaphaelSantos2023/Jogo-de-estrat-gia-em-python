import random
from model.Meteriais.comida import Comida
from colorama import Fore, Style, init

nomes = [
    "Xoxo", "Yithog", "Gotep", "Th'shu", "Tlaglnia", "Yakgu", "Arza", "Sochthu", "Rhoko", "Nathshathli",
    "Lhufaugn", "C'thada", "Ph'nc'thun", "Go", "Lothtep", "Chton", "Gu", "Guac'tha", "Cthun", "Y'rath",
    "Chaugkag", "Thurde", "Yugtli", "Tlachquah", "Mitho", "Quahshub", "Thartur", "Mnomm'ell", "Soc'thun", "Mak'n",
    "Nemchthon", "Gocha", "Ogxa", "Cthonagl", "Dhrahoth", "Chthonyig", "Shagog", "Lothc'thal", "Nacgua", "Y'x'o",
    "Bladespear", "Glazeglider", "Lordbrightlander", "Furycape", "Daggershadow", "Ragelander", "Metalnose",
    "Gazeoaken", "Stormrain", "Eyesblade", "Silvermoon", "Morningmane", "Silverwarg", "Darkaxefire",
    "Autumnaxe", "Dusklong", "Steelforge", "Yellowcape", "Whitegate", "Walkerlock"
]

alinhamento = ["Neutro","Caos","Ordem"]

dominios_sufixos = [
    {"Dominio": "Natureza", "Sufixos": ["O Verdejante", "A Raiz Eterna", "O Guardião das Florestas"]},
    {"Dominio": "Guerra", "Sufixos": ["O Sangrento", "A Lança Eterna", "O Brado de Ferro"]},
    {"Dominio": "Morte", "Sufixos": ["O Silencioso", "A Sombra Final", "O Julgador dos Fins"]},
    {"Dominio": "Luz", "Sufixos": ["O Radiante", "O Portador da Aurora", "A Chama Pura"]},
    {"Dominio": "Trevas", "Sufixos": ["O Oculto", "A Noite Sem Fim", "O Véu Sombrio"]},
    {"Dominio": "Conhecimento", "Sufixos": ["O Insondável", "O Guardião dos Segredos", "A Mente Infinita"]},
    {"Dominio": "Fertilidade", "Sufixos": ["A Mãe Abundante", "O Semeador", "O Ventre da Terra"]},
    {"Dominio": "Tecnologia", "Sufixos": ["O Engenhoso", "A Mente de Ferro", "O Tecedor de Engrenagens"]},
    {"Dominio": "Sonhos", "Sufixos": ["O Onírico", "O Senhor dos Devaneios", "O Tecelão do Impossível"]},
    {"Dominio": "Oceanos", "Sufixos": ["O Abissal", "O Sussurro das Marés", "A Fúria das Águas"]},
    {"Dominio": "Comércio", "Sufixos": ["O Dourado", "O Mestre da Barganha", "O Contador das Moedas"]},
    {"Dominio": "Tempo", "Sufixos": ["O Memoroso", "O Vigia", "O Tecelão da Eternidade"]}
]

caracteristicas = [
  {"Nome":"Trapaceiro","Comida":5,"Ouro":20,"Material":10,"vidas":2},
  {"Nome":"Honesto","Comida":8,"Ouro":15,"Material":12,"vidas":3},
  {"Nome":"Leal","Comida":6,"Ouro":18,"Material":11,"vidas":3},
  {"Nome":"Corajoso","Comida":7,"Ouro":22,"Material":9,"vidas":4},
  {"Nome":"Tímido","Comida":4,"Ouro":12,"Material":8,"vidas":2},
  {"Nome":"Ambicioso","Comida":6,"Ouro":25,"Material":13,"vidas":2},
  {"Nome":"Generoso","Comida":10,"Ouro":10,"Material":10,"vidas":3},
  {"Nome":"Injusto","Comida":3,"Ouro":30,"Material":7,"vidas":1},
  {"Nome":"Justo","Comida":9,"Ouro":14,"Material":12,"vidas":4},
  {"Nome":"Sábio","Comida":5,"Ouro":17,"Material":15,"vidas":4},
  {"Nome":"Ingênuo","Comida":6,"Ouro":10,"Material":9,"vidas":2},
  {"Nome":"Lutador","Comida":7,"Ouro":20,"Material":14,"vidas":5},
  {"Nome":"Pacifista","Comida":8,"Ouro":12,"Material":10,"vidas":3},
  {"Nome":"Aventureiro","Comida":9,"Ouro":23,"Material":11,"vidas":4}
]

tipos_organizacoes_religiosas = [
    "Igreja",
    "Templo",
    "Culto",
    "Ordem",
    "Seita",
    "Círculo",
    "Secto",
    "Clero",
    "Fraternidade",
    "Confraria",
    "Hermandade",
    "Aliança",
    "Sociedade",
    "Assembleia",
    "Congregação",
    "Legião Sagrada",
    "Cabala",
    "Sinédrio",
    "Enclave"
]

class Deuses:
  def __init__(self,dominio,raca):
    self.dominio = dominio 
    titulo = self.gerar_titulo(dominio)
    self.nome = random.choice(nomes) + ", " + titulo
    self.personalidade = random.choice(caracteristicas)
    self.Bencao_Descricao  = []
    self.Quantidade_animais = random.choice([7,14,21])
    self.raca = raca
    self.descricao_fisica = f"{self.nome} é a dinvidade da(o) {self.dominio}  dos {self.raca}"

  def GetBencao(self,alvo,alinhamento,quantidade_sacrificada_total,intensidade):

    if quantidade_sacrificada_total < self.Quantidade_animais:
        print(f">>>{Fore.LIGHTRED_EX}{self.nome} não parece estar satisfeito com o sacrificio")
    else:
        print(f"{Fore.LIGHTYELLOW_EX}>>>O sacrificio queimou e a fumaça sobre em espiral para o céu. {self.nome}\nparece estar satisfeito com o sacrificio\n")
        match alinhamento:
            case "Neutro":
                self.Bencao_Neutro(alvo,intensidade)
            case "Caos":
                self.Bencao_Caos(alvo,intensidade)
            case "Ordem":
                self.Bencao_Ordem(alvo,intensidade)
    
  def Bencao_Ordem(self,alvo,intensidade):
    return 
  def Bencao_Caos(self,alvo,intensidade):
    return

  def Bencao_Neutro(self,alvo,intensidade):
    return

  def gerar_titulo(self, dominio):
    for item in dominios_sufixos:
        if item["Dominio"] == dominio:
            return random.choice(item["Sufixos"])
    return ""

  def Descricao(self):
        personalidade = self.personalidade["Nome"]
        descricao = (
            f"\n🕯️ Nome: {self.nome}\n"
            f"📖 Domínio: {self.dominio}\n"
            f"🧬 Raça que o venera: {self.raca.nome}\n"
            f"🎭 Personalidade: {personalidade}\n"
            f"\n{self.nome} é adorado por muitos como a divindade do(a) {self.dominio}, "
            f" de espirito {personalidade.lower()} "
            f"aos {self.raca.nome}. Seus seguidores acreditam que sua vontade se manifesta "
            f"através de eventos sobrenaturais ligados ao seu domínio sagrado.\n"
        )
        return descricao
  
class DeusNatureza(Deuses):
    def __init__(self,raca):
        super().__init__("Natureza",raca)
        self.Bencao_Descricao = {
            "Ordem": "Cura os ferimentos e restaura a saúde.",
            "Neutro": "Aumenta a fertilidade de seus animais",
            "Caos": "Cria um desastre natural imprevisível no local."
        }
        
    def Bencao_Ordem(self, alvo, intensidade):
        curar(alvo, intensidade)

    def Bencao_Caos(self, alvo, intensidade):
        desastreNatural(alvo, intensidade)

    def Bencao_Neutro(self, alvo, intensidade):
        aumentar_fertilidade(alvo, intensidade)

class DeusGuerra(Deuses):
    def __init__(self,raca):
        super().__init__("Guerra",raca)
        self.Bencao_Descricao = {
            "Ordem": "Concede bênçãos estratégicas e força a guerreiros aliados.",
            "Neutro": "Inspira coragem e aumenta a moral das tropas.",
            "Caos": "Aumenta o dano físico causado, mas reduz o controle."
        }
    
    def Bencao_Ordem(self, alvo, intensidade):
        abencaoBatalha(alvo, intensidade)

    def Bencao_Caos(self, alvo, intensidade):
        aumentarDano(alvo, intensidade)

    def Bencao_Neutro(self, alvo, intensidade):
        reforcarMoral(alvo, intensidade)

class DeusMorte(Deuses):
    def __init__(self,raca):
        super().__init__("Morte",raca)
        self.Bencao_Descricao = {
            "Ordem": "Permite recuperar alguém recém-morto.",
            "Neutro": "Espalha doenças naturais pelo território.",
            "Caos": "Libera uma praga sobrenatural devastadora."
        }

    def Bencao_Ordem(self, alvo, intensidade):
        resgatarDaMorte(alvo)

    def Bencao_Caos(self, alvo, intensidade):
        pragaDivina(alvo, intensidade)

    def Bencao_Neutro(self, alvo, intensidade):
        doencasPragas(alvo, intensidade)

class DeusLuz(Deuses):
    def __init__(self,raca):
        super().__init__("Luz",raca)
        self.Bencao_Descricao = {
            "Ordem": "Cura feridas e purifica o corpo.",
            "Neutro": "Melhora a capacidade intelectual do alvo.",
            "Caos": "Confunde e reduz a inteligência do inimigo."
        }
    
    def Bencao_Ordem(self, alvo, intensidade):
        curar(alvo, intensidade)

    def Bencao_Caos(self, alvo, intensidade):
        diminuirInteligencia(alvo, intensidade)

    def Bencao_Neutro(self, alvo, intensidade):
        aumentarInteligencia(alvo, intensidade)

class DeusTrevas(Deuses):
    def __init__(self,raca):
        super().__init__("Trevas",raca)
        self.Bencao_Descricao = {
            "Ordem": "Reduz os danos sofridos com bênçãos sombrias defensivas.",
            "Neutro": "Libera pragas moderadas contra os inimigos.",
            "Caos": "Espalha doenças agressivas e imprevisíveis."
        }
    
    def Bencao_Ordem(self, alvo, intensidade):
        reduzirDano(alvo, intensidade)

    def Bencao_Caos(self, alvo, intensidade):
        doencasPragas(alvo, intensidade)

    def Bencao_Neutro(self, alvo, intensidade):
        pragaDivina(alvo, intensidade)

class DeusConhecimento(Deuses):
    def __init__(self,raca):
        super().__init__("Conhecimento",raca)
        self.Bencao_Descricao = {
            "Ordem": "Aumenta a inteligência e o raciocínio lógico.",
            "Neutro": "Fortalece a moral através do conhecimento compartilhado.",
            "Caos": "Confunde com excesso de informações contraditórias."
        }
    
    def Bencao_Ordem(self, alvo, intensidade):
        aumentarInteligencia(alvo, intensidade)

    def Bencao_Caos(self, alvo, intensidade):
        diminuirInteligencia(alvo, intensidade)

    def Bencao_Neutro(self, alvo, intensidade):
        reforcarMoral(alvo, intensidade)

class DeusFertilidade(Deuses):
    def __init__(self,raca):
        super().__init__("Fertilidade",raca)
        self.Bencao_Descricao = {
            "Ordem": "Faz as colheitas prosperarem e estimula a natalidade.",
            "Neutro": "Controla o clima para favorecer a produção.",
            "Caos": "Reduz o número de animais e fertilidade com pragas."
        }
    
    def Bencao_Ordem(self, alvo, intensidade):
        abencaoFertilidade(alvo, intensidade)

    def Bencao_Caos(self, alvo, intensidade):
        diminuirAnimais(alvo, intensidade)

    def Bencao_Neutro(self, alvo, intensidade):
        aumentar_fertilidade(alvo, intensidade)

class DeusTecnologia(Deuses):
    def __init__(self, raca):
        super().__init__("Tecnologia", raca)
        self.Bencao_Descricao = {
            "Ordem": "Impulsiona a inteligência com aprimoramento tecnológico.",
            "Neutro": "Motiva os aliados com inspiração científica.",
            "Caos": "Sobrecarrega o conhecimento, causando confusão."
        }

    def Bencao_Ordem(self, alvo, intensidade):
        aumentarInteligencia(alvo, intensidade * 2)

    def Bencao_Caos(self, alvo, intensidade):
        diminuirInteligencia(alvo, intensidade)

    def Bencao_Neutro(self, alvo, intensidade):
        reforcarMoral(alvo, intensidade)

class DeusSonhos(Deuses):
    def __init__(self, raca):
        super().__init__("Sonhos", raca)
        self.Bencao_Descricao = {
            "Ordem": "Cura através de sonhos tranquilos e reparadores.",
            "Neutro": "Estimula visões criativas que aumentam a inteligência.",
            "Caos": "Espalha pesadelos que causam doenças mentais e físicas."
        }

    def Bencao_Ordem(self, alvo, intensidade):
        curar(alvo, intensidade)

    def Bencao_Caos(self, alvo, intensidade):
        doencasPragas(alvo, intensidade)

    def Bencao_Neutro(self, alvo, intensidade):
        aumentarInteligencia(alvo, intensidade)

class DeusOceanos(Deuses):
    def __init__(self, raca):
        super().__init__("Oceanos", raca)
        self.Bencao_Descricao = {
            "Ordem": "Cria enchentes controladas para irrigar terras.",
            "Neutro": "Melhora a fertilidade por meio da abundância marinha.",
            "Caos": "Desencadeia tsunamis ou tempestades marinhas destrutivas."
        }

    def Bencao_Ordem(self, alvo, intensidade):
        aumentar_fertilidade(alvo, intensidade)

    def Bencao_Caos(self, alvo, intensidade):
        desastreNatural(alvo, intensidade)

    def Bencao_Neutro(self, alvo, intensidade):
        abencaoFertilidade(alvo, intensidade)

class DeusComercio(Deuses):
    def __init__(self, raca):
        super().__init__("Comércio", raca)
        self.Bencao_Descricao = {
            "Ordem": "Aumenta os lucros e garante negociações justas.",
            "Neutro": "Enche os cofres e atrai oportunidades.",
            "Caos": "Atrai riquezas rápidas, porém instáveis."
        }

    def Bencao_Ordem(self, alvo, intensidade):
        abencaoOuro(alvo, intensidade)

    def Bencao_Caos(self, alvo, intensidade):
        riquezaCelestial(alvo, intensidade)

    def Bencao_Neutro(self, alvo, intensidade):
        encherCofre(alvo, intensidade)

class DeusTempo(Deuses):
    def __init__(self,raca):
        super().__init__("Tempo",raca)
        self.Bencao_Descricao = {
            "Ordem": "Garante estabilidade econômica ao longo do tempo.",
            "Neutro": "Concede riquezas de forma progressiva.",
            "Caos": "Oferece riqueza súbita por meio de distorções temporais."
        }
    
    def Bencao_Ordem(self, alvo, intensidade):
        encherCofre(alvo, intensidade)

    def Bencao_Caos(self, alvo, intensidade):
        riquezaCelestial(alvo, intensidade)

    def Bencao_Neutro(self, alvo, intensidade):
        abencaoOuro(alvo, intensidade)

class Religiao:
  def __init__(self):
    self.nome = ""
    self.deuses = []

  def criarReligiao(self,racas):
    self.criarDeuses(racas)
    self.criarNome()

  def criarDeuses(self,racas):
    tipos_deuses = [
          DeusNatureza, DeusGuerra, DeusMorte, DeusLuz, DeusTrevas, DeusConhecimento,
          DeusFertilidade, DeusTempo, DeusTecnologia, DeusSonhos, DeusOceanos, DeusComercio
      ]

    for i in range(len(tipos_deuses)):
        especie_deuses = random.choice(racas)
        divindade = tipos_deuses[i](especie_deuses)

        self.deuses.append(divindade)

  def criarNome(self):
    sufixos = ["do Caos", "da Destruição",  "da Dissolução", "da Corrupção", "da Obscuridade", "da Desintegração", "da Desolação","da Ordem", "da Harmonia", "da Estabilidade", "da Disciplina", "da Paz", "da Virtude", "da Luz", "da Pureza", "da Unidade","da Equilíbrio", "da Moderção", "da Tranquilidade", "da Serenidade", "da Harmonia", "da Paciência", "da Sabedoria", "da Prudência", "da Justiça"]

    self.nome = random.choice(tipos_organizacoes_religiosas) + " " +random.choice(sufixos)

  def DescreverDeuses(self):
      text = "\nDeuses: \n"
      for i in range(len(self.deuses)):
          text += self.deuses[i].Descricao()
      text += "\n\n"
      return text
    
  def Descricao(self):
    text = f"Religião: {self.nome} \nAlinhamento: {self.tipo}"
    text += self.DescreverDeuses()
    return text

import random

def curar(alvo=None, intensidade=0.1):

    curados_feridos = []
    curados_doentes= []

    def Contarferidos(cidadaos):
        return [c for c in cidadaos if c.Ferido]

    def ContarDoentes(cidadaos):
        return [c for c in cidadaos if c.Doente]

    def Curar_Feridos(array):
        for cidadao in array:
            cidadao.Ferido = False

    def Curar_Doencas(array):
        for cidadao in array:
            cidadao.Doente = False

    # Garantir que intensidade seja entre 0 e 1
    intensidade = max(0, min(intensidade, 1))

    feridos = Contarferidos(alvo.cidadaos)
    doentes = ContarDoentes(alvo.cidadaos)

    if feridos != []:
        n_feridos = max(1, int(len(feridos) * intensidade)) if feridos else 0
        curados_feridos = random.sample(feridos, min(n_feridos, len(feridos)))
        Curar_Feridos(curados_feridos)

    if  doentes !=  []:
        n_doentes = max(1, int(len(doentes) * intensidade)) if doentes else 0
        curados_doentes = random.sample(doentes, min(n_doentes, len(doentes)))
        Curar_Doencas(curados_doentes)


    total_curados = len(curados_feridos) + len(curados_doentes)
    if total_curados != 0:
        print(f"{Fore.LIGHTGREEN_EX}>>> O tempo ficou lento e a natureza pareceu resplandecer, de subito.\nDiante dos seus olhos, os feridos tiveram suas feridas cicatrizadas \ncomo se numca as tiveram e os doentes perderam a\npalidez e a fracqueza do corpo!\n\nForam curadas {total_curados} pessoas.")
    else:
        print(f"{Fore.LIGHTGREEN_EX}>>> Vocês sentem uma presença perambular pelo reino, mas logo ela desa-\nparece, tendo visto não ter nenhum ferido ou doente em sua população.")


def encherCofre(alvo=None, intensidade=1):
    aumento_ouro = intensidade * 10
    alvo.ouro += aumento_ouro
    
    print(f"O cofre de {alvo.nome} foi preenchido! {aumento_ouro} de ouro foram adicionados.")

def doencasPragas(alvo=None, intensidade=1):
    perda_vida = intensidade * 10
    alvo.vida -= perda_vida
    print(f"{alvo.nome} foi atingido por uma praga! {perda_vida} de vida foram perdidos.")

def aumentarDano(alvo=None, intensidade=1):
    for soldado in alvo.exercito:
        soldado.dano += intensidade * 2
    print(f"O dano dos soldados de {alvo.nome} aumentou! {intensidade * 2} de dano foram adicionados a cada soldado.")

def reduzirDano(alvo=None, intensidade=1):
    for soldado in alvo.exercito:
        soldado.dano -= intensidade * 2
    print(f"O dano dos soldados de {alvo.nome} foi reduzido! {intensidade * 2} de dano foram subtraídos de cada soldado.")

def aumentarInteligencia(alvo=None, intensidade=1):
    aumento_inteligencia = intensidade * 2
    alvo.inteligencia += aumento_inteligencia
    print(f"A inteligência de {alvo.nome} aumentou! {aumento_inteligencia} de inteligência foram adicionados.")

def diminuirInteligencia(alvo=None, intensidade=1):
    perda_inteligencia = intensidade * 2
    alvo.inteligencia -= perda_inteligencia
    print(f"A inteligência de {alvo.nome} foi reduzida! {perda_inteligencia} de inteligência foram subtraídos.")

def diminuirAnimais(alvo=None, intensidade=1):
    perda_animais = intensidade * 5
    alvo.animais -= perda_animais
    print(f"{alvo.nome} perdeu {perda_animais} animais devido a uma maldição.")

def reforcarMoral(alvo=None, intensidade=1):
    """Aumenta o moral da população, o que melhora a produtividade e a felicidade."""
    aumento_moral = intensidade * 5
    alvo.moral += aumento_moral
    print(f"O moral da população em {alvo.nome} aumentou em {aumento_moral}.")

def desastreNatural(alvo=None, intensidade=1):
    dano_construcoes = intensidade * 2
    quantidade_destruida = 0

    for construcao in alvo.construcoes:
        construcao.vida -= dano_construcoes
        if construcao.vida <= 0:
            quantidade_destruida += 1
            alvo.construcoes.remove(construcao)
    
    if quantidade_destruida > 0:
        print(f"{Fore.LIGHTMAGENTA_EX}>>> O céu se encobriu e ventos colossais uivaram pelas terras de {alvo.nome}.\n"
              f"Estrondos e ruínas marcaram o fim de {quantidade_destruida} construções,\n"
              f"que agora não passam de escombros e lembranças do que um dia foram.")
    else:
        print(f">>> Nuvens sombrias rondaram {alvo.nome}, mas nada foi levado desta vez.\n"
              f"As construções resistiram bravamente aos caprichos da natureza.")

def abencaoFertilidade(alvo=None, intensidade=1):
    aumento_comida = intensidade * 25
    armazens = [c for c in alvo.construcoes if c.nome == "Armazem" and len(c.inventario) > 0]

    if not armazens:
        print("Não há armazéns com comida.")
        return

    armazem = random.choice(armazens)
    inventario = armazem.inventario

    # Filtra apenas os itens que têm 'Quantidade' e são comestíveis (você pode ajustar o filtro se quiser)
    comestiveis = [item for item in inventario if isinstance(item, dict) and  isinstance(item['Nome'],Comida) and"Quantidade" in item]

    if not comestiveis:
        print("O inventário do armazém não tem itens Comida.")
        return

    # Limita quantos itens vão receber a benção
    max_itens = min(len(comestiveis), aumento_comida)
    num_escolhidos = random.randint(1, max_itens)

    escolhidos = random.sample(comestiveis, num_escolhidos)

    # Distribui a quantidade entre os escolhidos
    partes = [0] * num_escolhidos
    for _ in range(aumento_comida):
        partes[random.randint(0, num_escolhidos - 1)] += 1

    for item, incremento in zip(escolhidos, partes):
        item["Quantidade"] += incremento


    print(f"A benção de fertilidade aumentou a produção de comida em {aumento_comida}.")

def abencaoOuro(alvo=None, intensidade=1):
    """Aumenta a quantidade de ouro no reino."""
    aumento_ouro = intensidade * 500
    alvo.ouro += aumento_ouro
    print(f"O reino {alvo.nome} recebeu {aumento_ouro} de ouro como presente divino.")

def resgatarDaMorte(alvo=None):
    """Revive um soldado ou cidadão importante."""
    if alvo:
        alvo.vida = alvo.vida_maxima  # Restaura a vida do alvo
        print(f"{alvo.nome} foi revivido e agora está completamente restaurado.")

def abencaoBatalha(alvo=None, intensidade=1):
    """Aumenta as habilidades dos soldados, como dano ou defesa."""
    for soldado in alvo.exercito:
        soldado.dano += intensidade * 3
    print(f"Os soldados do reino {alvo.nome} receberam uma bênção de batalha, aumentando seu dano.")

def aumentar_fertilidade(alvo=None, intensidade=1):
    intensidade = max(0, min(intensidade, 1))
    
    alvo.Turnos_reproducao = 10

    if intensidade < 1:
        alvo.chance_reproducao += intensidade
    else:
        alvo.chance_reproducao += 1

    print(f"{Fore.LIGHTCYAN_EX}>>> Um calor suave percorre os campos, e um aroma de vida fresca invade o ar.\nPor um instante, tudo silencia... então, os ventres se enchem, os ninhos se multiplicam,\ne as crias despertam antes mesmo de nascer.\n\n")

def riquezaCelestial(alvo=None, intensidade=1):
    """Gera uma grande quantidade de ouro, mas com consequências em longo prazo."""
    aumento_ouro = intensidade * 1000
    custo_comida = intensidade * 500  # O aumento de ouro pode diminuir a comida

    alvo.ouro += aumento_ouro
    alvo.Comida -= custo_comida

    print(f"A riqueza celestial trouxe {aumento_ouro} de ouro para {alvo.nome}, mas custou {custo_comida} de comida.")

def pragaDivina(alvo=None, intensidade=1):
    """Uma praga divina diminui a população e afeta a comida."""
    perda_populacao = intensidade * 10
    perda_comida = intensidade * 500

    alvo.populacao -= perda_populacao
    alvo.Comida -= perda_comida

    print(f"A praga divina causou a perda de {perda_populacao} cidadãos e {perda_comida} de comida em {alvo.nome}.")

