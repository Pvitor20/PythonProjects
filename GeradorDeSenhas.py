import random

class Gerador:
    def __init__(self, chars=None, tamanho=1, quantidade=1):
        if chars is None:
            self.chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]}{|;:',.<>?/1234567890`~"
        else:
            self.chars = chars
        self.tamanho = tamanho
        self.quantidade = quantidade
    
    def selecionar_tamanho(self):
        try:
            self.tamanho = int(input("Informe a quantidade de caracteres: "))
        except ValueError:
            print("Por favor, insira um número válido.")
        self.menu()
    
    def selecionar_quantidade(self):
        try:
            self.quantidade = int(input("Informe a quantidade de senhas: "))
        except ValueError:
            print("Por favor, insira um número válido.")
        self.menu()

    def gerar_senhas(self):
        print("Aqui estão as suas senhas:")
        for _ in range(self.quantidade):
            password = ''.join(random.choice(self.chars) for _ in range(self.tamanho))
            print(password)
        self.menu()
    
    def menu(self):
        while True:
            print("\nGerador de Senhas")
            print("=================")
            print("""
            ================ MENU ================
      
            [1] Gerar Senha
            [2] Definir tamanho
            [3] Definir quantidade de senhas
            [0] Sair
            """)
            try:
                choice = int(input("Escolha uma opção: "))
                if choice == 1:
                    self.gerar_senhas()
                elif choice == 2:
                    self.selecionar_tamanho()
                elif choice == 3:
                    self.selecionar_quantidade()
                elif choice == 0:
                    print("Saindo...")
                    break

                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Por favor, insira um número válido.")
                

# Inicia o programa
app = Gerador()
app.menu()





