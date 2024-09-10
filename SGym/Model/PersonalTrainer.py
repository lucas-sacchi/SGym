from Model.User import *

class PersonalTrainer(User):

    def __init__(self, nome, cpf, email, senha, tipo, especialidade):
        super().__init__(nome, cpf, email, senha, tipo)
        self.especializacao = especialidade
        self.listaAlunos = []
        
    @classmethod
    def registerPT(self, nome, cpf, email, senha, tipo, especialidade):
        return PersonalTrainer(nome, cpf, email, senha, tipo, especialidade)
    
    def checkAluno(self, aluno):
        print(f"Aluno: {aluno.nome}, CPF: {aluno.cpf}, Peso: {aluno.peso}, Altura: {aluno.altura}\n")

    def cadastrarAlunoPT(self, aluno):
        self.listaAlunos.append(aluno)



