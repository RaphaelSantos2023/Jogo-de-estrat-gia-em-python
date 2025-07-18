from model.Animais.animal import Animal
from colorama import Fore, Style, init
from model.Animais.Membros import Corpo
import random

nomes = [
    "Imkhay", "Moranly", "Tzacue", "Nisthi", "Naxa", "Altari", "Kha", "Ronrose", "Bolphe", "Sitsthal",
    "Dinora", "Thasah", "Kon'nee", "Tari", "Hualpar", "Diahagud", "Chio", "Thysis", "Thesgro", "Cthu",

    "Zzrirat", "Begar", "Radbeorth", "Smalttabak", "Cuetzlonro", "Lotlrid", "Galmus", "Drornna", "So", "Caadal",
    "Tathus", "Isum'xa", "Lordain", "Tisma", "Glana", "Thusvorg", "Ceton", "Dauz", "Silbe", "Reshde",

    "Shiba", "Sahamkeem", "Za-li", "Coyawi", "Uylvia", "Liramsorthky", "Slish'ra", "Shadaru", "Roth'nu", "Mal'mo",
    "Noenma", "Xoquetlim", "Htisthphor", "Lancthedil", "Aenli", "Athtskhi", "Zac-fu", "Bigaimil", "Shambericbryt", "Lagarich",

    "Sulgud'tar", "Jaleteshid", "Nieldhaneesal", "Rakuasfa", "Les'mibel", "Ne'drarghua", "Imastshaszaa", "Ushangfastvarordi", "Tsa'forsa", "Bemularahpa",
    "Dacmacyntuf", "Drelalbasals", "Noveratifas", "Gel-isa", "Ithtshasbucu", "Ysatlalmic", "Tulflamminshihten", "Jaxizzlasfur", "Nerpaisola", "Kihisstisthchoy"
]

adjetivos = [
    "o Temível",
    "o Flagelo dos Céus",
    "o Carrasco de Almas",
    "o Imperador do Sul",
    "o Sussurro na Escuridão",
    "o Despertar do Abismo",
    "o Quebrador de Mundos",
    "o Devorador de Sóis",
    "o Profanador de Tumbas",
    "o Sangue Inquieto",
    "o Grito do Vazio",
    "o Senhor das Moscas",
    "o Caçador de Esperanças",
    "o Rei Enferrujado",
    "o Lamento Eterno",
    "o Olho Sem Pálpebra",
    "o Filho do Caos",
    "o Herdeiro do Fim",
    "o Inominável",
    "o Engolidor de Chamas",
    "o Eco das Trevas",
    "o Fim em Carne",
    "o Antigo que Vigia",
    "o Último Flagelo",
    "o Mestre da Dor",
    "o Vulto de Mil Faces",
    "o Hálito da Morte",
    "o Guardião da Ruína",
    "o Que Habita nas Profundezas",
    "o Esquecido pelo Tempo"
]

cores = [
  "vermelho", "azul", "verde", "amarelo", "laranja",
  "roxo", "rosa", "marrom", "cinza", "preto",
  "branco", "turquesa", "ciano", "magenta", "bege",
  "dourado", "prata", "violeta", "índigo", "salmon",
  "azul-marinho", "verde-oliva", "coral", "pêssego", "menta"
]

tipo_corpo = ["Humanoide", "Aracnídeo", "Reptiliano","Insectoide","Gosma","Fungoide"]
texturas = ["escamosa", "lisa", "viscosa", "espinhosa", "peluda"]
formas = ["esquelética", "musculosa", "obesa", "alongada", "compacta"]
pele_extra = ["com verrugas", "luminescente", "coberta por limo", "com veias pulsantes", "com runas entalhadas"]
partes = ["Assas","Cauda","Pinça","Ferrão"]
comportamentos = [
    "agressivo", "calculista", "curioso", "sádico", "leal",
    "covarde", "vingativo", "impulsivo", "estrategista", "calmo"
]

