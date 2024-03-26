import customtkinter as ctk
from tkinter import PhotoImage

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configuracoes_da_janela_inicial()
        self.tela_de_login()
    
    # Configurando a janela principal    
    def configuracoes_da_janela_inicial(self):
        self.geometry("700x400")
        self.title("Tela de Login")
        self.resizable(False, False)    

    def tela_de_login(self):
        # Trabalhando com as imagens
        self.img = PhotoImage(file="login.png")
        self.img = self.img.subsample(6,6)
        self.lb_img = ctk.CTkLabel(self, image=self.img)
        self.lb_img.grid(row=1, column=0, padx=10)
        
        # Titulo da Plataforma
        self.title = ctk.CTkLabel(self, text="Faça o seu login ou Cadastre! \nPara ter acesso na plataforma", font=("Century Gothic bold", 14))
        self.title.grid(row=0, column=0, pady=10, padx=10)
        
        # Criar a frame do formulario de login
        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=350, y=10)
  
        # Colocando widget dentro do frame - formulario de login
        self.lbtitle = ctk.CTkLabel(self.frame_login, text="Faça seu Login", font=("Century Gothic bold", 22))
        self.lbtitle.grid(row=0, column=0, padx=10, pady=10)
        
        self.username_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Seu nome de usuário...", font=("Century Gothic bold", 16), corner_radius=15, border_color= "#005")
        self.username_login_entry.grid(row=1, column=0, pady=10, padx=10)
  
        self.senha_login_entry = ctk.CTkEntry(self.frame_login, width=300, placeholder_text="Seu nome de usuário...", font=("Century Gothic bold", 16), corner_radius=15, border_color= "#005")
        self.senha_login_entry.grid(row=2, column=0, pady=10, padx=10)
    
        self.ver_senha = ctk.CTkCheckBox(self.frame_login, text="Clique para ver a senha", font=("Century Gothic bold", 12), corner_radius=20)
        self.ver_senha.grid(row=3, column=0, pady=10, padx=10)
        
        self.btn_login = ctk.CTkButton(self.frame_login, width=30, text="Fazer Login".upper(), font=("Century Gothic bold", 16), corner_radius=15)
        self.btn_login.grid(row=4, column=0, pady=10, padx=10)
        
        self.span = ctk.CTkLabel(self.frame_login, text="Se você não tem conta,\nclique no botão abaixo para cadastrar!", font=("Century Gothic", 10))
        self.span.grid(row=5, column=0, pady=10, padx=10)

        self.btn_cadastro = ctk.CTkButton(self.frame_login, width=300, fg_color="green", hover_color="#050", text="Fazer Cadastro".upper(), font=("Century Gothic bold", 16))
        self.btn_cadastro.grid(row=6, column=0, pady=10, padx=10)
        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
