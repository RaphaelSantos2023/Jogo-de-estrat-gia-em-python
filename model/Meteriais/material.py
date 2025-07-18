class Material:
  def __init__(self,nome,tipo,simbolo,durabilidade):
      self.nome = nome
      self.tipo = tipo
      self.simbolo = simbolo
      self.durabilidade = durabilidade

class Madeira(Material):
  def __init__(self):
      super().__init__("Madeira","Construcao","/",10)

class Terra(Material):
  def __init__(self):
      super().__init__("Terra","Construcao",".",10)

class Pedra(Material):
  def __init__(self):
      super().__init__("Pedra","Construcao","#",20)

class Musculo(Material):
  def __init__(self):
      super().__init__("Musculo","Construcao","||",5)

class Ferro(Material):
  def __init__(self):
      super().__init__("Ferro","Materia Prima","",25)

class Cobre(Material):
  def __init__(self):
      super().__init__("Cobre", "Materia Prima", "c", 15)

class Estanho(Material):
  def __init__(self):
      super().__init__("Estanho", "Materia Prima", "h", 12)

class Prata(Material):
  def __init__(self):
      super().__init__("Prata", "Materia Prima", "a", 18)

class Ouro(Material):
  def __init__(self):
      super().__init__("Ouro", "Materia Prima", "r", 10)

class Platina(Material):
  def __init__(self):
      super().__init__("Platina", "Materia Prima", "â", 22)

class Níquel(Material):
  def __init__(self):
      super().__init__("Níquel", "Materia Prima", "n", 20)

class Titânio(Material):
  def __init__(self):
      super().__init__("Titânio", "Materia Prima", "î", 30)

