import sys
import os
currentdir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(currentdir)
sys.path.append(parent_dir) 

class MedidasCorporais:
    def __init__(self,  abdomen = 0, antebraco_direito = 0, antebraco_esquerdo = 0, braco_direito = 0, braco_esquerdo = 0, cintura = 0, coxa_direita = 0, coxa_esquerda = 0, ombro = 0, panturrilha_direita = 0, panturrilha_esquerda = 0, peitoral = 0, quadril = 0, torax = 0):
        self.peitoral = peitoral
        self.ombro = ombro
        self.torax = torax
        self.cintura = cintura
        self.abdomen = abdomen
        self.quadril = quadril
        self.braco_direito = braco_direito
        self.braco_esquerdo = braco_esquerdo
        self.antebraco_direito = antebraco_direito
        self.antebraco_esquerdo = antebraco_esquerdo
        self.coxa_direita = coxa_direita
        self.coxa_esquerda = coxa_esquerda
        self.panturrilha_direita = panturrilha_direita
        self.panturrilha_esquerda = panturrilha_esquerda

    def atualizaMedidas(self,  abdomen, antebraco_direito, antebraco_esquerdo, braco_direito, braco_esquerdo, cintura, coxa_direita, coxa_esquerda, ombro, panturrilha_direita, panturrilha_esquerda, peitoral, quadril, torax):
        self.peitoral = peitoral
        self.ombro = ombro
        self.torax = torax
        self.cintura = cintura
        self.abdomen = abdomen
        self.quadril = quadril
        self.braco_direito = braco_direito
        self.braco_esquerdo = braco_esquerdo
        self.antebraco_direito = antebraco_direito
        self.antebraco_esquerdo = antebraco_esquerdo
        self.coxa_direita = coxa_direita
        self.coxa_esquerda = coxa_esquerda
        self.panturrilha_direita = panturrilha_direita
        self.panturrilha_esquerda = panturrilha_esquerda