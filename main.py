from tkinter import *
import tkinter.messagebox
from tkinter.ttk import *
from datetime import datetime
from tkcalendar import Calendar
from PIL import Image, ImageTk
import requests
from io import BytesIO
import os

janela = Tk()
janela.geometry("300x400")
janela.resizable(False,False)
janela.title("Aluguel - Lazer")
cinza_escuro = "#576665"
cinza_claro = "#7E8890"

# Variaveis globais de controle
aberto_cad = 0
janela_cad = None

aberto_cad_area = 0
janela_cad_area = None

aberto_alugar = 0
janela_alugar = None

aberto_ex = 0
janela_ex = None

aberto_relat = 0 
janela_relat = None

aberto_ad = 0
janela_ad = None

aberto_ad_ap = 0
janela_ad_ap = None

aberto_ad_apc = 0
janela_ad_apc = None

# Desing
quadrado = Canvas(janela, width=310, height=410, background= cinza_escuro)
quadrado.create_rectangle(15, 15, 295, 395, fill= cinza_claro)
quadrado.place(x=-5,y=-5)


def fechar_janela_cadastro():
    global janela_cad, aberto_cad

    if janela_cad.winfo_exists():
        janela_cad.destroy()
    aberto_cad = 0

def cadastrar():
    global janela_cad, aberto_cad

    if aberto_cad <= 2:
        if not janela_cad or not janela_cad.winfo_exists():
            janela_cad = Toplevel(janela)
            janela_cad.geometry("300x380")
            janela_cad.resizable(False,False)
            janela_cad.title("Cadastro")
            janela_cad.configure( background= cinza_escuro)
            checargnr = StringVar()

            # Desing
            quadrado = Canvas(janela_cad, width=220, height=270, background= cinza_escuro)
            quadrado.create_rectangle(10, 10, 210, 260, fill= cinza_claro)
            quadrado.place(x=40,y=40)

            # Titulo
            label = Label(janela_cad, text="                                                                                                      ", font= "Arial, 15", background= cinza_claro)
            label.place(x=-5,y=10)

            label = Label(janela_cad, text="Cadastro", font= "Arial, 15", background= cinza_claro)
            label.place(x=110,y=10)
                
            # Nome
            label = Label(janela_cad, text="Nome: ", background= cinza_claro)
            label.place(x=60,y=60)
            entry_nm = Entry(janela_cad, width= 22)
            entry_nm.place(x=102,y=60)
            # CPF
            label = Label(janela_cad, text="CPF: ", background= cinza_claro)
            label.place(x=60,y=100)
            entry_cpf = Entry(janela_cad, width= 24)
            entry_cpf.place(x=91,y=100)
            # Endereço
            label = Label(janela_cad, text="Endereço: ", background= cinza_claro)
            label.place(x=60,y=140)
            entry_end = Entry(janela_cad)
            entry_end.place(x=115,y=140)
            # Telefone
            label = Label(janela_cad, text="Telefone: ", background= cinza_claro)
            label.place(x=60,y=180)
            entry_tel = Entry(janela_cad)
            entry_tel.place(x=115,y=180)

            # Genêro
            label = Label(janela_cad, text="Genêro: ", background= cinza_claro)
            label.place(x=60,y=240)

            # Radiobuttons
            radio1 = Radiobutton(janela_cad, value = "Feminino", var = checargnr)
            radio1.place(x=115, y=210)
            label = Label(janela_cad, text="Feminino", background= cinza_claro)
            label.place(x=140,y=210)

            radio2 = Radiobutton(janela_cad, value = "Masculino", var= checargnr)
            radio2.place(x=115, y=240)
            label = Label(janela_cad, text="Masculino", background= cinza_claro)
            label.place(x=140,y=240)

            radio3 = Radiobutton(janela_cad, value = "Outro", var = checargnr)
            radio3.place(x=115, y=270)
            label = Label(janela_cad, text="Outro", background= cinza_claro)
            label.place(x=140,y=270)


                
            def confirmar():
                nome = entry_nm.get()
                nome = nome.upper()
                cpf = entry_cpf.get()
                endereco = entry_end.get()
                endereco = endereco.upper()
                telefone = entry_tel.get()
                genero = checargnr.get()
                # Testando se o nome possuí caracter no nome
                resultado = any(caractere.isdigit() for caractere in nome)
                # Testando se possuí letras em telefone
                resultado_2 = any(caractere.isalpha() for caractere in telefone)
                
                if nome == "" or cpf == "" or endereco == "" or telefone == "" or genero == "":
                    tkinter.messagebox.showerror("Aviso", "Reveja os dados do cadastro!")

                elif len(cpf) != 11:
                    tkinter.messagebox.showerror("Aviso", "CPF inválido!")

                elif len(telefone) != 9:
                    tkinter.messagebox.showerror("Aviso", "Número inválido!")

                elif resultado == True:
                    tkinter.messagebox.showerror("Aviso", "O nome possuí números!")

                elif resultado_2 == True:
                    tkinter.messagebox.showerror("Aviso", "O telefone possuí letras!")

                else:
                    gravar = []
                    arquivo = open("cadastro.txt", "a")
                    gravar.append("\nDados\n")
                    gravar.append("\nNome: " +  nome)
                    gravar.append("\nCPF: " + cpf)
                    gravar.append("\nEndereço: " +  endereco)
                    gravar.append("\nTelefone: " + telefone)
                    gravar.append("\nGenêro: "+ genero)
                    gravar.append("\n-----------------------------------")
                    arquivo.writelines(gravar)
                    arquivo.close()
                    tkinter.messagebox.showinfo("Aviso","Cadastro realizado!")
                    # Apagar dados confirmados
                    entry_nm.delete(0, END)
                    entry_cpf.delete(0, END)
                    entry_end.delete(0, END)
                    entry_tel.delete(0, END)

                #Botões
            botao =Button(janela_cad, text= "Confirmar", command= confirmar)
            botao.place(x=110,y=330)

            janela_cad.protocol("WM_DELETE_WINDOW", fechar_janela_cadastro)

        aberto_cad += 1
        janela_cad.wait_window()

