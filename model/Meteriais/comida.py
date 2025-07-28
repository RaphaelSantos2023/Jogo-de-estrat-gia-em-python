from model.Meteriais.material import Material
from colorama import Fore, Style, init

class Comida(Material):
  def __init__(self,nome,simbolo,fome):
      super().__init__(nome,"comestivel",simbolo,10,10)
      self.fome = fome
      self.comestivel = True

# ---- >Comidas
class Trigo(Comida):
    def __init__(self):
        super().__init__("Trigo", "y", 5)  # trigo dá pouca fome

class Maca(Comida):
    def __init__(self):
        super().__init__("Maçã", "ª", 15)  # maçã médio

class Pescado(Comida):
    def __init__(self):
        super().__init__("Peixe", f"{Fore.CYAN}={Style.RESET_ALL}", 25)  # peixe razoável

class Banana(Comida):
    def __init__(self):
        super().__init__("Banana", "b", 12)  # banana mais próxima da maçã

class Laranja(Comida):
    def __init__(self):
        super().__init__("Laranja", "o", 14)  # fruta cítrica, média saciedade

class Uva(Comida):
    def __init__(self):
        super().__init__("Uva", "u", 8)  # fruta pequena, saciedade leve

class Morango(Comida):
    def __init__(self):
        super().__init__("Morango", "m", 6)  # fruta leve e doce

class Tomate(Comida):
    def __init__(self):
        super().__init__("Tomate", "t", 5)  # fruto vegetal, saciedade leve

class Cenoura(Comida):
    def __init__(self):
        super().__init__("Cenoura", "c", 9)  # vegetal raiz, saciedade média

class Alface(Comida):
    def __init__(self):
        super().__init__("Alface", "l", 4)  # folha leve, pouca saciedade

class Batata(Comida):
    def __init__(self):
        super().__init__("Batata", "b", 20)  # vegetal raiz, bastante saciedade

class Abobora(Comida):
    def __init__(self):
        super().__init__("Abóbora", "a", 15)  # vegetal, saciedade média

class Pepino(Comida):
    def __init__(self):
        super().__init__("Pepino", "p", 5)  # vegetal, saciedade leve

class Frutinha(Comida):
    def __init__(self):
        super().__init__("Frutinha", "f", 7)  # fruta leve

class Carne(Comida):
    def __init__(self):
        super().__init__("Carne", "C", 30)  # carne com boa saciedade

class Cogumelo(Comida):
    def __init__(self):
        super().__init__("Cogumelo", "W", 8)  # cogumelo leve

class Queijo(Comida):
    def __init__(self):
        super().__init__("Queijo", "q", 18)  # queijo médio-forte

class Pao(Comida):
    def __init__(self):
        super().__init__("Pão", "p", 10)  # pão básico

class FrangoAssado(Comida):
    def __init__(self):
        super().__init__("Frango Assado", "F", 40)  # comida pesada e muito saciante

class Beterraba(Comida):
    def __init__(self):
        super().__init__("Beterraba", "ß", 10)  # raiz adocicada, saciedade média

class Rabanete(Comida):
    def __init__(self):
        super().__init__("Rabanete", "R", 7)  # raiz picante, saciedade leve

class Mandioca(Comida):
    def __init__(self):
        super().__init__("Mandioca", "M", 22)  # raiz energética, boa saciedade

class Inhame(Comida):
    def __init__(self):
        super().__init__("Inhame", "I", 18)  # raiz densa, saciedade média

class Cebola(Comida):
    def __init__(self):
        super().__init__("Cebola", "e", 5)  # vegetal base, saciedade leve

class Abacaxi(Comida):
    def __init__(self):
        super().__init__("Abacaxi", "x", 13)  # fruta tropical, saciedade média

class Melancia(Comida):
    def __init__(self):
        super().__init__("Melancia", "w", 11)  # fruta refrescante, leve

class Manga(Comida):
    def __init__(self):
        super().__init__("Manga", "g", 16)  # fruta doce, saciedade média

class Pimentao(Comida):
    def __init__(self):
        super().__init__("Pimentão", "P", 6)  # vegetal, leve

class Espinafre(Comida):
    def __init__(self):
        super().__init__("Espinafre", "s", 5)  # folha nutritiva, saciedade leve

class Coco(Comida):
    def __init__(self):
        super().__init__("Coco", "k", 20)  # fruta gordurosa, alta saciedade

class Azeitona(Comida):
    def __init__(self):
        super().__init__("Azeitona", "z", 3)  # pequena, saciedade mínima

# ---- >Sementes
class Semente(Material):
    def __init__(self,nome):
        super().__init__(nome,"Semente","!",10,5)

class semente_maca(Semente):
    def __init__(self):
        super().__init__("Semente de Maçâ")

class semente_trigo(Semente):
    def __init__(self):
        super().__init__("Semente de Trigo")

