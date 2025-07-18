from model.Meteriais.material import Pedra
from colorama import Fore, Style, init

class Cenario:
  def __init__(self, nome, simbolo, Material, Quantidade, x, y):
      self.nome = nome
      self.simbolo = simbolo
      self.Material = Material
      self.Quantidade = Quantidade
      self.x = x
      self.y = y

CINZA = "\033[90m"
RESET = "\033[0m"  

class Pedregulho(Cenario):
  def __init__(self, x, y):
      super().__init__("Pedregulho", f"{CINZA}P{RESET}", Pedra(), 10, x, y)