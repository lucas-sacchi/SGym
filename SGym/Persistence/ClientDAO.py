import sys
import os
from Model import Client
from Persistence.DAO import DAO
currentdir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(currentdir)
sys.path.append(parent_dir) 
caminho_arquivo = os.path.join(parent_dir, 'Persistence', 'dados_client.txt')
caminho_arquivo2 = os.path.join(parent_dir, 'Persistence', 'dadosCorpo.txt')
caminho_arquivoExercicios = os.path.join(parent_dir, 'Persistence', 'listaExercicios.txt')

class persistenciaClient(DAO):
    __instancia = None

    @staticmethod
    def instancias():
        if (persistenciaClient.__instancia == None):
            persistenciaClient.__instancia = persistenciaClient()
        return persistenciaClient.__instancia

    def deleteUserByEmail(self, email): # deleta cliente por email 
        lines = []
        with open(caminho_arquivo, 'r') as arquivo:
            for linha in arquivo:
                if linha.strip().split(',')[2] != email:  # Mantém apenas as linhas cujo email não corresponde ao fornecido
                    lines.append(linha)
        with open(caminho_arquivo, 'w') as arquivo:
            for line in lines:
                arquivo.write(line)

    def leituraCadastro(self, controlador): # leitura de dados de dados_client
        with open(caminho_arquivo, 'r') as arquivo:
            for linha in arquivo:
                nome, cpf, email, senha, peso, altura, tipo = linha.strip().split(',')
                cliente = Client.Client(nome, int(cpf), email, senha, int(tipo), float(peso), float(altura))
                controlador.listaClient.append(cliente)
        with open(caminho_arquivoExercicios, 'r') as file: # Leitura de dadosCorpo
            client = None
            for line in file:
                line = line.strip()
                if line.startswith("CPF"):
                    cpf = int(line.split(": ")[1])
                    client = None
                    for client in controlador.listaClient:
                        if client.cpf == cpf:
                            client = client
                            break
                elif client:
                    client.listaExerciciosName.append(line)

    def persistenciaCadastro(self, controlador): # persiste dados de dados_client
        with open(caminho_arquivo, 'w') as arquivo:
            for index, item in enumerate(controlador.listaClient):
                if index != 0:  # Adiciona nova linha antes de cada item exceto o primeiro
                    arquivo.write("\n")
                arquivo.write(f"{item.nome},{item.cpf},{item.email},{item.senha},{item.peso},{item.altura},{item.tipo}")

    def escritaUser(self, user): # escreve em dados_client
        with open(caminho_arquivo, 'a') as arquivo:
            arquivo.write(f"\n{user.nome},{user.cpf},{user.email},{user.senha},{user.peso},{user.altura},{user.tipo}")

    def escrever_exercicios_em_arquivo(self, cliente): # escreve exercicios na lista de exercicios
        with open(f"{cliente.nome}_exercicios.txt", "w") as arquivo:
            for exercicio in cliente.listaExercicios:
                arquivo.write(exercicio + '\n')
    
    def escreverAval(self, cliente): # escreve avaliacao do cliente
        valores = []
        with open(caminho_arquivo2, 'r') as arquivo:
            email_atual = None
            for linha in arquivo:
                linha = linha.strip()
                if linha.startswith("Email:"):
                    email_atual = linha.split(": ")[1].strip()
                elif email_atual == cliente.email:
                    dados = linha.split(": ")
                    if len(dados) == 2:  
                        valores.append(float(dados[1]))
        if valores != []:
            cliente.MedidasCorporais.atualizaMedidas(valores[0],valores[1],valores[2],valores[3],valores[4],valores[5],valores[6],valores[7],valores[8],valores[9],valores[10],valores[11],valores[12],valores[13])
    
    def salvar_dados(email, valores): 
        with open(caminho_arquivo2, 'r') as arquivo:
            linhas = arquivo.readlines()
        email_encontrado = False
        linhas_filtradas = []
        for linha in linhas:
            if linha.startswith(f"Email: {email}"):
                email_encontrado = True
                continue
            if email_encontrado and linha.startswith("Email: "):
                email_encontrado = False
            if not email_encontrado:
                linhas_filtradas.append(linha)
        with open(caminho_arquivo2, 'w') as arquivo:
            arquivo.writelines(linhas_filtradas)
            arquivo.write(f"Email: {email}\n")
            for info, entry in valores.items():
                arquivo.write(f"{info}: {entry}\n")