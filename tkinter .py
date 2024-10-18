import tkinter as tk
from tkinter import messagebox

# Variáveis globais
usuarios = []
saldo = 0
cofres = []

# Função de cadastro
def cadastro():
    login = login_entry.get()
    senha = senha_entry.get()
    
    if login and senha:
        usuario = {'login': login, 'senha': senha}
        usuarios.append(usuario)
        messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
    else:
        messagebox.showwarning("Erro", "Preencha todos os campos!")

# Função de login
def login():
    login_input = login_entry.get()
    senha_input = senha_entry.get()

    usuario_encontrado = False
    for usuario in usuarios:
        if usuario['login'] == login_input and usuario['senha'] == senha_input:
            usuario_encontrado = True
            messagebox.showinfo("Sucesso", "Login efetuado com sucesso!")
            mostrar_menu_usuario()  # Mostrar o menu do usuário
            break
    
    if not usuario_encontrado:
        messagebox.showerror("Erro", "Usuário ou Senha incorretos!")

# Função para mostrar o menu do usuário após login
def mostrar_menu_usuario():
    login_frame.pack_forget()
    menu_usuario_frame.pack()

# Função para adicionar saldo
def add_saldo():
    global saldo
    adicionar = float(saldo_entry.get())
    saldo += adicionar
    atualizar_saldo()
    messagebox.showinfo("Sucesso", f"Saldo atualizado! Saldo atual: {saldo}")

# Função para remover saldo
def remover_saldo():
    global saldo
    remover = float(saldo_entry.get())
    saldo -= remover
    atualizar_saldo()
    messagebox.showinfo("Sucesso", f"Saldo atualizado! Saldo atual: {saldo}")

# Função para criar o cofre
def add_cofre():
    nome_cofre = nome_cofre_entry.get()
    cofre = {"nome": nome_cofre, "saldo": 0}
    cofres.append(cofre)
    messagebox.showinfo("Sucesso", f"Cofre '{nome_cofre}' criado!")

# Função para adicionar valor ao cofre
def add_valor_classe():
    global saldo
    findcofre = cofre_entry.get()
    addvalor = float(valor_entry.get())
    
    if addvalor <= saldo:
        for cofrinho in cofres:
            if cofrinho["nome"] == findcofre:
                cofrinho["saldo"] += addvalor
                saldo -= addvalor
                atualizar_saldo()
                messagebox.showinfo("Sucesso", f"Adicionado {addvalor} ao cofre '{findcofre}'. Saldo restante: {saldo}")
                return
        messagebox.showerror("Erro", "Cofre não encontrado!")
    else:
        messagebox.showerror("Erro", "Saldo insuficiente!")

# Função para remover valor do cofre
def remover_valor_classe():
    global saldo
    findcofre = cofre_entry.get()
    removervalor = float(valor_entry.get())
    
    for cofrinho in cofres:
        if cofrinho["nome"] == findcofre:
            if removervalor <= cofrinho["saldo"]:
                cofrinho["saldo"] -= removervalor
                saldo += removervalor
                atualizar_saldo()
                messagebox.showinfo("Sucesso", f"Removido {removervalor} do cofre '{findcofre}'. Saldo: {saldo}")
                return
            else:
                messagebox.showerror("Erro", "Saldo insuficiente no cofre!")
    messagebox.showerror("Erro", "Cofre não encontrado!")

# Função para excluir o cofre
def excluir_classe():
    global saldo
    removerclass = cofre_entry.get()
    
    for cofrinho in cofres:
        if cofrinho["nome"] == removerclass:
            saldo += cofrinho["saldo"]
            cofres.remove(cofrinho)
            atualizar_saldo()
            messagebox.showinfo("Sucesso", f"Cofre '{removerclass}' removido! Saldo atualizado: {saldo}")
            return
    messagebox.showerror("Erro", "Cofre não encontrado!")

# Função para visualizar cofres e saldos
def ver_cofres():
    if cofres:
        info = "\n".join([f"Cofre: {cofre['nome']} - Saldo: {cofre['saldo']}" for cofre in cofres])
        messagebox.showinfo("Cofres", info)
    else:
        messagebox.showinfo("Cofres", "Nenhum cofre disponível.")

# Função para atualizar o saldo exibido
def atualizar_saldo():
    saldo_label.config(text=f"Saldo Atual: {saldo}")

# Configurações da interface gráfica
root = tk.Tk()
root.title("Controle de Gastos - Visual Retrô")
root.geometry("500x500")

# Estilo retrô (Modo escuro)
root.configure(bg="#2E2E2E")

