from .User import User
from Model import MedidasCorporais

class Client(User):

    def __init__(self, nome, cpf, email, senha, tipo, peso = -1, altura = -1):
        super().__init__(nome, cpf, email, senha, tipo)
        self.peso = peso
        self.altura = altura
        self.listaExercicios = []
        self.listaExerciciosName = []
        self.MedidasCorporais = MedidasCorporais.MedidasCorporais()


    @classmethod
    def registerClient(self, nome, cpf, email, senha, tipo):
        return Client(nome, cpf, email, senha, tipo)
    
    def listarExercicios(self):
        aux = ''
        for elemento in self.listaExerciciosName:
            aux += f"{elemento}\n"
        return aux
    