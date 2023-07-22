from tkinter import *
import tkinter.messagebox
from tkinter.ttk import *
import datetime
from tkcalendar import Calendar
import os

janela = Tk()
janela.geometry("300x300")
janela.resizable(False,False)
janela.title("Aluguel - Lazer")

painel = PanedWindow(janela)
primeira_tela = Frame(painel)
segunda_tela = Frame(painel)

def cadastrar():
    janela_cad = Toplevel(janela)
    janela_cad.geometry("300x300")
    janela_cad.resizable(False,False)
    janela_cad.title("Aluguel - Lazer")

    # Nome
    entry_nm = Entry(janela_cad)
    entry_nm.place(x=10,y=20)
    # CPF
    entry_cpf = Entry(janela_cad)
    entry_cpf.place(x=10,y=20)
    # Endereço
    entry_end = Entry(janela_cad)
    entry_end.place(x=10,y=20)
    # Telefone
    entry_tel = Entry(janela_cad)
    entry_tel.place(x=10,y=20)

    
    def confirmar():
        nome = entry_nm.get()
        cpf = entry_cpf.get()
        endereco = entry_end.get()
        telefone = entry_tel.get()

        gravar = []
        arquivo = open("cadastro.txt", "a")
        gravar.append("Dados\n")
        gravar.append("\nNome:" +  nome)
        gravar.append("\nCPF" + cpf)
        gravar.append("\nEndereço:" +  endereco)
        gravar.append("\nTelefone:" + telefone)
        gravar.append("-----------------------------------")
       
        arquivo.writelines(gravar)
        arquivo.close()

    #Botões
    botao =Button(janela, text= "Confirmar", command= confirmar)
    botao.place(x=110,y=250)

def cad_area():
    if os.system("dadosarea.txt"):
        janela_ex = Toplevel(janela)
        janela_ex.geometry("300x300")
        janela_ex.resizable(False,False)
        janela_ex.title("Exibir Dados da Área")

    else:
        janela_cad_area = Toplevel(janela)
        janela_cad_area.geometry("300x300")
        janela_cad_area.resizable(False,False)
        janela_cad_area.title("Cadastrar Área")

        # Nome da área
        entry_nm_ar = Entry(janela_cad_area)
        entry_nm_ar.place(x=10,y=20)
        # Endereço da área
        entry_end_ar = Entry(janela_cad_area)
        entry_end_ar.place(x=10,y=20)
        # Valor da área
        entry_valor = Entry(janela_cad_area)
        entry_valor.place(x=10,y=20)

        def confirmar():
            nome = entry_nm_ar.get()
            endereco = entry_end_ar.get()
            valor = entry_valor.get()

            gravar = []
            arquivo = open("dadosarea.txt", "a")
            gravar.append("Dados\n")
            gravar.append("\nNome da Área:" +  nome)
            gravar.append("\nEndereço da Área:" + endereco)
            gravar.append("\nPreço do Aluguel:" +  valor)
            gravar.append("-----------------------------------")
            arquivo.writelines(gravar)
            arquivo.close()

        #Botões
        botao =Button(janela, text= "Confirmar", command= confirmar)
        botao.place(x=110,y=250)



def alugar():
    if os.system("cadastro.txt"):
        janela_alugar = Toplevel(janela)
        janela_alugar.geometry("300x300")
        janela_alugar.resizable(False,False)
        janela_alugar.title("Aluguel - Lazer")

        # Deixar o calendario att
        data_atual = datetime.datetime.now()
        ano = data_atual.year
        mes = data_atual.month
        dia = data_atual.day

        # Listar Clientes
        listar_clientes = Listbox(janela_alugar)
        listar_clientes.place(x=10,y=20)

        # Busca
        busca = Entry(janela_alugar)
        busca.place(x=280,y=10)

        calendario = Calendar(janela_alugar, selectmode = 'day',year = ano, month = mes,day = dia)
        calendario.place(x=10,y=20)

        def alugar_ar():
            data = "Data Alugada: " + calendario.get_date()
            nome = listar_clientes.get(ANCHOR)
            gravar = []
            arquivo = open("aluguel.txt", "a")
            gravar.append("| Aluguel |\n")
            gravar.append("\nNome:" +  nome)
            gravar.append("\n" + data)
            gravar.append("-----------------------------------")
            arquivo.writelines(gravar)
            arquivo.close()

        #Botões
        botao =Button(janela, text= "Alugar", command= alugar_ar)
        botao.place(x=110,y=250)

    else:


def relacao():
    janela_rela = Toplevel(janela)
    janela_rela.geometry("300x300")
    janela_rela.resizable(False,False)
    janela_rela.title("Aluguel - Lazer")
def relatorio():
    janela_relat = Toplevel(janela)
    janela_relat.geometry("300x300")
    janela_relat.resizable(False,False)
    janela_relat.title("Aluguel - Lazer")


# Botão
botao =Button(janela, text= "Cadastrar", command= cadastrar)
botao.place(x=110,y=250)

botao =Button(janela, text= "Cadastrar a Área", command= cad_area)
botao.place(x=110,y=250)

botao =Button(janela, text= "Alugar", command= alugar)
botao.place(x=110,y=250)

botao =Button(janela, text= "Relação da Área", command= relacao)
botao.place(x=110,y=250)

botao =Button(janela, text= "Relátorio Clientes", command= relatorio)
botao.place(x=110,y=250)


janela.mainloop()