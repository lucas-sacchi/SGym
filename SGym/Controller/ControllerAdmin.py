import sys
import os
currentdir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(currentdir)
sys.path.append(parent_dir) 
from Model import Admin 
from Model import PersonalTrainer
from Model import Client
from Persistence import AdminDAO
from Controller.ControllerDecorator import ControllerDecorator
caminho_arquivo = os.path.join(parent_dir, 'Persistence', 'dados_admin.txt')

class ControllerAdmin(ControllerDecorator):
    def __init__(self):
        self.listaAdmin = []
        self.persistenciaAdmin = AdminDAO.persistenciaAdmin.instancias()
        self.controlador = ControllerDecorator

    def delete_user_by_email(self, listaClient, listaPersonal, email, persistenciaClient, persistenciaPT):
        for client in listaClient:
            if client.email == email:
                listaClient.remove(client)
                persistenciaClient.deleteUserByEmail(email)
                return True
            
        for admin in self.listaAdmin:
            if admin.email == email:
                self.listaAdmin.remove(admin)
                self.persistenciaAdmin.deleteUserByEmail(email)
                return True
            
        for personal in listaPersonal:
            if personal.email == email:
                listaPersonal.remove(personal)
                persistenciaPT.deleteUserByEmail(email)
                return True
        return False  # Retorna False se o usuário não for encontrado

    def registerAdmin(self, nome, cpf, email, senha, tipo, listaClient, listaPT, persistenciaClient, persistenciaPT): # registra usuarios de acordo com tipo
        sucess = True
        if tipo == 1:
            for user in self.listaAdmin:
                if user.email == email or user.cpf == cpf:
                    sucess = False
            if sucess:
                administrator = Admin.Admin.createAdmin(nome, cpf, email, senha, tipo)
                self.listaAdmin.append(administrator)
                self.persistenciaAdmin.escritaUser(administrator)
        elif tipo == 2:
            for user in listaPT:
                if user.email == email or user.cpf == cpf:
                    sucess = False
            if sucess:
                pt = PersonalTrainer.PersonalTrainer.registerPT(nome, cpf, email, senha, tipo, "não definido")
                listaPT.append(pt)
                persistenciaPT.escritaUser(pt)
        else: 
            for user in listaClient:
                if user.email == email or user.cpf == cpf:
                    sucess = False
            if sucess:
                client = Client.Client.registerClient(nome, cpf, email, senha, tipo)
                listaClient.append(client)
                persistenciaClient.escritaUser(client)

    def leituraArquivoAdmin(self, nome, cpf, email, senha, peso, altura, tipo):
        admin = Admin.Admin(nome, cpf, email, senha, tipo)
        self.listaAdmin.append(admin)

