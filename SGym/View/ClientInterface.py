import sys
import os
currentdir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(currentdir)
sys.path.append(parent_dir) 
from Controller.ControllerClient import ControllerClient
import customtkinter
from View import Avaliacao

class ClientInterface:
    @staticmethod
    def interfClient(cliente_logado, controladorClient):
        logado = cliente_logado
        window = customtkinter.CTk()
        window.geometry("900x600")
        window.title("Painel Cliente")
        window.resizable(False, False)

        text = customtkinter.CTkLabel(window, text="Tela Cliente")
        text.pack(padx=10, pady=10)

        buttonPT = customtkinter.CTkButton(
            window,
            text="Ficha de Treino",
            command=lambda: ClientInterface.mostrar_ficha_de_treino(cliente_logado, controladorClient)
        )
        buttonPT.pack(padx=0, pady=4)

        buttonAval = customtkinter.CTkButton(window, text="Avaliação", command=lambda: Avaliacao.Avaliacao.interfAval(logado, controladorClient))
        buttonAval.pack(padx=0, pady=4)

        def mostrar_imc(controladorClient):
            #peso = logado.peso  # Obtém o peso do cliente logado
            #altura = logado.altura  # Obtém a altura do cliente logado
            imc = controladorClient.calcular_imc_cliente(logado)
            buttonIMC.configure(text=f"IMC: {imc:.2f}")

        buttonIMC = customtkinter.CTkButton(window, text="Calcular IMC", command=lambda: mostrar_imc(controladorClient))
        buttonIMC.pack(padx=0, pady=4)

        window.mainloop()

    @staticmethod
    def mostrar_ficha_de_treino(cliente, controladorCliente):
        ficha_window = customtkinter.CTkToplevel()
        ficha_window.geometry("400x300")
        ficha_window.title("Ficha de Treino")
        ficha_window.resizable(False, False)

        text = customtkinter.CTkLabel(ficha_window, text="Ficha de Treino")
        text.pack(padx=10, pady=10)
        exercicios_text = controladorCliente.listarExerciciosDeClient(cliente)
        exercicios_label = customtkinter.CTkLabel(ficha_window, text=exercicios_text)
        exercicios_label.pack(padx=10, pady=10)

        close_button = customtkinter.CTkButton(ficha_window, text="Fechar", command=ficha_window.destroy)
        close_button.pack(padx=10, pady=10)
