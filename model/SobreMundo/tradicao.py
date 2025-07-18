import random

origem = [
    "Pré-histórica, passada oralmente por gerações",
    "Fundada após um cataclismo natural devastador",
    "Desenvolvida em tribos nômades das montanhas",
    "Criada por antigos sábios durante uma era dourada",
    "Surgida a partir da fusão de culturas rivais",
    "Inspirada por visões místicas de um líder profeta",
    "Formada em torno de um evento celestial raro",
    "Originada nos templos subterrâneos esquecidos",
    "Nascida dos ensinamentos de um ser divino exilado",
    "Transmitida pelos primeiros habitantes de uma ilha isolada",
    "Evoluída através de rituais secretos em florestas sagradas",
    "Estabelecida por uma ordem guerreira após uma grande guerra",
    "Fundada por sobreviventes de uma praga devastadora",
    "Desenvolvida a partir do culto aos ancestrais",
    "Surgida em meio a uma revolução social e espiritual",
    "Criada para proteger segredos proibidos do conhecimento",
    "Baseada nas constelações e movimentos dos astros",
    "Originada em cavernas onde a luz do sol nunca penetra",
    "Transcendida dos sonhos compartilhados por uma comunidade",
    "Formada por discípulos que seguiram um mestre desaparecido"
]

cores = [
  "vermelho",
  "azul",
  "verde",
  "amarelo",
  "laranja",
  "roxo",
  "rosa",
  "preto",
  "branco",
  "cinza"
]

descricoes = [
    "estrela",
    "triângulo para cima",
    "círculo",
    "quadrado",
    "losango",
    "trébol",
    "coração",
    "sol",
    "guarda-chuva",
    "cruz",
    "espada",
    "escudo",
    "coroa",
    "âncora",
    "crânio"
    "infinito"
]

relacoes_com_deuses = [
    "Deuses como seres imperfeitos",
    "Deuses como criadores supremos",
    "Deuses como guardiões protetores",
    "Deuses como figuras de punição",
    "Deuses como guias espirituais",
    "Deuses como manifestações da natureza",
    "Deuses como símbolos de moralidade",
    "Deuses como entidades distantes e inalcançáveis",
    "Deuses como parte da alma humana",
    "Deuses como seres mutáveis e falíveis",
    "Deuses como forças cósmicas impessoais",
    "Deuses como figuras de inspiração e esperança",
    "Deuses como entidades vingativas",
    "Deuses como seres benevolentes e compassivos",
    "Deuses como forças da destruição e renovação"
]

ritos = [
    "Ritual da Chuva", "Dança das Fogueiras", "Cerimônia do Renascimento",
    "Festival das Estrelas", "Jejum Sagrado", "Oferenda à Terra",
    "Marcha dos Ancestrais", "Rito de Passagem", "Noite dos Espíritos"
]

mitos = [
    "O Dragão Guardião dos Segredos", "A Mãe Terra e o Filho Céu",
    "A Lenda do Primeiro Rei Imortal", "Os Gigantes Adormecidos",
    "A Semente que Germinou o Mundo", "A Serpente que Une os Mundos"
]

objetos_sagrados = [
    "Amuleto de Jade", "Cetro da Lua", "Máscara dos Antepassados",
    "Pedra do Destino", "Livro das Sombras", "Espada da Verdade"
]

valores_culturais = [
    "Honra acima da vida", "Harmonia com a natureza", "Coragem e Sacrifício",
    "Sabedoria ancestral", "Respeito aos mortos", "Busca pelo conhecimento"
]

influencias_geograficas = [
    "Montanhas geladas", "Florestas tropicais", "Desertos vastos",
    "Ilhas isoladas", "Planícies ventosas", "Cidades subterrâneas"
]

class Tradicao:
    def __init__(self):
        self.origem = ""
        self.simbolos = ""
        self.relacao_com_deuses = ""
        self.rito = ""
        self.objeto_sagrado = ""

        self.simboloInterior = ""
        self.simboloExterno = ""

        self.valor_cultural = ""
        self.influencia_geografica = ""
        self.formarTradicao()

    def Descricao(self):
        return (
            f"Origem: {self.origem}\n"
            f"Símbolos: {self.simbolos}\n"
            f"Relação com os deuses: {self.relacao_com_deuses}\n"
            f"Rito principal: {self.rito}\n"
            f"Objeto sagrado: {self.objeto_sagrado}\n"
            f"Valor cultural: {self.valor_cultural}\n"
            f"Influência geográfica: {self.influencia_geografica}"
        )
  
    def criarSimsolo(self):
        exterior_forma = random.choice(descricoes)
        cor_exterior = random.choice(cores)
        exterior = exterior_forma + " " + cor_exterior
        
        interior_forma = random.choice(descricoes)
        cor_interior = random.choice(cores)
        interior = interior_forma + " " + cor_interior
        
        self.simboloInterior = interior
        self.simboloExterno = exterior

        self.simbolos = interior + " dentro de " + exterior

    def criarOrigem(self):
        self.origem = random.choice(origem)

    def criarRelacaoComDeuses(self):
        self.relacao_com_deuses = random.choice(relacoes_com_deuses)
        
    def criarRito(self):
        self.rito = random.choice(ritos)
        
    def criarObjetoSagrado(self):
        self.objeto_sagrado = random.choice(objetos_sagrados)
        
    def criarValorCultural(self):
        self.valor_cultural = random.choice(valores_culturais)
        
    def criarInfluenciaGeografica(self):
        self.influencia_geografica = random.choice(influencias_geograficas)

    def formarTradicao(self):
        self.criarOrigem()
        self.criarSimsolo()
        self.criarRelacaoComDeuses()
        self.criarRito()
        self.criarObjetoSagrado()
        self.criarValorCultural()
        self.criarInfluenciaGeografica()



        