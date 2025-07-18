import random
from model.Meteriais.material import Madeira, Pedra, Musculo, Ferro
class Membros:
  def __init__(self,nome,vida):
    self.nome = nome
    self.item = None
    self.vida = vida
    self.membros = []

  def addMembros(self,membro):
    self.membros.append(membro)
  
class Braco(Membros):
  def __init__(self):
    super().__init__("Braço",5)

class Perna(Membros):
  def __init__(self):
    super().__init__("Perna",5)

class Cauda(Membros):
  def __init__(self):
    super().__init__("Cauda",5)

class Cabeca(Membros):
  def __init__(self):
    super().__init__("Cabeça",5)

class Olho(Membros):
  def __init__(self):
    super().__init__("Olho",1)

class Asa(Membros):
  def __init__(self):
    super().__init__("Asa",2)

class Maos(Membros):
  def __init__(self):
    super().__init__("Mão",2)

class Pes(Membros):
  def __init__(self):
    super().__init__("Pé",2)

class Dedo(Membros):
  def __init__(self):
    super().__init__("Dedo",1)

class Garra(Membros):
  def __init__(self):
    super().__init__("Garra",1)


tipo_corpo = ["Humanoide", "Aracnídeo", "Reptiliano", "Aquática","Insectoide","Gosma","Fungoide"]
texturas = ["escamosa", "lisa", "viscosa", "espinhosa", "peluda"]
formas = ["esquelética", "musculosa", "obesa", "alongada", "compacta"]
pele_extra = ["com verrugas", "luminescente", "coberta por limo", "com veias pulsantes", "com runas entalhadas"]

class Corpo:
  def __init__(self):

    self.vida = random.randint(10,20)
    
    self.n_pernas = 0
    self.n_bracos = 0
    self.n_cabecas = 0
    self.n_olhos = 0
    self.n_assas = 0
    self.n_caudas =  0
    
    self.Material = None
    self.n_dedos = random.randint(1, 5)
    self.membros_torax = []
    self.membros_abdomen = []

  def criar_bracos(self):
    
    n_bracos = random.randint(1, 3) *2
    n_assas = random.randint(0,2) * 2
    
    for i in range(n_bracos):
        braco = Braco()
        Mao = Maos()
        for w in range(self.n_dedos):
            dedo = Dedo()
            Mao.addMembros(dedo)
        
        braco.addMembros(Mao)
        self.membros_torax.append(braco)

    if n_assas != 0:
      for j in range(n_assas):
        asa = Asa()
        self.membros_torax.append(asa)

    self.n_bracos = n_bracos
    self.n_assas = n_assas
    
    self.vida += (Dedo().vida*self.n_dedos) + (Braco().vida * n_bracos) + (Maos().vida * n_bracos)
  
  def criar_partes_inferiores(self):
    n_pernas = random.randint(0, 3) *2
    n_caudas = random.randint(0,2)

    if n_pernas != 0:
      for i in range(n_pernas):
          perna = Perna()
          Pe = Pes()
          for w in range(self.n_dedos):
            Pe.addMembros(Dedo())
          perna.addMembros(Pe)
          self.membros_abdomen.append(perna)
      
    if n_caudas != 0:
      for j in range(n_caudas):
        cauda = Cauda()
        self.membros_abdomen.append(cauda)

    self.n_pernas = n_pernas
    self.n_caudas = n_caudas
    
    self.vida += (Dedo().vida * self.n_dedos) + (Perna().vida * n_pernas) + (Pes().vida*n_pernas)

  def criar_cabeca(self):
    n_cabecas = random.randint(1,3)
    n_olhos = random.randint(1, 2)
    for i in range(n_cabecas):
      cabeca = Cabeca()
      for i in range(n_olhos):
        cabeca.addMembros(Olho())

    self.n_cabecas = n_cabecas
    self.n_olhos = n_olhos

    self.vida += (Cabeca().vida * n_cabecas) + (Olho().vida * n_olhos)
  
  def escolher_Material(self):
    self.Material = random.choice([Madeira(),Pedra(),Musculo(), Ferro()])
  
  def CriarCorpo(self):
    self.escolher_Material()
    self.criar_cabeca()
    self.criar_bracos()
    self.criar_partes_inferiores()
    
    
  
