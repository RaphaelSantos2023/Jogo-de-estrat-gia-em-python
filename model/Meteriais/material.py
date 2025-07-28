class Material:
  def __init__(self,nome,tipo,simbolo,durabilidade,qualidade):
      self.nome = nome
      self.tipo = tipo
      self.simbolo = simbolo
      self.durabilidade = durabilidade
      self.qualidade = qualidade

class Madeira(Material):
    def __init__(self):
        super().__init__("Madeira", "Construcao", "/", 10, 0.2)

class Terra(Material):
    def __init__(self):
        super().__init__("Terra", "Construcao", ".", 10, 0.1)

class Pedra(Material):
    def __init__(self):
        super().__init__("Pedra", "Construcao", "#", 20, 0.3)

class Musculo(Material):
    def __init__(self):
        super().__init__("Musculo", "Construcao", "||", 5, 0.4)

class Ferro(Material):
    def __init__(self):
        super().__init__("Ferro", "Materia Prima", "", 25, 0.5)

class Cobre(Material):
    def __init__(self):
        super().__init__("Cobre", "Materia Prima", "c", 15, 0.45)

class Estanho(Material):
    def __init__(self):
        super().__init__("Estanho", "Materia Prima", "h", 12, 0.4)

class Prata(Material):
    def __init__(self):
        super().__init__("Prata", "Materia Prima", "a", 18, 0.7)

class Ouro(Material):
    def __init__(self):
        super().__init__("Ouro", "Materia Prima", "r", 10, 0.9)

class Platina(Material):
    def __init__(self):
        super().__init__("Platina", "Materia Prima", "â", 22, 1.0)

class Níquel(Material):
    def __init__(self):
        super().__init__("Níquel", "Materia Prima", "n", 20, 0.55)

class Titânio(Material):
    def __init__(self):
        super().__init__("Titânio", "Materia Prima", "î", 30, 0.85)

class Areia(Material):
    def __init__(self):
        super().__init__("Areia", "Construcao", ":", 5, 0.1)

class Argila(Material):
    def __init__(self):
        super().__init__("Argila", "Construcao", "~", 8, 0.2)

class Gelo(Material):
    def __init__(self):
        super().__init__("Gelo", "Construcao", "*", 6, 0.15)

class Vidro(Material):
    def __init__(self):
        super().__init__("Vidro", "Construcao", "v", 12, 0.4)

class Bronze(Material):
    def __init__(self):
        super().__init__("Bronze", "Materia Prima", "b", 20, 0.6)

class Zinco(Material):
    def __init__(self):
        super().__init__("Zinco", "Materia Prima", "z", 14, 0.35)

class Chumbo(Material):
    def __init__(self):
        super().__init__("Chumbo", "Materia Prima", "x", 18, 0.3)

class Mercúrio(Material):
    def __init__(self):
        super().__init__("Mercúrio", "Materia Prima", "m", 10, 0.7)

class Obsidiana(Material):
    def __init__(self):
        super().__init__("Obsidiana", "Exotico", "O", 28, 0.85)

class Cristal(Material):
    def __init__(self):
        super().__init__("Cristal", "Exotico", "C", 15, 0.95)
