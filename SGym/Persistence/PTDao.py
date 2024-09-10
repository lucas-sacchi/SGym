import sys
import os
from Persistence.DAO import DAO
currentdir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(currentdir)
sys.path.append(parent_dir) 
caminho_arquivo = os.path.join(parent_dir, 'Persistence', 'dados_pt.txt')
caminho_arquivo2 = os.path.join(parent_dir, 'Persistence', 'dadosCorpo.txt')
caminho_listaExercicios = os.path.join(parent_dir, 'Persistence', 'listaExercicios.txt')
caminho_listaClientePT = os.path.join(parent_dir, 'Persistence', 'listaClientesPT.txt')
class persistenciaPT(DAO):
    __instancia = None

    @staticmethod
    def instancias():
        if (persistenciaPT.__instancia == None):
            persistenciaPT.__instancia = persistenciaPT()
        return persistenciaPT.__instancia

    def leituraCadastro(self, controlador): # leitura de dados_pt
        with open(caminho_arquivo, 'r') as arquivo:
            for linha in arquivo:
                nome, cpf, email, senha, peso, altura, tipo = linha.strip().split(',')
                if int(tipo) == 2:
                    controlador.leituraArquivoPT(nome, int(cpf), email, senha, int(tipo), "não definido")   

    def deleteUserByEmail(self, email): # deleta cliente por email 
        pass

    def escritaUser(self, user): # escreve personal trainer
        with open(caminho_arquivo, 'a') as f:  # Abra o arquivo em modo de adição ('a')
            f.write(f"\n{user.nome},{user.cpf},{user.email},{user.senha},-1,-1,{user.tipo}")  # Adicione '\n' para separar os registros 

    def persistenciaCadastro(self, controlador): # persistencia de cadastro em dados_pt
        with open(caminho_arquivo, 'a') as arquivo:
            for item in controlador.listaPT:
                    arquivo.write(f"{item.nome},{item.cpf},{item.email},{item.senha},{-1},{-1},{item.tipo}, {item.especialidade}\n") 
  
    def persistenciaExerciciosPT(lines, listaExercicios, cpf): # persistencia de exercicios pra cliente feitos pelo PT
        with open(caminho_listaExercicios, 'w') as file:
            for line in lines:
                file.write(f"{line}\n")
        with open(caminho_listaExercicios, 'a') as file:
            file.write(f"CPF: {cpf}")
            for exercicio in listaExercicios:
                file.write(f"\n{exercicio}")

    def save_exercises(self, listaPT): # botao pra salvar exercicios 
        lines = []
        aux = 0
        for personal in listaPT:
            for aluno in personal.listaAlunos:
                cpf_aluno = aluno.cpf
                if aluno.listaExerciciosName != []:
                    if aux == 0:
                        lines.append(f"CPF: {cpf_aluno}")
                        aux = 1
                    else:
                        lines.append(f"\nCPF: {cpf_aluno}")
                    for exercicios in aluno.listaExerciciosName:
                        lines.append(f"\n{exercicios}")
        with open(caminho_listaExercicios, 'w') as file:
            for line in lines:
                file.write(line)
        
    def registrarAluno(self, cpf, cpf_personal): # registra aluno na lista que pt tem em um arquivo 
        with open(caminho_listaClientePT, 'r') as arquivo:
            linhas = arquivo.readlines()
        cpf_encontrado = False
        linhas_filtradas = ''
        linhas2 = ''
        for linha in linhas:
            if linha.startswith(f"CPF_PT: {str(cpf_personal)}"):
                cpf_encontrado = True
                linhas2 += f"CPF_PT: {str(cpf_personal)}\n"
                continue
            if cpf_encontrado and linha.startswith("CPF: "):
                linhas2 += linha
            if linha.startswith(f"CPF_PT: ") and cpf_encontrado:
                linhas_filtradas += linha
                cpf_encontrado = False
        if linhas2 == '':
            linhas2 += f"CPF_PT: {str(cpf_personal)}"
        linhas2 += f"\nCPF: {str(cpf)}"
        with open(caminho_listaClientePT, 'w') as arquivo:
            if linhas_filtradas != '':
                arquivo.writelines(linhas_filtradas)
            if linhas2 != '':
                arquivo.writelines(linhas2)