def fechar_janela_cad_area():
    global janela_cad_area, aberto_cad_area

    if janela_cad_area.winfo_exists():
        janela_cad_area.destroy()
    aberto_cad_area = 0
    
def cad_area():
    global janela_cad_area, aberto_cad_area

    if aberto_cad_area <= 2:
        if not janela_cad_area or not janela_cad_area.winfo_exists():
            if os.path.isfile("dadosarea.txt"):
                tkinter.messagebox.showinfo("Aviso","Cadastro já foi realizado!")
            else:
                janela_cad_area = Toplevel(janela)
                janela_cad_area.geometry("300x240")
                janela_cad_area.resizable(False,False)
                janela_cad_area.title("Cadastrar Área")
                janela_cad_area.configure( background= cinza_escuro)

                # Desing
                quadrado = Canvas(janela_cad_area, width=285, height=140, background= cinza_escuro)
                quadrado.create_rectangle(10, 10, 275, 130, fill= cinza_claro)
                quadrado.place(x=5,y=40)

                # Titulo
                label = Label(janela_cad_area, text="                                                                                                      ", font= "Arial, 15", background= cinza_claro)
                label.place(x=-5,y=10)

                label = Label(janela_cad_area, text="Cadastro Área", font= "Arial, 15", background= cinza_claro)
                label.place(x=80,y=10)

                # Nome da área
                label = Label(janela_cad_area, text="Nome da área: ", background= cinza_claro)
                label.place(x=20,y=60)
                entry_nm_ar = Entry(janela_cad_area, width= 26)
                entry_nm_ar.place(x=105,y=60)

                # Endereço da área
                label = Label(janela_cad_area, text="Endereço da área: ", background= cinza_claro)
                label.place(x=20,y=100)
                entry_end_ar = Entry(janela_cad_area, width= 24)
                entry_end_ar.place(x=116,y=100)

                # Valor da área
                label = Label(janela_cad_area, text="Valor da área R$: ", background= cinza_claro)
                label.place(x=20,y=140)
                entry_valor = Entry(janela_cad_area, width= 25)
                entry_valor.place(x=110,y=140)

                def confirmar():
                    nome = entry_nm_ar.get()
                    endereco = entry_end_ar.get()
                    valor = entry_valor.get()

                    if nome == "" or endereco == "" or valor == "":
                        tkinter.messagebox.showerror("Aviso", "Reveja os dados do cadastro!")
                    else:
                        gravar = []
                        arquivo = open("dadosarea.txt", "a")
                        gravar.append("Dados\n")
                        gravar.append("\nNome da Área: " +  nome)
                        gravar.append("\nEndereço da Área: " + endereco)
                        gravar.append("\nPreço do Aluguel R$: " +  valor)
                        arquivo.writelines(gravar)
                        arquivo.close()
                        tkinter.messagebox.showinfo("Aviso","Cadastro da área realizado!")
                        janela_cad_area.destroy()
                    

                #Botões
                botao =Button(janela_cad_area, text= "Confirmar", command= confirmar)
                botao.place(x=110,y=200)
                janela_cad_area.protocol("WM_DELETE_WINDOW", fechar_janela_cad_area)

            aberto_cad_area += 1
            janela_cad_area.wait_window()