class Monstros(Animal):
    def __init__(self,x,y):
      
        self.nome = self.gerarNome()
        self.textura = random.choice(texturas)
        self.forma = random.choice(formas)
        self.pele_extra = random.choice(pele_extra)
        self.tracos = random.sample(comportamentos, 2)
        self.poderes = random.sample(poderes, 1)
        
        self.corpo = Corpo()
        self.corpo.CriarCorpo() 
        
        idade = random.randint(10,100)
        vida =   self.corpo.vida + self.corpo.Material.durabilidade + random.randint(100,150)
        
        self.tipo_corpo = random.choice(tipo_corpo)
        nome = self.gerarNome()
        dano = random.randint(10,20)
        self.cor = random.choice(cores)

        super().__init__(f"{Fore.LIGHTRED_EX}N{Style.RESET_ALL}",vida,1000,dano,1000,idade,nome,100,x,y)
  
  
    def gerarNome(self):
        primeiro_nome = random.choice(nomes)
        adjetivo = random.choice(adjetivos)
        return f"{primeiro_nome}, {adjetivo}"

    def movimentar(self, humano, mapa):
        alvo = self.encontrar_mais_proximo(humano, mapa, self.simbolo)
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
              humano.Dentro_estrutura = False
              self.n_pessoas +=1

    def encontrar_mais_proximo(self, humano, mapa, simbolos):
        menor_dist = float("inf")
        alvo = None
        for i in range(len(mapa)):
            for j in range(len(mapa[0])):
                if mapa[i][j] in simbolos:
                    dist = abs(humano.x - i) + abs(humano.y - j)
                    if dist < menor_dist:
                        menor_dist = dist
                        alvo = (i, j)
        return alvo
    
    def Atacar(self, alvo):
        chance_base = 0.5
        fator_velocidade = 0.02
        diferenca_vel = self.velocidade - alvo.velocidade
        chance_acerto = min(0.95, max(0.05, chance_base + diferenca_vel * fator_velocidade))
        chance_especial = min(0.95, max(0.05, chance_base + diferenca_vel * fator_velocidade))

        if random.random() < chance_acerto:
            if random.random() < chance_especial:
                self.poderes[0]["Metodo"](self,alvo)
            alvo.vida -= self.dano
            print(f"{self.nome} acertou o ataque! {alvo.nome} perdeu {self.dano} de vida.")
        else:
            print(f"{self.nome} errou o ataque em {alvo.nome}.")
    
    def Descricao(self):
        return (
            f"{self.nome}, um ser {self.tipo_corpo} de forma {self.forma}.\n"
            f"Sua pele é {self.textura} e {self.pele_extra}.\n"
            f"Material: {self.corpo.Material.nome}, cor: {self.cor}.\n"
            f"Possui {self.corpo.n_pernas} pernas, {self.corpo.n_bracos} braços,\n"
            f"{self.corpo.n_cabecas} cabeça(s) com {self.corpo.n_olhos} olhos,\n"
            f"{self.corpo.n_assas} asas e {self.corpo.n_caudas} caudas.\n"
            f"Comportamentos: {', '.join(self.tracos)}.\n"
            f"Poder especial: {self.poderes[0]['Nome']}.\n"
            f"Vida total: {self.vida}.\n"
        )


def regeneracao(usuario=None, alvo=None):
    cura = random.randint(5, 10)
    usuario.vida += cura
    print(f"{usuario.nome} regenerou seu corpo!\n{usuario.nome} regenerou {cura} de vida.")

def cuspe_acido(usuario=None, alvo=None):
    dano = random.randint(2, 5)
    alvo.vida -= dano
    print(f"{usuario.nome} vomitou ácido sobre {alvo.nome}!\n{alvo.nome} perdeu {dano} de vida.")

poderes = [
    {"Nome": "cuspe ácido", "Metodo": cuspe_acido},
    {"Nome": "regeneração", "Metodo": regeneracao}
]
