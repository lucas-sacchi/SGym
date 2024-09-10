import customtkinter
from tkinter import messagebox

class InterfaceAdmin:
    @staticmethod
    def menu(cliente_logado, controladorAdmin, listaCliente, listaPT, persistenciaClient, persistenciaPT):
        window = customtkinter.CTk()
        window.geometry("900x600")
        window.title("Painel ADMIN")
        window.resizable(False, False)

        text = customtkinter.CTkLabel(window, text="Tela ADMIN")
        text.pack(padx=10, pady=10)

        delete_frame = customtkinter.CTkFrame(window, width=350, height=150)
        delete_frame.pack(pady=20)

        delete_email_entry = customtkinter.CTkEntry(delete_frame, placeholder_text="Email do usuário a ser deletado")
        delete_email_entry.pack(padx=10, pady=10)

        def delete_user():
            email_to_delete = delete_email_entry.get()
            success = controladorAdmin.delete_user_by_email(listaCliente, listaPT, email_to_delete, persistenciaClient, persistenciaPT)
            if success:
                messagebox.showinfo("Sucesso", f"Usuário com email {email_to_delete} excluído.")
            else:
                messagebox.showerror("Erro", f"Nenhum usuário encontrado com o email {email_to_delete}.")

        delete_button = customtkinter.CTkButton(delete_frame, text="Deletar Usuário", command=delete_user)
        delete_button.pack(padx=10, pady=10)

        # Frame
        login_frame = customtkinter.CTkFrame(window, width=350, height=250)
        login_frame.pack(pady=20)

        def fun_registrar_entidade():
            login_frame.pack_forget() 
            
            reg_frame = customtkinter.CTkFrame(master=window, width= 350, height = 250)
            reg_frame.pack(pady=10)   
            
            reg_nome = customtkinter.CTkEntry(reg_frame, placeholder_text="Digite o nome")
            reg_nome.pack(padx=10, pady=10)   
            
            reg_email = customtkinter.CTkEntry(reg_frame, placeholder_text="Digite o e-mail")
            reg_email.pack(padx=10, pady=10)  
            
            reg_password = customtkinter.CTkEntry(reg_frame, placeholder_text="Digite uma senha", show="*")
            reg_password.pack(padx=10, pady=10)   
            
            reg_password1 = customtkinter.CTkEntry(reg_frame, placeholder_text="Repita a senha", show="*")
            reg_password1.pack(padx=10, pady=10)  
            
            reg_cpf = customtkinter.CTkEntry(reg_frame, placeholder_text="Digite o CPF")
            reg_cpf.pack(padx=10, pady=10)
            
            reg_tipo = customtkinter.CTkEntry(reg_frame, placeholder_text="Escolha o tipo (1 p/ ADMIN, 2 p/ PT e 3 p/ Cliente)")
            reg_tipo.pack(padx=10, pady=10)
            
            def register_and_back():
                if (int(reg_tipo.get()) >= 1 and int(reg_tipo.get()) <= 3):
                    controladorAdmin.registerAdmin(reg_nome.get(), int(reg_cpf.get()), reg_email.get(), reg_password.get(), int(reg_tipo.get()), listaCliente, listaPT, persistenciaClient, persistenciaPT)
                reg_frame.pack_forget()
                login_frame.pack(pady=20)
                
            reg_button = customtkinter.CTkButton(reg_frame, text="Registrar", fg_color = "green", hover_color = "#2D9334", command = register_and_back)
            reg_button.pack(padx=10, pady=10)  
            
            def verificar_campos():
                if not all(entry.get() for entry in (reg_nome, reg_email, reg_password, reg_password1, reg_cpf, reg_tipo)):
                    messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
                    return
                else:
                    register_and_back()
                    
            reg_button.configure(command=verificar_campos)
        
        register_button = customtkinter.CTkButton(login_frame, text="Registrar", fg_color = "green", hover_color = "#2D9334", command = fun_registrar_entidade)
        register_button.pack(padx=10, pady=10)

        window.mainloop() 
        