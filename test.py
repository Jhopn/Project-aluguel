import tkinter as tk

aberto_cad = 0
janela_cad = None

def fechar_janela_cadastro():
    global janela_cad, aberto_cad

    if janela_cad.winfo_exists():
        janela_cad.destroy()

    aberto_cad = 0

def abrir_janela_cadastro():
    global janela_cad, aberto_cad

    if aberto_cad <= 2:
        if not janela_cad or not janela_cad.winfo_exists():
            janela_cad = tk.Toplevel(raiz)
            janela_cad.title("Janela de Cadastro")
            # Adicione os elementos da janela de cadastro aqui
            # ...

            janela_cad.protocol("WM_DELETE_WINDOW", fechar_janela_cadastro)

        aberto_cad += 1
        janela_cad.wait_window()
    else:
        print("Limite de janelas abertas excedido!")

# Inicialização do Tkinter
raiz = tk.Tk()
raiz.title("Exemplo de Janela de Cadastro")

# Exemplo de botão para abrir a janela de cadastro
botao_abrir = tk.Button(raiz, text="Abrir Cadastro", command=abrir_janela_cadastro)
botao_abrir.pack()

raiz.mainloop()
