class Estoque:
    def __init__(self,objeto,quantidade):
        self.nome = objeto
        self.quantidade = quantidade

class Estoque_semente(Estoque):
    def __init__(self, objeto, quantidade,semente):
        super().__init__(objeto, quantidade)
        self.semente = semente