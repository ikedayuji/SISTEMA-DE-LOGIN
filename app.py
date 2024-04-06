import customtkinter as ctk
from tkinter import *
import sqlite3
from tkinter import messagebox

class BackEnd():
    def conecta_db(self):
        self.conn = sqlite3.connect("Sistema_cadastros.db")
        self.cursor = self.conn.cursor()
        print("Banco de dados conectado")
        
    def desconecta_db(self):
        self.conn.close()
        print("Banco de dados desconectado")
        
    def cria_tabela(self):
        self.conecta_db()
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Usuarios (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Username TEXT NOT NULL,
            Email TEXT NOT NULL,
            Senha TEXT NOT NULL,
            Confirma_Senha TEXT NOT NULL
             )
        """)
        
        try:
            if (self.username_cadastro == "" or self.email_cadastro=="" or self.senha_cadastro=="" or self.confirma_senha_cadastro==""):
                messagebox.showerror(title="Sistema de login", message="ERRO!\nPor favor preencha todos os campos!")
            elif (len(self.username_cadastro) < 4):
                messagebox.showwarning(title="Sistema de Login", message="O nome do usuário deve ter pelo menos 4 caracteres.")
            elif (len(self.senha_cadastro) < 4):
                messagebox.showwarning(title="Sistema de Login", message="A senha deve ter pelo menos 4 caracteres.")
            elif (self.senha_cadastro != self.confirma_senha_cadastro):
                messagebox.showerror(title="Sistema de login", message="ERRO!\nAs senhas que você colocou não estão iguais, coloque novamente as senhas iguais.")
            else: 
                self.conn.commit()
                messagebox.showinfo(title="Sistema de login", message="\n{self.username_cadastro}\n Os seus dados foram cadastrados com sucesso")
                self.desconecta_db()
                self.limpa_entry_cadastro()
        except:
            self.desconecta_db()
        
        
    def cadastrar_usuario(self):
        self.username_cadastro = self.username_cadastro_entry.get()
        self.email_cadastro = self.email_cadastro_entry.get()
        self.senha_cadastro = self.senha_cadastro_entry.get()
        self.confirma_senha_cadastro = self.confirma_senha_entry.get()
        
        self.conecta_db()
        
        self.cursor.execute("""
            INSERT INTO Usuarios (Username, Email, Senha, Confirma_Senha)
            VALUES (?, ?, ?, ?)""", (self.username_cadastro, self.email_cadastro, self.senha_cadastro, self.confirma_senha_cadastro))

        self.conn.commit()
        print("Dados cadastrados com sucesso!")
        self.desconecta_db()

    def verifica_login(self):
        self.username_login = self.username_login_entry.get()
        self.senha_login = self.senha_login_entry.get()
        
        self.conecta_db()
        
        self.cursor.execute("""SELECT * FROM Usuarios WHERE (Username = ? AND Senha = ?)""", (self.username_login, self.senha_login))
        
        self.verifica_dados = self.cursor.fetchone() #Percorrendo na tabela usuarios
        
        try: 
            if (self.username_login == "" or self.senha_login == ""):
                messagebox.showwarning(title="Sistema de login", message="Por favor preencha todos os campos!")
            elif (self.username_login in self.verifica_dados and self.senha_login in self.verifica_dados):
                messagebox.showinfo(title="Sistema de Login", message=f"Olá {self.username_login}\nSeu login foi feito com sucesso!")
                self.desconecta_db()
                self.limpa_entry_login()
        except:
            messagebox.showerror(title="Sistema de login", message="ERRO!!!\n Dados não encontrados no sistema. Por favor verifique os seus dados ou cadastre-se no nosso sistema")
            self.desconecta_db()
        
class App(ctk.CTk, BackEnd):
    def __init__(self):
        super().__init__()
        self.configuracoes_da_janela_inicial()
        self.tela_de_login()
    
    # Configurando a janela principal    
    def configuracoes_da_janela_inicial(self):
        largura_monitor = self.winfo_screenwidth()
        altura_monitor = self.winfo_screenheight()
        
        largura_janela = 500
        altura_janela = 600
        
        x_janela = (largura_monitor - largura_janela) // 2
        y_janela = (altura_monitor - altura_janela) // 2
        
        self.geometry(f"{largura_janela}x{altura_janela}+{x_janela}+{y_janela}")
        self.title("Tela de Login")
        self.resizable(True, True)    
        self.cria_tabela()
        self.update_idletasks()  # Atualiza a geometria da janela antes de exibir
    
    def tela_de_login(self):
        # Criar a frame do formulario de login
        self.frame_login = ctk.CTkFrame(self, width=400, height=450)
        self.frame_login.place(relx=0.5, rely=0.5, anchor="center")
  
        # Colocando widget dentro do frame - formulario de login
        self.lbtitle = ctk.CTkLabel(self.frame_login, text="Faça seu Login", font=("Century Gothic bold", 22))
        self.lbtitle.place(relx=0.5, rely=0.1, anchor="center")
        
        self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Seu nome de usuário...", font=("Century Gothic bold", 16), corner_radius=15, border_color= "#005")
        self.username_login_entry.place(relx=0.5, rely=0.25, anchor="center")
  
        self.senha_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Sua senha...", font=("Century Gothic bold", 16), corner_radius=15, border_color= "#005", show="*")
        self.senha_login_entry.place(relx=0.5, rely=0.35, anchor="center")
        
        self.btn_login = ctk.CTkButton(self.frame_login, width=30, text="Fazer Login".upper(), font=("Century Gothic bold", 14), corner_radius=15, command=self.verifica_login)
        self.btn_login.place(relx=0.5, rely=0.45, anchor="center")
        
        self.span = ctk.CTkLabel(self.frame_login, text="Se você não tem conta,\nclique no botão abaixo para cadastrar!", font=("Century Gothic", 12))
        self.span.place(relx=0.5, rely=0.55, anchor="center")

        self.btn_cadastro = ctk.CTkButton(self.frame_login, width=300, fg_color="green", hover_color="#050", text="Fazer Cadastro".upper(), font=("Century Gothic bold", 14), corner_radius=15, command=self.tela_de_cadastro)
        self.btn_cadastro.place(relx=0.5, rely=0.65, anchor="center")
        
    def tela_de_cadastro(self):
        #Remover o formulario de login
        self.frame_login.place_forget()
    
        #Frame de formulario de cadastro
        self.frame_cadastro = ctk.CTkFrame(self, width=400, height=450)
        self.frame_cadastro.place(relx=0.5, rely=0.5, anchor="center")
    
        #Criando o titulo
        self.lbtitle_cadastro = ctk.CTkLabel(self.frame_cadastro, text="Faça seu Cadastro", font=("Century Gothic bold", 22))
        self.lbtitle_cadastro.place(relx=0.5, rely=0.1, anchor="center")
    
        #Criar widgets da tela de cadastro
        self.username_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Seu nome de usuário...", font=("Century Gothic bold", 16), corner_radius=15, border_color= "#005")
        self.username_cadastro_entry.place(relx=0.5, rely=0.25, anchor="center")
    
        self.email_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Email de usuário...", font=("Century Gothic bold", 16), corner_radius=15, border_color= "#005")
        self.email_cadastro_entry.place(relx=0.5, rely=0.35, anchor="center")

        self.senha_cadastro_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Senha do usuario...", font=("Century Gothic bold", 16), corner_radius=15, border_color= "#005", show="*")
        self.senha_cadastro_entry.place(relx=0.5, rely=0.45, anchor="center")
    
        self.confirma_senha_entry = ctk.CTkEntry(self.frame_cadastro, width=300, placeholder_text="Confirmar a senha de usuário...", font=("Century Gothic bold", 16), corner_radius=15, border_color= "#005", show="*")
        self.confirma_senha_entry.place(relx=0.5, rely=0.55, anchor="center")
    
        self.btn_cadastrar_user = ctk.CTkButton(self.frame_cadastro, width=300, fg_color="green", hover_color="#050", text="Cadastrar".upper(), font=("Century Gothic bold", 16), corner_radius=15, command=self.cadastrar_usuario)
        self.btn_cadastrar_user.place(relx=0.5, rely=0.65, anchor="center")
    
        self.btn_login_back = ctk.CTkButton(self.frame_cadastro, width=30, text="Voltar a Login".upper(), font=("Century Gothic bold", 14), corner_radius=15, fg_color="#444", hover="#333", command=self.voltar_para_login)
        self.btn_login_back.place(relx=0.5, rely=0.75, anchor="center")
        
    def voltar_para_login(self):
        # Limpa o frame de cadastro
        self.frame_cadastro.place_forget()
        # Exibe o frame de login novamente
        self.tela_de_login()
        
    def limpa_entry_cadastro(self):
        self.username_cadastro_entry.delete(0, END)
        self.email_cadastro_entry.delete(0, END)
        self.senha_cadastro_entry.delete(0, END)
        self.confirma_senha_entry.delete(0, END)
        
    def limpa_entry_login(self):
        self.username_login_entry.delete(0, END)
        self.senha_login_entry.delete(0, END)

if __name__ == "__main__":
    app = App()
    app.mainloop()
