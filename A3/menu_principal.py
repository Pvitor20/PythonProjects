# menu_principal.py
from tkinter import *
from tkinter import messagebox, filedialog
import database
from datetime import datetime

def exibir_menu_principal(user_id):
    janela = Toplevel()  # Cria uma nova janela, sem bloquear o loop principal
    janela.title("Relato Popular - Menu Principal")
    janela.geometry("400x500")

    # Funções da interface gráfica
    def open_nova_denuncia():
        tela_menu.pack_forget()
        tela_nova_denuncia.pack(fill="both", expand=True)

    def open_acompanhar_denuncias():
        tela_menu.pack_forget()
        carregar_denuncias()
        tela_acompanhar_denuncias.pack(fill="both", expand=True)

    def voltar_menu():
        tela_nova_denuncia.pack_forget()
        tela_acompanhar_denuncias.pack_forget()
        tela_menu.pack(fill="both", expand=True)

    def carregar_denuncias():
        # Limpar a área de exibição de denúncias anteriores
        for widget in frame_denuncias.winfo_children():
            widget.destroy()

        denuncias = database.listar_denuncias(user_id)
        for denuncia in denuncias:
            data_hora, localizacao, texto, resolvido = denuncia
            status = "Resolvido" if resolvido else "Pendente"
            Label(frame_denuncias, text=f"{data_hora} - {localizacao}\nStatus: {status}\n\n{texto}", 
                  wraplength=280, relief="solid", padx=10, pady=10).pack(pady=5)

    def selecionar_foto():
        global foto_path
        foto_path = filedialog.askopenfilename(title="Selecionar uma imagem",
                                               filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if foto_path:
            messagebox.showinfo("Imagem selecionada", f"Imagem selecionada: {foto_path.split('/')[-1]}")

    def salvar_denuncia():
        localizacao = entry_localizacao.get()
        denuncia_texto = entry_denuncia.get("1.0", END).strip()
        
        if not localizacao or not denuncia_texto:
            messagebox.showerror("Erro", "Por favor, preencha os campos obrigatórios.")
            return
        
        database.registrar_denuncia(user_id, localizacao, denuncia_texto, foto_path)
        messagebox.showinfo("Sucesso", "Denúncia registrada com sucesso!")
        voltar_menu()

    # Tela do Menu Principal
    tela_menu = Frame(janela)
    Label(tela_menu, text="Menu Principal", font=("Arial", 16)).pack(pady=10)

    botao_nova_denuncia = Button(tela_menu, text="Nova Denúncia", command=open_nova_denuncia)
    botao_nova_denuncia.pack(pady=10)

    botao_acompanhar_denuncias = Button(tela_menu, text="Acompanhar Denúncias", command=open_acompanhar_denuncias)
    botao_acompanhar_denuncias.pack(pady=10)

    # Tela de Nova Denúncia
    tela_nova_denuncia = Frame(janela)
    Label(tela_nova_denuncia, text="Nova Denúncia", font=("Arial", 16)).pack(pady=10)

    Label(tela_nova_denuncia, text="Localização:").pack()
    entry_localizacao = Entry(tela_nova_denuncia, width=50)
    entry_localizacao.pack(pady=5)

    Label(tela_nova_denuncia, text="Denúncia:").pack()
    entry_denuncia = Text(tela_nova_denuncia, width=50, height=10)
    entry_denuncia.pack(pady=5)

    botao_selecionar_foto = Button(tela_nova_denuncia, text="Selecionar Foto (Opcional)", command=selecionar_foto)
    botao_selecionar_foto.pack(pady=5)

    botao_salvar = Button(tela_nova_denuncia, text="Salvar", command=salvar_denuncia)
    botao_salvar.pack(pady=10)

    botao_voltar = Button(tela_nova_denuncia, text="Voltar", command=voltar_menu)
    botao_voltar.pack(pady=5)

    # Tela de Acompanhamento de Denúncias
    tela_acompanhar_denuncias = Frame(janela)
    Label(tela_acompanhar_denuncias, text="Minhas Denúncias", font=("Arial", 16)).pack(pady=10)

    frame_denuncias = Frame(tela_acompanhar_denuncias)
    frame_denuncias.pack(pady=10)

    botao_voltar_acompanhar = Button(tela_acompanhar_denuncias, text="Voltar", command=voltar_menu)
    botao_voltar_acompanhar.pack(pady=10)

    # Exibe a tela do menu principal
    tela_menu.pack(fill="both", expand=True)
