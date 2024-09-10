import sys
import os
currentdir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(currentdir)
sys.path.append(parent_dir) 

from Controller import ControllerPT
from Model.User import *
from Controller.ControllerClient import ControllerClient

class Admin(User):
    def __init__(self, nome, cpf, email, senha, tipo):
        super().__init__(nome, cpf, email, senha, tipo)

    def createPT(self, nome, cpf, email, senha, tipo, especialidade):
        personal_trainer = ControllerPT.registerPT(nome, cpf, email, senha, tipo, especialidade)
        return personal_trainer
    
    @classmethod
    def createAdmin(self, nome, cpf, email, senha, tipo):
        administrator = Admin(nome, cpf, email, senha, tipo)
        return administrator
    
    def createClient(self, nome, cpf, email, senha, tipo, peso, altura):
        newClient = ControllerClient.registerClient(nome, cpf, email, senha, tipo, peso, altura)
        return newClient