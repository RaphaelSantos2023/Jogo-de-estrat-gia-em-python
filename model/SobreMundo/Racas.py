from colorama import Fore, Style, init

class Raca:

    def __init__(self,nome,simbolo, vida, dano, altura, aparencia, forca, destreza, inteligencia, carisma,constituicao):
        self.nome = nome
        self.simbolo = simbolo
        self.vida = vida
        self.dano = dano
        self.altura = altura
        self.aparencia = aparencia
        self.forca = forca
        self.destreza = destreza
        self.inteligencia = inteligencia
        self.carisma = carisma
        self.constituicao = constituicao
        self.relacao_racas = []
        
    def MostrarRelacoes(self):
        txt = "\n\nRelações com outras especies:\n"
        for relacao in self.relacao_racas:

            if relacao['Afinidade'] >= 50:
                relacao_caso = f"{Fore.GREEN}Aliado"
            elif relacao['Afinidade'] >= 0:
                relacao_caso = f"{Fore.LIGHTCYAN_EX}Neutro"
            else:
                relacao_caso = f"{Fore.RED}Inimigo"

            txt += f"• {Fore.LIGHTCYAN_EX}{relacao['Nome'].nome}{Style.RESET_ALL}, Relacao: {relacao_caso}{Style.RESET_ALL}, Numero: {relacao['Afinidade']}\n"
        return txt

    def Descricao(self):
        txt = (
            f"\n🏹 Raça: {self.nome}\n"
            f"🔰 Símbolo: {self.simbolo}\n"
            f"📏 Altura média: {self.altura}\n"
            f"🎨 Aparência: {self.aparencia}\n"
            f"❤️ Vida Base: {self.vida} HP\n"
            f"🗡️ Dano Base: {self.dano}\n"
            f"📊 Atributos:\n"
            f"   • Força (STR): +{self.forca}\n"
            f"   • Destreza (DEX): +{self.destreza}\n"
            f"   • Inteligência (INT): +{self.inteligencia}\n"
            f"   • Carisma (CHA): +{self.carisma}\n"
            f"   • Constituição (CON): +{self.constituicao}\n"
            f"\nEsta raça é conhecida por sua aparência {self.aparencia} e altura {self.altura}"
        )

        txt += self.MostrarRelacoes()
        return txt
        
class Criatura:
    def __init__(self, vida, dano, altura, aparencia, forca, destreza, inteligencia, carisma, constituicao):
        self.nome = ""
        self.vida = vida
        self.dano = dano
        self.altura = altura
        self.aparencia = aparencia
        self.forca = forca
        self.destreza = destreza
        self.inteligencia = inteligencia
        self.carisma = carisma
        self.constituicao = constituicao

    def __str__(self):
        return f"{self.nome} - Vida: {self.vida}, Dano: {self.dano}"