def fechar_janela_alugar():
    global janela_alugar, aberto_alugar

    if janela_alugar.winfo_exists():
        janela_alugar.destroy()
    aberto_alugar = 0

def alugar():
    global janela_alugar, aberto_alugar

    if aberto_cad_area <= 2:
        if not janela_alugar or not janela_alugar.winfo_exists():
            if os.path.isfile("cadastro.txt"):
                janela_alugar = Toplevel(janela)
                janela_alugar.geometry("495x380")
                janela_alugar.resizable(False,False)
                janela_alugar.title("Aluguel")
                janela_alugar.configure(background= cinza_escuro)
                checar_cadeira = StringVar()
                checar_cozinha = StringVar()

                # Desing
                quadrado = Canvas(janela_alugar, width=480, height=280, background= cinza_escuro)
                quadrado.create_rectangle(10, 10, 470, 270, fill= cinza_claro)
                quadrado.place(x=5,y=40)

                # Titulo
                label = Label(janela_alugar, text="                                                                                                      ", font= "Arial, 15", background= cinza_claro)
                label.place(x=-5,y=10)

                label = Label(janela_alugar, text="Alugar", font= "Arial, 15", background= cinza_claro)
                label.place(x=220,y=10)
                
                # Deixar o calendario att
                data_atual = datetime.now()
                ano = data_atual.year
                mes = data_atual.month
                dia = data_atual.day

                # Listar Clientes
                listar_clientes = Listbox(janela_alugar, width= 30)
                listar_clientes.place(x=280,y=90)

                # Carregar nomes dos clientes
                arquivo = open("cadastro.txt", "r")
                for linha in arquivo:
                    if "Nome:" in linha:
                        nome = linha
                        nome = nome[5:]
                        listar_clientes.insert(END,nome)
                arquivo.close()

                # Busca
                label = Label(janela_alugar, text= "Pesquise:", background= cinza_claro)
                label.place(x=280,y=60)

                busca = Entry(janela_alugar)
                busca.place(x=338,y=60) 

                # Horario do aluguel
                label = Label(janela_alugar, text= "Horário: ", background= cinza_claro)
                label.place(x=20,y=270)

                label = Label(janela_alugar, text= "Início", background= cinza_claro)
                label.place(x=90,y=250)
                combo_in = Combobox(janela_alugar, width= 5)
                horarios = [
                "00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30",
                "04:00", "04:30", "05:00", "05:30", "06:00", "06:30", "07:00", "07:30",
                "08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
                "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30",
                "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30",
                "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00", "23:30"]
                combo_in['values'] = (horarios)
                combo_in.current(0)
                combo_in.place(x=80,y=270)


                label = Label(janela_alugar, text= "Término", background= cinza_claro)
                label.place(x=162,y=250)
                combo_fm = Combobox(janela_alugar, width= 5)
                combo_fm['values'] = (horarios)
                combo_fm.current(0)
                combo_fm.place(x=160,y=270)

                # Cadeiras e  Cozinha
                label = Label(janela_alugar, text= "Incluso: ", background= cinza_claro)
                label.place(x=260,y=270)
                
                check1 = Checkbutton(janela_alugar, var= checar_cadeira , onvalue="Com cadeira", offvalue="Sem cadeira")
                check1.place(x=310,y=270)
                label = Label(janela_alugar, text= "Cadeira", background= cinza_claro)
                label.place(x=333,y=270)

                check2 = Checkbutton(janela_alugar, var= checar_cozinha , onvalue="Com cozinha", offvalue="Sem cozinha")
                check2.place(x=380,y=270)
                label = Label(janela_alugar, text= "Cozinha", background= cinza_claro)
                label.place(x=410,y=270)

                def pesquisar():
                    pesquisa = busca.get()
                    pesquisa = pesquisa.upper()

                    arquivo = open("cadastro.txt", "r")
                    for linha in arquivo:
                        if pesquisa in linha and "Nome:" in linha:
                            # Limpa a listbox
                            listar_clientes.delete(0, END)
                            # Dado da pesquisa
                            listar_clientes.insert(END, linha[5:])
                    arquivo.close()

                    if  pesquisa == "":
                        # Limpa a listbox
                        listar_clientes.delete(0, END)
                        # Carregar nomes dos clientes
                        arquivo = open("cadastro.txt", "r")
                        for linha in arquivo:
                            if "Nome:" in linha:
                                nome = linha
                                nome = nome[5:]
                                listar_clientes.insert(END,nome)
                        arquivo.close()
                    
                busca.bind('<KeyRelease>', lambda event: pesquisar())

                calendario = Calendar(janela_alugar, selectmode = 'day',year = ano, month = mes,day = dia)
                calendario.place(x=20,y=60)

                # carregar alugueis e deixar o calendario marcado 
                if os.path.isfile("aluguel.txt"):
                    arquivo = open("aluguel.txt", "r")
                    for linha in arquivo:
                        if "Data Alugada:" in linha:

                            dia_al = linha[14:16]
                            dia_al = int(dia_al)

                            mes_al = linha[17:19]
                            mes_al = int(mes_al)

                            ano_al = linha[20:24]
                            ano_al = int(ano_al)

                            data = f"{dia_al}/{mes_al}/{ano_al}"
                            # Tranforma variavel str em datetime
                            data_time = datetime.strptime(data, "%d/%m/%Y").date()
                            # Cria um evento no calendario
                            calendario.calevent_create(data_time, "Evento", "marcado")
                            # Configura a cor do evento
                            calendario.tag_config("marcado", background= "red", foreground="black")

                    arquivo.close()
                    

                def alugar_ar():
                    nome = listar_clientes.get(ANCHOR)

                    if nome == "":
                        tkinter.messagebox.showerror("Aviso","Nenhum cliente selecionado!")

                    else:
                        gravar = []
                        arquivo = open("aluguel.txt", "a")
                        gravar.append("\nCliente: " +  nome)
                        gravar.append("Data Alugada: " + calendario.get_date())
                        gravar.append("\nHorário de Inicio: " + combo_in.get())
                        gravar.append("\nHorário de Término: " + combo_fm.get())
                        cadeira = checar_cadeira.get()
                        if cadeira == "":
                            cadeira = "Sem cadeira"
                        gravar.append("\nSituação Cadeiras: " + cadeira)
                        cozinha = checar_cozinha.get()
                        if cozinha == "":
                            cozinha = "Sem cozinha"
                        gravar.append("\nSituação Cozinha: " + cozinha) 
                        arquivo.writelines(gravar)
                        arquivo.close()
                        tkinter.messagebox.showinfo("Aviso","Alugado com sucesso!")

                #Botões
                botao =Button(janela_alugar, text= "Alugar", command= alugar_ar)
                botao.place(x=210,y=330)
                janela_alugar.protocol("WM_DELETE_WINDOW", fechar_janela_alugar)

            
            else:
                tkinter.messagebox.showinfo("Aviso","Nenhum cadastro realizado criado!")

            aberto_alugar += 1
            janela_alugar.wait_window()

