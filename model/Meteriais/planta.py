from model.Meteriais.comida import Maca, Frutinha
from model.Meteriais.material import Madeira
import random
from colorama import Fore, Style, init

class Planta:
    def __init__(self, nome, simbolo, Material, Quantidade, x, y):
        self.nome = nome
        self.simbolo = simbolo
        self.Material = Material
        self.Quantidade = random.randint(1,Quantidade)
        self.x = x
        self.y = y


class Arvore(Planta):
    def __init__(self, x, y):
        super().__init__("Arvore", f"{Fore.LIGHTGREEN_EX}T{Style.RESET_ALL}", Madeira(), 5, x, y)


class Macieira(Planta):
    def __init__(self, x, y):
        super().__init__("Macieira", f"{Fore.LIGHTGREEN_EX}T{Style.RESET_ALL}", [Madeira(), Maca()], 3, x, y)

class Arbusto(Planta):
    def __init__(self, x, y):
        super().__init__("Arbusto", f"{Fore.LIGHTGREEN_EX}m{Style.RESET_ALL}", [Frutinha()], 3, x, y)
