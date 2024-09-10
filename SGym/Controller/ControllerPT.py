import sys
import os
from Model.PersonalTrainer import PersonalTrainer
from Model import Client
from Persistence import PTDao
from Controller.ControllerDecorator import ControllerDecorator
currentdir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(currentdir)
sys.path.append(parent_dir)
caminho_arquivo = os.path.join(parent_dir, 'Persistence', 'dados_pt.txt')
caminho_listaExercicios = os.path.join(parent_dir, 'Persistence', 'listaExercicios.txt')
caminho_listaClientesPT = os.path.join(parent_dir, 'Persistence', 'listaClientesPT.txt')

class ControllerPT(ControllerDecorator):
    def __init__(self, listaPT = []):
        self.listaPT = listaPT
        self.persistenciaPT = PTDao.persistenciaPT.instancias()

    def registerPT(nome, cpf, email, senha, tipo, especialidade): # TODO
        personalTrainer = PersonalTrainer(nome, cpf, email, senha, tipo, especialidade)
        return personalTrainer
    
    def buscar_personal_por_cpf(self, cpf): # TODO
        with open(caminho_arquivo, 'r') as arquivo:
            for linha in arquivo:
                nome, cpf_personal, email, senha, tipo, especialidade = linha.strip().split(',')
                if cpf_personal == cpf:
                    return PersonalTrainer.PersonalTrainer(nome, int(cpf), email, senha, int(tipo), especialidade)
        return None
    
    def escrever_exercicios_em_arquivo(self, cliente): # escreve os exercicios que pt adicionou na interface no arquivo
        # Escrever os exercícios do cliente em um arquivo de texto
        with open(f"{cliente.nome}_exercicios.txt", "w") as arquivo:
            for exercicio in cliente.listaExercicios:
                arquivo.write(exercicio + '\n')

    def adicionar_exercicio(self, cliente, exercicio): # adiciona exercicios a lista de exercicios
        cliente.listaExercicios.append(exercicio)
        self.escrever_exercicios_em_arquivo(cliente)

    def cadastraAlunoPT(self, Personal, nome, cpf, email, senha, peso, altura, tipo): # cadastra aluno de pt
        Personal.cadastrarAlunoPT(Client.Client(nome, cpf, email, senha, tipo, peso, altura))

    def checarAlunoPT(self, cpf, personal:PersonalTrainer): # checa aluno de pt por cpf 
        for alunos in personal.listaAlunos:
            if alunos.cpf == cpf:
                personal.CheckAluno()
    
    def apagarAlunoPT(self, email, personal:PersonalTrainer): # apaga aluno de pt por email
        for aluno in personal.listaAlunos:
            if aluno.email == email:
                personal.listaAlunos.remove(aluno)
                self.persistenciaPT.deleteUserByEmail(email)

    def exibirListaDeExercicios(self, cpf): # exibe lista de exercicios na interface 
        listaExercicios = []
        cpf_atual = -1
        with open(caminho_listaExercicios, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith("CPF:"):
                    cpf_atual = cpf
                if cpf_atual == cpf:
                    listaExercicios.append(line)
        return listaExercicios
    
    def modificarListaDeExercicios(self, listaExercicios, cpf): # modifica lista de exercicios na interface
        lines = []
        listaExerciciosAntiga = []
        with open(caminho_listaExercicios, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith("CPF:") and line.split(":")[1].strip() != cpf:
                    cpf_atual = line.split(":")[1].strip()
                    lines.append(lines)
                elif cpf_atual == cpf:
                    listaExerciciosAntiga.append(line)
                else:
                    lines.append(line)
        if listaExercicios > 0: # pra remover 
            lines.append(cpf)
            for elementos in listaExercicios:
                lines.append(f"{elementos}\n")
            with open(caminho_listaExercicios, 'w') as file:
                for line in lines:
                    file.write(line)
    
    def leituraArquivoPT(self, nome, cpf, email, senha, tipo, especialidade): # leitura de arquivo do pt
        pt = PersonalTrainer(nome, cpf, email, senha, tipo, especialidade)
        self.listaPT.append(pt)

    def loadClientesPT(self, listaClient): # carrega dados da lista de personal trainer que contem seus clientes
        personal_trainer = None
        with open(caminho_listaClientesPT, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith("CPF_PT"):
                    cpf_pt = int(line.split(": ")[1])
                    personal_trainer = None
                    for personal in self.listaPT:
                        if personal.cpf == cpf_pt:
                            personal_trainer = personal
                            break
                elif line.startswith("CPF") and personal_trainer:
                    cpf_client = int(line.split(": ")[1])
                    client = None
                    for client in listaClient:
                        if client.cpf == cpf_client:
                            break
                    if client is not None:
                        personal_trainer.cadastrarAlunoPT(client)
         
    def listarClientesPT(self, personal): # retorna a lista de clientes do personal trainer pra exibir
        return personal.listaAlunos

    def save_exercises(self): # salva os exercicios dos clientes de pt
        self.persistenciaPT.save_exercises(self.listaPT)

    def registrarAlunos(self, cpf, listaClientes, personal): # registra alunos do pt
        for clientes in listaClientes:
            if cpf == clientes.cpf:
                personal.cadastrarAlunoPT(clientes)
                self.persistenciaPT.registrarAluno(cpf, personal.cpf)
                return True
        return False