class semente_laranja(Semente):
    def __init__(self):
        super().__init__("Semente de Laranja")

class semente_uva(Semente):
    def __init__(self):
        super().__init__("Semente de Uva")

class semente_morango(Semente):
    def __init__(self):
        super().__init__("Semente de Morango")

class semente_tomate(Semente):
    def __init__(self):
        super().__init__("Semente de Tomate")

class semente_pepino(Semente):
    def __init__(self):
        super().__init__("Semente de Pepino")

class semente_abobora(Semente):
    def __init__(self):
        super().__init__("Semente de Abóbora")

class semente_batata(Semente):
    def __init__(self):
        super().__init__("Semente de Batata")

class semente_alface(Semente):
    def __init__(self):
        super().__init__("Semente de Alface")

class semente_cenoura(Semente):
    def __init__(self):
        super().__init__("Semente de Cenoura")

class semente_beterraba(Semente):
    def __init__(self):
        super().__init__("Semente de Beterraba")

class semente_rabanete(Semente):
    def __init__(self):
        super().__init__("Semente de Rabanete")

class semente_mandioca(Semente):
    def __init__(self):
        super().__init__("Semente de Mandioca")

class semente_inhame(Semente):
    def __init__(self):
        super().__init__("Semente de Inhame")

class semente_cebola(Semente):
    def __init__(self):
        super().__init__("Semente de Cebola")

class semente_abacaxi(Semente):
    def __init__(self):
        super().__init__("Semente de Abacaxi")

class semente_melancia(Semente):
    def __init__(self):
        super().__init__("Semente de Melancia")

class semente_manga(Semente):
    def __init__(self):
        super().__init__("Semente de Manga")

class semente_pimentao(Semente):
    def __init__(self):
        super().__init__("Semente de Pimentão")

class semente_espinafre(Semente):
    def __init__(self):
        super().__init__("Semente de Espinafre")

class semente_coco(Semente):
    def __init__(self):
        super().__init__("Semente de Coco")

class semente_azeitona(Semente):
    def __init__(self):
        super().__init__("Semente de Azeitona")

# ---->Cultivo

class cultivo:
    def __init__(self,nome,semente,fruta,dias_para_colheita):
        self.nome = nome
        self.semente = semente
        self.resultado = fruta
        self.dias_para_colheita =dias_para_colheita

class cultivo_maca(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Maçã", semente_maca(), Maca(), dias_para_colheita=8)

class cultivo_trigo(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Trigo", semente_trigo(), Trigo(), dias_para_colheita=9)

class cultivo_laranja(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Laranja", semente_laranja(), Laranja(), dias_para_colheita=10)

class cultivo_uva(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Uva", semente_uva(), Uva(), dias_para_colheita=8)

class cultivo_morango(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Morango", semente_morango(), Morango(), dias_para_colheita=6)

class cultivo_tomate(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Tomate", semente_tomate(), Tomate(), dias_para_colheita=5)

class cultivo_cenoura(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Cenoura", semente_cenoura(), Cenoura(), dias_para_colheita=7)

class cultivo_alface(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Alface", semente_alface(), Alface(), dias_para_colheita=4)

class cultivo_batata(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Batata", semente_batata(), Batata(), dias_para_colheita=9)

class cultivo_abobora(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Abóbora", semente_abobora(), Abobora(), dias_para_colheita=10)

class cultivo_pepino(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Pepino", semente_pepino(), Pepino(), dias_para_colheita=5)

class cultivo_beterraba(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Beterraba", semente_beterraba(), Beterraba(), dias_para_colheita=7)

class cultivo_rabanete(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Rabanete", semente_rabanete(), Rabanete(), dias_para_colheita=5)

class cultivo_mandioca(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Mandioca", semente_mandioca(), Mandioca(), dias_para_colheita=11)

class cultivo_inhame(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Inhame", semente_inhame(), Inhame(), dias_para_colheita=9)

class cultivo_cebola(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Cebola", semente_cebola(), Cebola(), dias_para_colheita=5)

class cultivo_abacaxi(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Abacaxi", semente_abacaxi(), Abacaxi(), dias_para_colheita=12)

class cultivo_melancia(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Melancia", semente_melancia(), Melancia(), dias_para_colheita=11)

class cultivo_manga(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Manga", semente_manga(), Manga(), dias_para_colheita=10)

class cultivo_pimentao(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Pimentão", semente_pimentao(), Pimentao(), dias_para_colheita=6)

class cultivo_espinafre(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Espinafre", semente_espinafre(), Espinafre(), dias_para_colheita=4)

class cultivo_coco(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Coco", semente_coco(), Coco(), dias_para_colheita=13)

class cultivo_azeitona(cultivo):
    def __init__(self):
        super().__init__("Cultivo de Azeitona", semente_azeitona(), Azeitona(), dias_para_colheita=8)