# Configurações de estilo para widgets
retro_font = ("Courier", 12)
btn_bg_color = "#4E4E4E"
btn_fg_color = "#FFFFFF"
entry_bg_color = "#4E4E4E"
entry_fg_color = "#FFFFFF"

# Tela inicial (Cadastro/Login)
login_frame = tk.Frame(root, bg="#2E2E2E")
login_frame.pack(pady=20)

tk.Label(login_frame, text="Login:", font=retro_font, bg="#2E2E2E", fg="#FFFFFF").grid(row=0, column=0, pady=5)
login_entry = tk.Entry(login_frame, font=retro_font, bg=entry_bg_color, fg=entry_fg_color)
login_entry.grid(row=0, column=1)

tk.Label(login_frame, text="Senha:", font=retro_font, bg="#2E2E2E", fg="#FFFFFF").grid(row=1, column=0, pady=5)
senha_entry = tk.Entry(login_frame, font=retro_font, show="*", bg=entry_bg_color, fg=entry_fg_color)
senha_entry.grid(row=1, column=1)

tk.Button(login_frame, text="Cadastro", command=cadastro, font=retro_font, bg=btn_bg_color, fg=btn_fg_color).grid(row=2, column=0, pady=10)
tk.Button(login_frame, text="Login", command=login, font=retro_font, bg=btn_bg_color, fg=btn_fg_color).grid(row=2, column=1, pady=10)

# Menu do Usuário (aparece após o login)
menu_usuario_frame = tk.Frame(root, bg="#2E2E2E")

# Label do menu com o saldo visível
tk.Label(menu_usuario_frame, text="Menu do Usuário", font=("Courier", 16), bg="#2E2E2E", fg="#FFFFFF").pack(pady=10)

saldo_label = tk.Label(menu_usuario_frame, text=f"Saldo Atual: {saldo}", font=retro_font, bg="#2E2E2E", fg="#FFFFFF")
saldo_label.pack(pady=10)

tk.Button(menu_usuario_frame, text="Adicionar Saldo", command=add_saldo, font=retro_font, bg=btn_bg_color, fg=btn_fg_color).pack(pady=5)
tk.Button(menu_usuario_frame, text="Remover Saldo", command=remover_saldo, font=retro_font, bg=btn_bg_color, fg=btn_fg_color).pack(pady=5)

saldo_entry = tk.Entry(menu_usuario_frame, font=retro_font, bg=entry_bg_color, fg=entry_fg_color)
saldo_entry.pack(pady=5)

tk.Label(menu_usuario_frame, text="Nome do Cofre:", font=retro_font, bg="#2E2E2E", fg="#FFFFFF").pack(pady=5)
nome_cofre_entry = tk.Entry(menu_usuario_frame, font=retro_font, bg=entry_bg_color, fg=entry_fg_color)
nome_cofre_entry.pack(pady=5)

tk.Button(menu_usuario_frame, text="Criar Cofre", command=add_cofre, font=retro_font, bg=btn_bg_color, fg=btn_fg_color).pack(pady=5)

tk.Label(menu_usuario_frame, text="Cofre:", font=retro_font, bg="#2E2E2E", fg="#FFFFFF").pack(pady=5)
cofre_entry = tk.Entry(menu_usuario_frame, font=retro_font, bg=entry_bg_color, fg=entry_fg_color)
cofre_entry.pack(pady=5)

tk.Label(menu_usuario_frame, text="Valor:", font=retro_font, bg="#2E2E2E", fg="#FFFFFF").pack(pady=5)
valor_entry = tk.Entry(menu_usuario_frame, font=retro_font, bg=entry_bg_color, fg=entry_fg_color)
valor_entry.pack(pady=5)

tk.Button(menu_usuario_frame, text="Adicionar Valor ao Cofre", command=add_valor_classe, font=retro_font, bg=btn_bg_color, fg=btn_fg_color).pack(pady=5)
tk.Button(menu_usuario_frame, text="Remover Valor do Cofre", command=remover_valor_classe, font=retro_font, bg=btn_bg_color, fg=btn_fg_color).pack(pady=5)
tk.Button(menu_usuario_frame, text="Excluir Cofre", command=excluir_classe, font=retro_font, bg=btn_bg_color, fg=btn_fg_color).pack(pady=5)
tk.Button(menu_usuario_frame, text="Ver Cofres", command=ver_cofres, font=retro_font, bg=btn_bg_color, fg=btn_fg_color).pack(pady=10)

# Iniciar a interface gráfica
root.mainloop()
