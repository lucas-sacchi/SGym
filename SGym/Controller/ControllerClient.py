import sys
import os
from tkinter import messagebox
currentdir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(currentdir)
sys.path.append(parent_dir) 
from Model import Client
from Persistence import ClientDAO
from Controller.ControllerDecorator import ControllerDecorator
caminho_arquivo = os.path.join(parent_dir, 'Persistence', 'dados_client.txt')

class ControllerClient(ControllerDecorator):
    def __init__(self, listaClient = []):
        self.listaClient = listaClient
        self.persistenciaClient = ClientDAO.persistenciaClient.instancias()

    # def verificaLogin(self, email, senha): # verifica o tipo do usuario pra entrar na respectiva interface
    #     tipo = -1
    #     for client in self.listaClient:
    #         if client.email == email and client.senha == senha:
    #             tipo = client.tipo
    #     return tipo
    
    # def getUserByEmail(self, email): # pega email do client e retorna client
    #     for client in self.listaClient:
    #         if client.email == email:
    #             return client
    #     return None  # Retorna None se o cliente não for encontrado
    
    # def loadData(self, ControladorCliente): # carrega dados no inicio
    #     self.persistenciaClient.leituraCadastro(ControladorCliente)
    #     for cliente in ControladorCliente.listaClient:
    #         self.persistenciaClient.escreverAval(cliente)
    
    # def saveData(self, ControladorCliente): # salva dados no final 
    #     self.persistenciaClient.persistenciaCadastro(ControladorCliente)

    def registerUser(self, nome, cpf, email, senha, senha1, tipo, peso, altura): # registra cliente na interface de registro inicial 
        aux = 1
        if senha1 == senha:
            for elemento in self.listaClient:
                if email == elemento.email or int(cpf) == elemento.cpf:
                    aux = 0
            if aux:
                if peso == None:
                    cliente = Client.Client(nome, cpf, email, senha, tipo)
                    self.listaClient.append(cliente)
                else:
                    cliente = Client.Client(nome, cpf, email, senha, tipo, peso, altura) 
                    self.listaClient.append(cliente)
                self.persistenciaClient.escritaUser(cliente)
                return "Registrado"
            else:
                return "Nao foi possivel registrar"
        else:
            return "Senhas distintas"

    def calcular_imc_cliente(self, cliente): # calcula o imc do cliente dentro da interface 
        peso = cliente.peso
        altura = cliente.altura
        return peso/pow(altura,2)
    
    def listarExerciciosDeClient(self, cliente):
        return cliente.listarExercicios()
    
    def abrirTreino(self, cliente): # abre ficha de treino na interface 
        lines = ''
        for exercicio in cliente.listaExerciciosName:
            lines += f"{str(exercicio)}\n"
        if lines == '':
            messagebox.showerror("Erro", "Não possui ficha!.")
        return lines

    def retornarAval(self, cliente): # retorna avaliação feita pelo cliente na interface
        valores = {}
        for medida in dir(cliente.MedidasCorporais):
            if not medida.startswith('__') and not callable(getattr(cliente.MedidasCorporais, medida)):
                valores[medida] = getattr(cliente.MedidasCorporais, medida)
        return valores

    def saveAval(self, email, valores): # salva valores da avaliação do cliente
        self.persistenciaClient.salvar_dados(email,valores)
        
