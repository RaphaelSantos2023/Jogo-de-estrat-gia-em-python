
class Sexualidade:
  def __init__(self,nome,preferencia,pessoa = None):
      self.nome = nome
      self.preferencia = preferencia
      self.pessoa = pessoa
  
  def relacao(self,pessoa):
    valor = False
    
    match self.preferencia:
      case "Oposto":
        if pessoa.genero != self.pessoa.genero:
          valor = True
      case "Mesmo":
        if pessoa.genero == self.pessoa.genero:
          valor = True
      case "Todos":
        valor = True
        
    return valor

class Heterossexual(Sexualidade):
  def __init__(self,pessoa):
      super().__init__("Heterossexual","Oposto",pessoa)

class Homosexual(Sexualidade):
  def __init__(self,pessoa):
      super().__init__("Homosexual","Mesmo",pessoa)

class Bisexual(Sexualidade):
  def __init__(self,pessoa):
      super().__init__("Bisexual","Todos",pessoa)

class Asexual(Sexualidade):
  def __init__(self,pessoa):
      super().__init__("Asexual","Nenhum",pessoa)

  