def fechar_janela_ex():
    global janela_ex, aberto_ex

    if janela_ex.winfo_exists():
        janela_ex.destroy()
    aberto_ex = 0

def relacao():
    global janela_ex, aberto_ex
    
    if aberto_ex <= 2:
        if not janela_ex or not janela_ex.winfo_exists():
            if os.path.isfile("dadosarea.txt"):
                janela_ex = Toplevel(janela)
                janela_ex.geometry("350x400")
                janela_ex.resizable(False,False)
                janela_ex.title("Exibir Dados da Área")
                janela_ex.configure( background= cinza_escuro)

                dados = []
                arquivo = open("dadosarea.txt", "r")
                for linha in arquivo:
                    if "Nome da Área:" in linha:
                        dados.append(linha)
                    elif "Endereço da Área:" in linha:
                        dados.append(linha)
                    elif "Preço do Aluguel R$" in linha:
                        dados.append(linha)
                arquivo.close()
                

                # Desing
                quadrado = Canvas(janela_ex, width=340, height=300, background= cinza_escuro)
                quadrado.create_rectangle(10, 10, 330, 290, fill= cinza_claro)
                quadrado.place(x=3,y=40)

                # Titulo
                label = Label(janela_ex, text="                                                                                                      ", font= "Arial, 15", background= cinza_claro)
                label.place(x=-5,y=10)
                label = Label(janela_ex, text= "Dados da Área", font= "Arial, 15", background= cinza_claro)
                label.place(x=110,y=10)

                label = Label(janela_ex, text= dados[0], background= cinza_claro)
                label.place(x=20,y=60)

                label = Label(janela_ex, text= dados[1], background= cinza_claro)
                label.place(x=20,y=80)

                label = Label(janela_ex, text= dados[2], background= cinza_claro)
                label.place(x=20,y=100)

                listar_clientes = Listbox(janela_ex, width= 50, height= 10)
                listar_clientes.place(x=22,y=160)

                arquivo = open("aluguel.txt", "r")
                for linha in arquivo:
                    if "Cliente:" in linha:
                        listar_clientes.insert(END, "\n------------")
                        listar_clientes.insert(END, linha)
                    elif "Data Alugada:" in linha:
                        listar_clientes.insert(END, linha)
                    elif "Horário de Inicio:" in linha:
                        listar_clientes.insert(END, linha)
                    elif "Horário de Término:" in linha:
                        listar_clientes.insert(END, linha)
                    elif "Situação Cadeiras:" in linha:
                        listar_clientes.insert(END, linha)
                    elif "Situação Cozinha:" in linha:
                        listar_clientes.insert(END, linha)
                arquivo.close()

                # Pesquisa
                label = Label(janela_ex, text= "Pesquise:", background= cinza_claro)
                label.place(x=70,y=130)
                busca = Entry(janela_ex)
                busca.place(x=130,y=130)

                def pesquisar():
                        pesquisa = busca.get()
                        pesquisa = pesquisa.upper()
                        arquivo = open("aluguel.txt", "r")
                        achou = False
                        # Limpa a listbox
                        listar_clientes.delete(0, END)
                        for linha in arquivo:
                            if pesquisa in linha and "Cliente:" in linha:
                                listar_clientes.insert(END, "\n------------")
                                listar_clientes.insert(END, linha)
                                achou = True
                            elif achou == True and "Data Alugada:" in linha:
                                listar_clientes.insert(END, linha)
                            elif achou == True and "Horário de Inicio:" in linha:
                                listar_clientes.insert(END, linha)
                            elif achou == True and "Horário de Término:" in linha:
                                listar_clientes.insert(END, linha)
                            elif achou == True and "Situação Cadeiras:" in linha:
                                listar_clientes.insert(END, linha)
                            elif achou == True and "Situação Cozinha:" in linha:
                                listar_clientes.insert(END, linha)
                                achou = False
                        arquivo.close()

                        if  pesquisa == "":
                            # Limpa a listbox
                            listar_clientes.delete(0, END)
                            # Carregar nomes dos clientes
                            arquivo = open("aluguel.txt", "r")
                            for linha in arquivo:
                                if "Cliente:" in linha:
                                    listar_clientes.insert(END, "\n------------")
                                    listar_clientes.insert(END,linha)
                                elif "Data Alugada:" in linha:
                                    listar_clientes.insert(END,linha)
                                elif "Horário de Inicio:" in linha:
                                    listar_clientes.insert(END, linha)
                                elif "Horário de Término:" in linha:
                                    listar_clientes.insert(END, linha)
                                elif "Situação Cadeiras:" in linha:
                                    listar_clientes.insert(END, linha)
                                elif "Situação Cozinha:" in linha:
                                    listar_clientes.insert(END, linha)
                            arquivo.close()
                        
                busca.bind('<KeyRelease>', lambda event: pesquisar())

                def apagar_aluguel():
                    nome = listar_clientes.get(ANCHOR)
                    if "Cliente:" not in nome:
                        tkinter.messagebox.showerror("Aviso", "Selecione o nome do cliente que deseja cancelar o aluguel!")
                    
                    else:
                        dados = []
                        achou = FALSE
                        arquivo = open("aluguel.txt", "r")

                        for linha in arquivo:
                            dados.append(linha)
                            if nome in linha:
                                dados.remove(linha)
                                achou = True
                            elif achou == True and 'Data Alugada:' in linha:
                                dados.remove(linha)
                        
                            elif achou == True and "Horário de Inicio:" in linha:
                                dados.remove(linha)
                                
                            elif achou == True and 'Horário de Término:' in linha:
                                dados.remove(linha)
                    
                            elif achou == True and 'Situação Cadeiras:' in linha:
                                dados.remove(linha)
                            
                            elif achou == True and 'Situação Cozinha:' in linha:
                                dados.remove(linha)
                            
                            elif linha =='\n':
                                dados.remove(linha)
                                achou = False
                        print(dados)
                        arquivo.close()
                        os.remove("aluguel.txt")
                        arquivo = open("aluguel.txt", "a")
                        arquivo.writelines(dados)
                        arquivo.close()
                        tkinter.messagebox.showinfo("Aviso","Dado apagado!")

                botao =Button(janela_ex, text= "-    Apagar    -\nCadastro Área", command= apagar)
                botao.place(x=230,y=70)

                botao =Button(janela_ex, text= "Apagar Aluguel", command= apagar_aluguel)
                botao.place(x=130,y=360)

                janela_ex.protocol("WM_DELETE_WINDOW", fechar_janela_ex)

            else:
                tkinter.messagebox.showerror("Aviso","Cadastro da área não foi realizado!")
            
            aberto_ex += 1
            janela_ex.wait_window()

