import customtkinter as ctk



class App(ctk.CTk):
    def __init__(self):
        self.configuracoes_da_janela_inicial()
        super().__init__()
    
    #configurando a janela principal    
    def configuracoes_da_janela_inicial(self):
        self.geometry("700x400")
        self.title("Tela de Login")
        self.resizable(False, False)    



if __name__ =="__main__":
    app = App()
    app.mainloop()