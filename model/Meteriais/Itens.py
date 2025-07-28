import random

class item:
    def __init__(self,nome,material,preco):
        self.nome = nome
        self.material = material
        self.preco = preco * material.qualidade
        self.durabilidade = self.material.durabilidade
        self.qualidade = material.qualidade

class Armas(item):
    def __init__(self,nome,material,preco): 
        super().__init__(nome,material,preco)

class espada(Armas):
    def __init__(self,material):
        super().__init__(f"Espada de {material.nome}",material,50)
        self.dano = 10 * material.qualidade    

class armadura(item):
    def __init__(self,material):
        super().__init__(f"Armadura de {material.nome}",material,50)
        self.vida = 20 * material.qualidade

class escudo(item):
    def __init__(self, material):
        super().__init__(f"Escudo de {material.nome}", material, 45)
        self.bloqueio = 15 * self.qualidade

class adorno(item):
    def __init__(self, material):
        nomes_adorno = ["Adorno","Colar","Anel","Brinco"]
        super().__init__(f"{random.choice(nomes_adorno)} de {material.nome}", material, 100)

class Qualidade_reino(item):
    def __init__(self, nome, material, preco, qualidade):
        super().__init__(nome, material, preco)
        self.qualidade_reino = qualidade

class Tapecaria(Qualidade_reino):
    def __init__(self, material):
        super().__init__(f"Tapeçaria de {material.nome}", material, 45,80)

class vasos(Qualidade_reino):
    def __init__(self,material):
        super().__init__(f"Vaso de {material.nome}",material,20,10)
        self.quantidade = 10 * material.qualidade