def fechar_janela_relatorio():
    global janela_relat, aberto_relat

    if janela_relat.winfo_exists():
        janela_relat.destroy()
    aberto_relat = 0            
    
def relatorio():
    global janela_relat, aberto_relat

    if aberto_relat <= 2:
        if not janela_relat or not janela_relat.winfo_exists():
            if os.path.isfile("cadastro.txt"):
                janela_relat = Toplevel(janela)
                janela_relat.geometry("300x390")
                janela_relat.resizable(False,False)
                janela_relat.title("Relatorio")
                janela_relat.configure( background= cinza_escuro)

                # Desing
                quadrado = Canvas(janela_relat, width=290, height=310, background= cinza_escuro)
                quadrado.create_rectangle(10, 10, 280, 300, fill= cinza_claro)
                quadrado.place(x=4, y=5)

                #listbox
                listar_clientes = Listbox(janela_relat, width= 42, height= 14)
                listar_clientes.place(x=22,y=65)

                # Carregar nomes dos clientes
                arquivo = open("cadastro.txt", "r")
                for linha in arquivo:
                    if "Nome:" in linha:
                        nome = linha
                        nome = nome[5:]
                        listar_clientes.insert(END,nome)
                arquivo.close()

                # Pesquisa
                label = Label(janela_relat, text= "Pesquise:", background= cinza_claro)
                label.place(x=70,y=30)
                busca = Entry(janela_relat)
                busca.place(x=130,y=30)

                def pesquisar():
                        pesquisa = busca.get()
                        pesquisa = pesquisa.upper()

                        arquivo = open("cadastro.txt", "r")
                        for linha in arquivo:
                            if pesquisa in linha and "Nome:" in linha:
                                # Limpa a listbox
                                listar_clientes.delete(0, END)
                                # Dado da pesquisa
                                listar_clientes.insert(END, linha[5:])
                        arquivo.close()

                        if  pesquisa == "":
                            # Limpa a listbox
                            listar_clientes.delete(0, END)
                            # Carregar nomes dos clientes
                            arquivo = open("cadastro.txt", "r")
                            for linha in arquivo:
                                if "Nome:" in linha:
                                    nome = linha
                                    nome = nome[5:]
                                    listar_clientes.insert(END,nome)
                            arquivo.close()
                        
                busca.bind('<KeyRelease>', lambda event: pesquisar())

                def ver_dados():
                    janela_relat.geometry("200x200")
                    arquivo = open("cadastro.txt", "r")
                    dados = []
                    corrente = 0
                    for linha in arquivo:
                        if listar_clientes.get(ANCHOR) in linha:
                            corrente = 1
                            dados.append(linha)
                        elif "CPF:" in linha and corrente == 1:
                            dados.append(linha)
                        elif "Endereço:" in linha and corrente == 1:
                            dados.append(linha)
                        elif "Telefone:" in linha and corrente == 1:
                            dados.append(linha)
                        elif "Genêro:" in linha and corrente == 1:
                            dados.append(linha)
                            break
                    arquivo.close()

                
                    label = Label(janela_relat,text= dados[0])
                    label.pack(fill = BOTH, expand = False)

                    label = Label(janela_relat,text= dados[1])
                    label.pack(fill = BOTH, expand = False)

                    label = Label(janela_relat,text= dados[2])
                    label.pack(fill = BOTH, expand = False)

                    label = Label(janela_relat,text= dados[3])
                    label.pack(fill = BOTH, expand = False)

                    label = Label(janela_relat,text= dados[4])
                    label.pack(fill = BOTH, expand = False)


                    def voltar():
                        janela_relat.destroy()
                        relatorio()

                    # Botões
                    botao = Button(janela_relat, text= "Voltar", command= voltar)
                    botao.pack(fill = BOTH, expand = True)
                        
                # Botões
                botao =Button(janela_relat, text= "Ver", command= ver_dados)
                botao.place(x=60,y=340)

                botao =Button(janela_relat, text= "Excluír", command= apagar_cadastros)
                botao.place(x=160,y=340)
                janela_relat.protocol("WM_DELETE_WINDOW", fechar_janela_relatorio)

            
            else:
                tkinter.messagebox.showerror("Aviso","Nenhum cadastro realizado!")
            
            aberto_relat += 1
            janela_relat.wait_window()

