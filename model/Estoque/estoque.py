class Estoque:
    def __init__(self,objeto,quantidade):
        self.nome = objeto
        self.quantidade = quantidade

class Estoque_semente(Estoque):
    def __init__(self, objeto, quantidade,semente):
        super().__init__(objeto, quantidade)
        self.semente = semente

class Membro_espedicao:
    def __init__(self,pessoa,posicao):
        self.pessoa = pessoa
        self.posicao = posicao

class Dado_espedicao:
    def __init__(self,grupo,local,tempo,Dia_inicio,Ano_inicio,Data):
        self.grupo = grupo
        self.local = local
        self.tempo = tempo
        self.Dia_inicio = Dia_inicio
        self.Ano_inicio = Ano_inicio
        self.Data = Data
    
    def Descricao(self):
        print(f"local {self.local} - tempo {self.tempo} - Dia_inicio {self.Dia_inicio} - Ano_inicio {self.Ano_inicio} - Data {self.Data}")