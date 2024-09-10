import customtkinter as ctk
from tkinter import simpledialog, ttk

class PersonalInterface:
    @staticmethod
    def create_interface(cliente_logado, controladorPT, listaClient):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        root = ctk.CTk()
        root.geometry("900x600")
        root.title("Painel Personal")
        root.resizable(False, False)

        personal_frame = ctk.CTkFrame(root)
        personal_frame.pack(pady=10, padx=10, fill='x', anchor='nw')

        personal_label = ctk.CTkLabel(personal_frame, text=f"Personal: {cliente_logado.nome}\nCPF: {cliente_logado.cpf}")
        personal_label.pack(anchor='w')

        main_frame = ctk.CTkFrame(root)
        main_frame.pack(pady=10, padx=10, fill='x')

        list_users_button = ctk.CTkButton(main_frame, text="Listar Usuários", command=lambda: PersonalInterface.list_users(controladorPT, cliente_logado))
        list_users_button.pack(pady=5)

        criar_Aluno = ctk.CTkEntry(main_frame, placeholder_text="Cadastro CPF Aluno")
        criar_Aluno.pack(padx=10, pady=10)

        list_users_button = ctk.CTkButton(main_frame, text="Registrar Aluno", command=lambda: PersonalInterface.registrarAluno(controladorPT, criar_Aluno.get(), listaClient, cliente_logado))
        list_users_button.pack(pady=5)

        # Caixa de texto para exibir os usuários listados
        PersonalInterface.users_list_frame = ctk.CTkFrame(main_frame)
        PersonalInterface.users_list_frame.pack(pady=5, fill='x')

        # Notebook para as abas dos alunos
        PersonalInterface.notebook = ttk.Notebook(root)
        PersonalInterface.notebook.pack(pady=10, padx=10, fill='both', expand=True)

        root.mainloop()

    @staticmethod
    def list_users(controladorPT, cliente_logado):
        lista = controladorPT.listarClientesPT(cliente_logado)
        for widget in PersonalInterface.users_list_frame.winfo_children():
            widget.destroy()

        for user in lista:
            frame = ctk.CTkFrame(PersonalInterface.users_list_frame)
            frame.pack(fill='x', pady=2)

            label = ctk.CTkLabel(frame, text=user.nome)
            label.pack(side='left', padx=5)

            button = ctk.CTkButton(frame, text="Go to Exercises", command=lambda u=user: PersonalInterface.open_user_tab(u, cliente_logado, controladorPT))
            button.pack(side='right', padx=5)

    @staticmethod
    def open_user_tab(user, cliente_logado, controladorPT):
        idx_aluno = cliente_logado.listaAlunos.index(user)
        aluno = cliente_logado.listaAlunos[idx_aluno]

        # Verifica se a aba do aluno já existe
        for i in range(PersonalInterface.notebook.index("end")):
            if PersonalInterface.notebook.tab(i, "text") == aluno.nome:
                PersonalInterface.notebook.select(i)
                return

        if not hasattr(aluno, 'labels'):
            aluno.listaExercicios = []
            aluno.labels = []
            aluno.check_vars = []

        tab = ttk.Frame(PersonalInterface.notebook)
        PersonalInterface.notebook.add(tab, text=aluno.nome)

        exercise_frame = ctk.CTkFrame(tab)
        exercise_frame.pack(pady=10, padx=10, fill='x')

        add_exercise_button = ctk.CTkButton(exercise_frame, text="Adicionar Exercicios", command=lambda: PersonalInterface.add_exercise(aluno, tab))
        add_exercise_button.grid(row=0, column=0, padx=5, pady=5)

        save_exercises_button = ctk.CTkButton(exercise_frame, text="Salvar", command=lambda: PersonalInterface.save_exercises(controladorPT))
        save_exercises_button.grid(row=0, column=1, padx=5, pady=5)

        exercise_list_frame = ctk.CTkFrame(exercise_frame)
        exercise_list_frame.grid(row=1, column=0, columnspan=3, pady=10)

        aluno.labels.append(exercise_list_frame)

        # Reutiliza os widgets dos exercícios existentes
        for i, (chk, edit_button, remove_button) in enumerate(aluno.listaExercicios):
            chk.master = exercise_list_frame
            chk.grid(row=i, column=0, padx=5, pady=5, sticky='w')
            edit_button.master = exercise_list_frame
            edit_button.grid(row=i, column=1, padx=5, pady=5)
            remove_button.master = exercise_list_frame
            remove_button.grid(row=i, column=2, padx=5, pady=5)

    @staticmethod
    def create_exercise_widget(aluno, exercise_name, tab):
        var = ctk.IntVar(value=1)  # Checkbox marcada por padrão
        row = len(aluno.listaExercicios)

        chk = ctk.CTkCheckBox(aluno.labels[0], text=exercise_name, variable=var)
        chk.grid(row=row, column=0, padx=5, pady=5, sticky='w')

        edit_button = ctk.CTkButton(aluno.labels[0], text="Edit", command=lambda: PersonalInterface.edit_exercise(aluno, chk))
        edit_button.grid(row=row, column=1, padx=5, pady=5)

        remove_button = ctk.CTkButton(aluno.labels[0], text="Remove", command=lambda: PersonalInterface.remove_exercise(aluno, chk, edit_button, remove_button))
        remove_button.grid(row=row, column=2, padx=5, pady=5)

        aluno.listaExercicios.append((chk, edit_button, remove_button))
        aluno.listaExerciciosName.append(exercise_name)
        aluno.check_vars.append(var)

    @staticmethod
    def add_exercise(aluno, tab):
        exercise_name = simpledialog.askstring("Input", "Enter exercise name:")
        if exercise_name:
            PersonalInterface.create_exercise_widget(aluno, exercise_name, tab)

    @staticmethod
    def edit_exercise(aluno, chk):
        new_name = simpledialog.askstring("Input", "Enter new exercise name:", initialvalue=chk.cget("text"))
        if new_name:
            # Atualiza o nome do exercício na lista
            index = aluno.listaExerciciosName.index(chk.cget("text"))
            aluno.listaExerciciosName[index] = new_name
            chk.configure(text=new_name)

    @staticmethod
    def remove_exercise(aluno, chk, edit_button, remove_button):
        # Remover os widgets da interface
        chk.grid_forget()
        edit_button.grid_forget()
        remove_button.grid_forget()

        # Encontrar o índice do exercício a ser removido
        index = -1
        for i, (c, e, r) in enumerate(aluno.listaExercicios):
            if c == chk:
                index = i
                break

        # Remover o exercício das listas
        if index != -1:
            del aluno.listaExercicios[index]
            del aluno.check_vars[index]
            del aluno.listaExerciciosName[index]

        # Atualizar os widgets
        PersonalInterface.refresh_widgets(aluno)

    @staticmethod
    def refresh_widgets(aluno):
        # Reorganizar os widgets após a remoção
        for i, (chk, edit_button, remove_button) in enumerate(aluno.listaExercicios):
            chk.grid(row=i, column=0, padx=5, pady=5, sticky='w')
            edit_button.grid(row=i, column=1, padx=5, pady=5)
            remove_button.grid(row=i, column=2, padx=5, pady=5)

    def save_exercises(controladorPT):
        controladorPT.save_exercises()

    @staticmethod
    def registrarAluno(controladorPT, cpf, listaClient, personal):
        controladorPT.registrarAlunos(int(cpf), listaClient, personal)