def fechar_janela_adm():
    global janela_ad, aberto_ad

    if janela_ad.winfo_exists():
        janela_ad.destroy()
    aberto_ad = 0      

def adm():
    global janela_ad, aberto_ad

    if aberto_ad <= 2:
        if not janela_ad or not janela_ad.winfo_exists():
            if os.path.isfile("adm.txt"):
                tkinter.messagebox.showinfo("Aviso","Senha e Usúario já foi cadastrado!")
            else:
                janela_ad = Toplevel(janela)
                janela_ad.geometry("300x200")
                janela_ad.resizable(False,False)
                janela_ad.title("Administrador")

                label = Label(janela_ad, text="Defina um usúario e senha!")
                label.place(x=75,y=10)

                # Usuario
                label = Label(janela_ad, text="Usúario: ", background= cinza_claro)
                label.place(x=40,y=60)
                entry_us = Entry(janela_ad, width= 22)
                entry_us.place(x=102,y=60)

                # Senha
                label = Label(janela_ad, text="Senha: ", background= cinza_claro)
                label.place(x=40,y=100)
                entry_se = Entry(janela_ad, width= 24)
                entry_se.place(x=91,y=100)

                def confirmar():
                    gravar = []
                    usuario = entry_us.get()
                    senha = entry_se.get()
                    arquivo = open("adm.txt", "a")
                    gravar.append("\nAdministrção\n")
                    gravar.append("\nUsúario: " +  usuario)
                    gravar.append("\nSenha: " + senha)
                    arquivo.writelines(gravar)
                    arquivo.close()
                    tkinter.messagebox.showinfo("Aviso","Cadastro realizado! Lembre-se de sua senha!")
                    janela_ad.destroy()
                    janela_ad.protocol("WM_DELETE_WINDOW", fechar_janela_adm)

                # Botões
                botao =Button(janela_ad, text= "Confirmar", command= confirmar)
                botao.place(x=110,y=160)

            aberto_ad += 1
            janela_ad.wait_window()

