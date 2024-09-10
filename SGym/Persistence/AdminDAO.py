import sys
import os
from Persistence.DAO import DAO
 
currentdir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(currentdir)
sys.path.append(parent_dir) 
caminho_arquivo = os.path.join(parent_dir, 'Persistence', 'dados_admin.txt')
caminho_arquivo2 = os.path.join(parent_dir, 'Persistence', 'dadosCorpo.txt')

class persistenciaAdmin(DAO):
    __instancia = None

    @staticmethod
    def instancias():
        if (persistenciaAdmin.__instancia == None):
            persistenciaAdmin.__instancia = persistenciaAdmin()
        return persistenciaAdmin.__instancia
    
    def leituraCadastro(self, controladorAdmin): # Leitura de dados do ADMIN que estão em dados_admin
        with open(caminho_arquivo, 'r') as arquivo:
            for linha in arquivo:
                nome, cpf, email, senha, peso, altura, tipo = linha.strip().split(',')
                controladorAdmin.leituraArquivoAdmin(nome, int(cpf), email, senha, float(peso), float(altura), int(tipo))   

    def escritaUser(self, user): # Escreve no final do arquivo de dados_admin um admin
        with open(caminho_arquivo, 'a') as f:  
            f.write(f"\n{user.nome},{user.cpf},{user.email},{user.senha},-1,-1,{user.tipo}")  

    def persistenciaCadastro(self, controlador): # persiste os dados de dados_admin
        with open(caminho_arquivo, 'w') as arquivo:
            for idx, item in enumerate(controlador.listaAdmin):
                    if idx != 0:
                        arquivo.write("\n")
                    arquivo.write(f"{item.nome},{item.cpf},{item.email},{item.senha},{-1},{-1},{item.tipo}") 
    
    def deleteUserByEmail(self, email):  # deleta cliente por email 
        lines = []
        with open(caminho_arquivo, 'r') as arquivo:
            for linha in arquivo:
                if linha.strip().split(',')[2] != email:  # Mantém apenas as linhas cujo email não corresponde ao fornecido
                    lines.append(linha.strip())  # Remover o '\n' ao final de cada linha
        with open(caminho_arquivo, 'w') as arquivo:
            for i, line in enumerate(lines):
                if i < len(lines) - 1:
                    arquivo.write(line + '\n')  # Adiciona '\n' para todas as linhas, exceto a última
                else:
                    arquivo.write(line)  # Para a última linha, não adicionar '\n'
