import sys
import os
currentdir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(currentdir)
sys.path.append(parent_dir) 
from Controller import ControllerClient
from View import AdminInterface
from View import ClientInterface
from View import PTInterface
from Controller import ControllerAdmin
from Controller import ControllerPT
import customtkinter
from tkinter import *
from tkinter import messagebox

class intefaceLR:
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    controladorCliente = ControllerClient.ControllerClient()
    controladorAdmin = ControllerAdmin.ControllerAdmin()
    controladorPersonalTrainer = ControllerPT.ControllerPT()
    controladorCliente.loadData(controladorCliente.persistenciaClient ,controladorCliente)
    controladorAdmin.loadData(controladorAdmin.persistenciaAdmin, controladorAdmin)
    controladorPersonalTrainer.loadData(controladorPersonalTrainer.persistenciaPT, controladorPersonalTrainer)
    controladorPersonalTrainer.loadClientesPT(controladorCliente.listaClient)
    cliente_logado = None

    def menu(self):
        window = customtkinter.CTk()
        window.geometry('500x300')
        window.title("Sistema - Academia")
        window.resizable(False, False)

        # Frame 
        login_frame = customtkinter.CTkFrame(window, width=350, height=250)
        login_frame.pack(pady=20)

        def check_login(email, senha):
            resultado_login = self.controladorCliente.verificaLogin(email, senha, self.controladorCliente.listaClient)
            if(resultado_login == -1):     
                resultado_login = self.controladorAdmin.verificaLogin(email, senha, self.controladorAdmin.listaAdmin)

            if(resultado_login == -1):
                resultado_login = self.controladorPersonalTrainer.verificaLogin(email, senha, self.controladorPersonalTrainer.listaPT)
                
            if resultado_login == 1:
                window.destroy()  # Fecha a janela inicial
                self.cliente_logado = self.controladorAdmin.getUserByEmail(email, self.controladorAdmin.listaAdmin)
                AdminInterface.InterfaceAdmin.menu(self.cliente_logado, self.controladorAdmin, self.controladorCliente.listaClient, self.controladorPersonalTrainer.listaPT, self.controladorCliente.persistenciaClient, self.controladorPersonalTrainer.persistenciaPT)

            elif resultado_login == 2:  
                window.destroy()  # Fecha a janela inicial
                self.cliente_logado = self.controladorPersonalTrainer.getUserByEmail(email, self.controladorPersonalTrainer.listaPT)
                PTInterface.PersonalInterface.create_interface(self.cliente_logado, self.controladorPersonalTrainer, self.controladorCliente.listaClient)

            elif resultado_login == 3:
                window.destroy()  # Fecha a janela inicial
                self.cliente_logado = self.controladorCliente.getUserByEmail(email, self.controladorCliente.listaClient)
                ClientInterface.ClientInterface.interfClient(self.cliente_logado, self.controladorCliente)

            else:
                # Exibe uma mensagem de erro para qualquer outro resultado
                messagebox.showerror("Erro", "Dados Incorretos")


        text = customtkinter.CTkLabel(login_frame, text="Login", font=("Roboto", 17))
        text.pack(padx=10, pady=15)

        email = customtkinter.CTkEntry(login_frame, placeholder_text="E-mail")
        email.pack(padx=10, pady=10)

        password = customtkinter.CTkEntry(login_frame, placeholder_text="Senha", show="*")
        password.pack(padx=10, pady=10)

        login_button = customtkinter.CTkButton(login_frame, text="Login", command=lambda: check_login(email.get(), password.get()))
        login_button.pack(padx=10, pady=10)
                
        def fun_registrar():
            login_frame.pack_forget()

            reg_frame = customtkinter.CTkFrame(master=window, width= 350, height = 250)
            reg_frame.pack(pady=10)
            
            reg_nome = customtkinter.CTkEntry(reg_frame, placeholder_text="Digite seu nome")
            reg_nome.pack(padx=10, pady=10)

            reg_email = customtkinter.CTkEntry(reg_frame, placeholder_text="Digite seu e-mail")
            reg_email.pack(padx=10, pady=10)

            reg_password = customtkinter.CTkEntry(reg_frame, placeholder_text="Digite uma senha", show="*")
            reg_password.pack(padx=10, pady=10)

            reg_password1 = customtkinter.CTkEntry(reg_frame, placeholder_text="Repita sua senha", show="*")
            reg_password1.pack(padx=10, pady=10)

            reg_cpf = customtkinter.CTkEntry(reg_frame, placeholder_text="Digite seu CPF", )
            reg_cpf.pack(padx=10, pady=10)

            def register_and_back():
                self.controladorCliente.registerUser(reg_nome.get(), reg_cpf.get(), reg_email.get(), reg_password.get(), reg_password1.get(), 3, None, None)
                reg_frame.pack_forget()
                login_frame.pack(pady=20)
            
            reg_button = customtkinter.CTkButton(reg_frame, text="Registrar", fg_color="green", hover_color="#2D9334", command=lambda: register_and_back())
            reg_button.pack(padx=10, pady=10)

            def verificar_campos():
                if not all(entry.get() for entry in (reg_nome, reg_email, reg_password, reg_password1, reg_cpf)):
                    messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
                    return
                else:
                    register_and_back()

            reg_button.configure(command=verificar_campos)
            
        register_button = customtkinter.CTkButton(login_frame, text="Registrar", fg_color="green", hover_color="#2D9334", command=fun_registrar)
        register_button.pack(padx=10, pady=10)

        window.mainloop()
        self.controladorCliente.saveData(self.controladorCliente.persistenciaClient, self.controladorCliente) 
        self.controladorAdmin.saveData(self.controladorAdmin.persistenciaAdmin, self.controladorAdmin)

# login_frame.pack_forget()