def fechar_janela_apagar():
    global janela_ad_ap, aberto_ad_ap

    if janela_ad_ap.winfo_exists():
        janela_ad_ap.destroy()
    aberto_ad_ap = 0 

def apagar():
    global janela_ad_ap, aberto_ad_ap

    if aberto_ad_ap <= 2:
        if not janela_ad_ap or not janela_ad_ap.winfo_exists():
            if os.path.isfile("adm.txt"):
                janela_ad_ap = Toplevel(janela)
                janela_ad_ap.geometry("300x200")
                janela_ad_ap.resizable(False,False)
                janela_ad_ap.title("Administrador")

                label = Label(janela_ad_ap, text="Ao apagar perderá o cadastro da área!")
                label.place(x=50,y=10)

                # Usuario
                label = Label(janela_ad_ap, text="Usúario: ", background= cinza_claro)
                label.place(x=40,y=60)
                entry_us = Entry(janela_ad_ap, width= 22)
                entry_us.place(x=102,y=60)

                # Senha
                label = Label(janela_ad_ap, text="Senha: ", background= cinza_claro)
                label.place(x=40,y=100)
                entry_se = Entry(janela_ad_ap, width= 24)
                entry_se.place(x=91,y=100)

                def confirmar():
                    usuario = entry_us.get()
                    senha = entry_se.get()

                    # Carrega a senha e o usúario configurado anteriormente
                    arquivo = open("adm.txt", "r")
                    for linha in arquivo:
                        if "Usúario:" in linha:
                            usuario_padrao = linha[9:]
                        elif "Senha:" in linha:
                            senha_padrao = linha[7:]
                    arquivo.close()

                    # verifica se é a mesma senha e usuario
                    if usuario == usuario_padrao or senha == senha_padrao:
                        os.remove("dadosarea.txt")
                        tkinter.messagebox.showinfo("Aviso", "Dados da área excluídos!")
                    else:
                        tkinter.messagebox.showerror("Aviso", "Senha ou Usúario errado!")
                    janela_ad_ap.protocol("WM_DELETE_WINDOW", fechar_janela_apagar)

            else:
                tkinter.messagebox.showerror("Aviso", "Voçê ainda não registrou sua senha e usúario!")

            aberto_ad_ap += 1
            janela_ad_ap.wait_window()

    # Botões
    botao =Button(janela_ad, text= "Apagar", command= confirmar)
    botao.place(x=110,y=160)

