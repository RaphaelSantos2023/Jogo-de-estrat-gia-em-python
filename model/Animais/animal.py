import random
from model.Animais.sexualidade import Heterossexual, Homosexual, Bisexual, Asexual
import random


class Animal:
    def __init__(self, simbolo, vida, fome, dano, felicidade, idade, nome,comida_quantidade, x, y):
        self.simbolo = simbolo
        self.Dentro_estrutura = False
        self.emocoes = "Neutro"
        self.genero = self.selecionarGenero()
        self.sexualidade = self.selecionarSexualidade()
        self.vida = vida
        self.vidaMax = vida
        self.fome = fome
        self.fomeMax = fome
        self.dano = dano
        self.felicidade = felicidade
        self.idade = idade
        self.nome = nome
        self.inventario = []
        self.comida_quantidade = comida_quantidade
        self.x = x
        self.y = y
        self.velocidade = random.randint(5,10)

        # Novos atributos de características
        self.forca = 0
        self.destreza = 0
        self.inteligencia = 0
        self.carisma = 0
        self.constituicao = 0

        self.randomizarAtributos()

    def Comer(self,comida):
        self.fome += comida.fome

    def selecionarGenero(self):
        generos = ["Masculino", "Feminino"]
        return random.choice(generos)

    def selecionarSexualidade(self):
        # Suponha que essas classes existem
        sexualidades = [Heterossexual(self), Homosexual(self), Bisexual(self), Asexual(self)]
        return random.choice(sexualidades)

    def randomizarAtributos(self):
        self.forca = random.randint(1, 5)
        self.destreza = random.randint(1, 5)
        self.inteligencia = random.randint(1, 5)
        self.carisma = random.randint(1, 5)
        self.constituicao = random.randint(1, 5)

    def Atacar(self, alvo):
        chance_critico = random.random()

        alvo.vida -= self.dano
        if chance_critico > 5.0:
            critico = (self.forca//3 + self.constituicao//3)
            alvo.vida -= critico


    def SetXY(self, x, y):
        self.x = x
        self.y = y

    def Descricao(self):
        return (f"Nome: {self.nome}\n|| Vida: {self.vida} || Idade: {self.idade} "
                f"\n|| Gênero: {self.genero} || Sexualidade: {type(self.sexualidade).__name__} || "
                f"\n|| Dano: {self.dano} \n||  Força: {self.forca} || Destreza: {self.destreza} || Inteligência: {self.inteligencia}"
                f"\n|| Carisma: {self.carisma} || Constituição: {self.constituicao}")
    
    def ShowStatus(self):
        print(
        f"\n• Força: {self.forca}",
        f"\n• Destreza: {self.destreza}",
        f"\n• Inteligencia: {self.inteligencia}",
        f"\n• Carisma: {self.carisma}",
        f"\n• Constituição: {self.constituicao}"
        )

class Animal_nao_sapiente(Animal):
    def __init__(self, simbolo, vida, dano, nome,comida_quantidade,Tempo_reproducao ,tipo):
        self.tipo = tipo
        self.Tempo_reproducao = Tempo_reproducao

        idade = random.randint(1, 10)
        super().__init__(simbolo, vida, 100, dano, 100, idade, nome,comida_quantidade, 0, 0)

class Animal_selvagem(Animal_nao_sapiente):
    def __init__(self, simbolo, vida, dano, nome, comida_quantidade, tempo_reproducao):
        super().__init__(simbolo, vida, dano, nome, comida_quantidade, tempo_reproducao, "Selvagem")

class Animal_domestico(Animal_nao_sapiente):
    def __init__(self, simbolo, vida, dano, nome, comida_quantidade, tempo_reproducao):
        super().__init__(simbolo, vida, dano, nome, comida_quantidade, tempo_reproducao, "Domestico")

# Classes individuais dos animais, categorizados como selvagens ou domésticos
# Domésticos
class Porco(Animal_domestico):
    def __init__(self):
        super().__init__("P", 50, 5, "Porco", 20, 140)  # 140 dias

class Galinha(Animal_domestico):
    def __init__(self):
        super().__init__("G", 30, 2, "Galinha", 10, 21)

class Cavalo(Animal_domestico):
    def __init__(self):
        super().__init__("C", 60, 8, "Cavalo", 30, 330)

class Gato(Animal_domestico):
    def __init__(self):
        super().__init__("g", 25, 4, "Gato", 8, 60)

class Cachorro(Animal_domestico):
    def __init__(self):
        super().__init__("c", 40, 6, "Cachorro", 10, 63)

# Selvagens
class Coelho(Animal_selvagem):
    def __init__(self):
        super().__init__("c", 20, 2, "Coelho", 5, 31)

class Urso(Animal_selvagem):
    def __init__(self):
        super().__init__("U", 100, 15, "Urso", 50, 220)

class Elefante(Animal_selvagem):
    def __init__(self):
        super().__init__("e", 120, 10, "Elefante", 60, 660)

class Veado(Animal_selvagem):
    def __init__(self):
        super().__init__("v", 60, 5, "Veado", 25, 200)  # Gestação: ~200 dias

class Raposa(Animal_selvagem):
    def __init__(self):
        super().__init__("r", 35, 6, "Raposa", 10, 52)  # Gestação: ~52 dias

class Coruja(Animal_selvagem):
    def __init__(self):
        super().__init__("O", 30, 4, "Coruja", 6, 30)   # Incubação: ~30 dias

class Cobra(Animal_selvagem):
    def __init__(self):
        super().__init__("s", 40, 10, "Cobra", 8, 60)   # Incubação (ovípara): ~60 dias

class Camelo(Animal_selvagem):
    def __init__(self):
        super().__init__("m", 70, 4, "Camelo", 35, 390) # Gestação: ~390 dias

class Jacare(Animal_selvagem):
    def __init__(self):
        super().__init__("j", 80, 12, "Jacare", 45, 65)  # Incubação dos ovos: ~65 dias

class Sapo(Animal_selvagem):
    def __init__(self):
        super().__init__("S", 25, 3, "Sapo", 4, 10)      # Desenvolvimento dos girinos: ~10 dias

class Tartaruga(Animal_selvagem):
    def __init__(self):
        super().__init__("T", 60, 3, "Tartaruga", 15, 60) # Incubação dos ovos: ~60 dias

class Lobo(Animal_selvagem):
    def __init__(self):
        super().__init__("L", 70, 10, "Lobo", 30, 63)     # Gestação: ~63 dias

class Cabra(Animal_selvagem):
    def __init__(self):
        super().__init__("b", 50, 4, "Cabra", 18, 150)    # Gestação: ~150 dias

class Tigre(Animal_selvagem):
    def __init__(self):
        super().__init__("t", 90, 14, "Tigre", 40, 105)   # Gestação: ~105 dias

class Leao(Animal_selvagem):
    def __init__(self):
        super().__init__("l", 95, 13, "Leão", 42, 110)  # Gestação: ~110 dias

class Anta(Animal_selvagem):
    def __init__(self):
        super().__init__("a", 60, 5, "Anta", 20, 395)   # Gestação: ~395 dias

class CavaloMarinho(Animal_selvagem):
    def __init__(self):
        super().__init__("M", 20, 2, "CavaloMarinho", 3, 20)  # Incubação (macho): ~20 dias

class Ganso(Animal_selvagem):
    def __init__(self):
        super().__init__("n", 30, 3, "Ganso", 7, 28)    # Incubação dos ovos: ~28 dias

class Pato(Animal_selvagem):
    def __init__(self):
        super().__init__("p", 30, 3, "Pato", 6, 28)     # Incubação dos ovos: ~28 dias

class Rato(Animal_selvagem):
    def __init__(self):
        super().__init__("R", 20, 2, "Rato", 3, 21)     # Gestação: ~21 dias

class Morcego(Animal_selvagem):
    def __init__(self):
        super().__init__("M", 25, 4, "Morcego", 5, 120) # Gestação: ~120 dias

class Ovelha(Animal_domestico):
    def __init__(self):
        super().__init__("o", 45, 4, "Ovelha", 18, 150)  # Gestação: ~150 dias

class Gado(Animal_domestico):
    def __init__(self):
        super().__init__("g", 45, 4, "Gado", 18, 283)    # Gestação: ~283 dias (vaca)

class Pavao(Animal_domestico):
    def __init__(self):
        super().__init__("v", 35, 2, "Pavão", 10, 29)    # Incubação dos ovos: ~29 dias

class GansoDomestico(Animal_domestico):
    def __init__(self):
        super().__init__("n", 30, 3, "Ganso Doméstico", 8, 28)  # Incubação: ~28 dias

class Lhama(Animal_domestico):
    def __init__(self):
        super().__init__("L", 55, 5, "Lhama", 22, 350)   # Gestação: ~350 dias

class Peru(Animal_domestico):
    def __init__(self):
        super().__init__("P", 40, 3, "Peru", 12, 28)     # Incubação: ~28 dias

class Burro(Animal_domestico):
    def __init__(self):
        super().__init__("B", 65, 7, "Burro", 28, 365)  # Gestação: ~365 dias

class Javali(Animal_selvagem):
    def __init__(self):
        super().__init__("J", 70, 8, "Javali", 30, 115)  # Gestação: ~115 dias

class Onca(Animal_selvagem):
    def __init__(self):
        super().__init__("O", 85, 12, "Onça", 38, 100)   # Gestação: ~100 dias

class Tamandua(Animal_selvagem):
    def __init__(self):
        super().__init__("T", 45, 3, "Tamanduá", 15, 180)  # Gestação: ~180 dias

class BichoPreguica(Animal_selvagem):
    def __init__(self):
        super().__init__("Z", 50, 2, "Bicho-Preguiça", 12, 180)  # Gestação: ~180 dias

class Cervo(Animal_selvagem):
    def __init__(self):
        super().__init__("C", 55, 5, "Cervo", 20, 230)  # Gestação: ~230 dias

class Falcao(Animal_selvagem):
    def __init__(self):
        super().__init__("F", 35, 6, "Falcão", 9,20)

