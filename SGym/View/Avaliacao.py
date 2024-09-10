import sys
import os
currentdir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(currentdir)
sys.path.append(parent_dir) 
import customtkinter

class Avaliacao:
    @staticmethod
    def interfAval(cliente_logado, controladorClient):
        email = cliente_logado.email  # Obtendo o email do cliente logado
        window = customtkinter.CTk()
        window.geometry("910x910")
        window.title("Avaliação")
        window.resizable(False, False)

        text = customtkinter.CTkLabel(window, text="Avaliação")
        text.pack(padx=10, pady=10)

        valores = controladorClient.retornarAval(cliente_logado)

        # Adicionando caixas de texto com os valores das medidas corporais
        entries = {}
        for info, valor in valores.items():
            label = customtkinter.CTkLabel(window, text=info.capitalize())
            label.pack()
            entry = customtkinter.CTkEntry(window)
            entry.pack()
            entry.insert(0, str(valor))  # preenche a entrada com o valor
            entries[info] = entry
        
        
        salvar_button = customtkinter.CTkButton(window, text="Salvar", command=lambda: salvar_dados(email, entries, controladorClient))
        salvar_button.pack(padx=10, pady=10)

        def salvar_dados(email, valores, controladorClient):
            valores_atualizados = {info: valores.get() for info, valores in valores.items()}
            controladorClient.saveAval(email,valores_atualizados)

        window.mainloop()
    