def fechar_janela_apagar_cadastros():
    global janela_ad_apc, aberto_ad_apc

    if janela_ad_apc.winfo_exists():
        janela_ad_apc.destroy()
    aberto_ad_apc = 0 

def apagar_cadastros():
    global janela_ad_apc, aberto_ad_ap

    if aberto_ad_ap <= 2:
        if not janela_ad_apc or not janela_ad_apc.winfo_exists():
            if os.path.isfile("adm.txt"):
                janela_ad_apc = Toplevel(janela)
                janela_ad_apc.geometry("300x200")
                janela_ad_apc.resizable(False,False)
                janela_ad_apc.title("Administrador")

                label = Label(janela_ad_apc, text="Ao apagar perderá o TODOS os cadastros!")
                label.place(x=40,y=10)

                # Usuario
                label = Label(janela_ad_apc, text="Usúario: ", background= cinza_claro)
                label.place(x=40,y=60)
                entry_us = Entry(janela_ad, width= 22)
                entry_us.place(x=102,y=60)

                # Senha
                label = Label(janela_ad_apc, text="Senha: ", background= cinza_claro)
                label.place(x=40,y=100)
                entry_se = Entry(janela_ad_apc, width= 24)
                entry_se.place(x=91,y=100)

                def confirmar():
                    usuario = entry_us.get()
                    senha = entry_se.get()

                    # Carrega a senha e o usúario configurado anteriormente
                    arquivo = open("adm.txt", "r")
                    for linha in arquivo:
                        if "Usúario:" in linha:
                            usuario_padrao = linha[9:]
                        elif "Senha:" in linha:
                            senha_padrao = linha[7:]
                    arquivo.close()

                    # verifica se é a mesma senha e usuario
                    if usuario == usuario_padrao or senha == senha_padrao:
                        os.remove("cadastro.txt")
                        tkinter.messagebox.showinfo("Aviso", "Dados da área excluídos!")
                    else:
                        tkinter.messagebox.showerror("Aviso", "Senha ou Usúario errado!")
                    janela_ad_apc.protocol("WM_DELETE_WINDOW", fechar_janela_apagar_cadastros)

            else:
                tkinter.messagebox.showerror("Aviso", "Voçê ainda não registrou sua senha e usúario!")

            # Botões
            botao =Button(janela_ad, text= "Apagar", command= confirmar)
            botao.place(x=110,y=160)

            aberto_ad_apc += 1
            janela_ad_apc.wait_window()

# Botão
botao =Button(janela, text= "Cadastrar", command= cadastrar, width= 18)
botao.place(x=90,y=20)

botao =Button(janela, text= "Cadastrar a Área", command= cad_area, width= 18)
botao.place(x=90,y=70)

botao =Button(janela, text= "Alugar", command= alugar, width= 18)
botao.place(x=90,y=120)

botao =Button(janela, text= "Relação da Área", command= relacao, width= 18)
botao.place(x=90,y=170)

botao =Button(janela, text= "Relátorio Clientes", command= relatorio, width= 18)
botao.place(x=90,y=220)

botao =Button(janela, text= "Administração", command= adm, width= 18)
botao.place(x=90,y=270)

janela.mainloop()