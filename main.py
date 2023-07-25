from tkinter import *
import tkinter.messagebox
from tkinter.ttk import *
from datetime import datetime
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
    checargnr = StringVar()

    # Desing
    quadrado = Canvas(janela_cad, width=400, height=600)
    quadrado.create_rectangle(10, 10, 290, 290, fill="blue")
    quadrado.place(x=0,y=0)
    
    # Nome
    label = Label(janela_cad, text="Nome: ")
    label.place(x=10,y=20)
    entry_nm = Entry(janela_cad)
    entry_nm.place(x=160,y=20)
    # CPF
    label = Label(janela_cad, text="CPF: ")
    label.place(x=10,y=70)
    entry_cpf = Entry(janela_cad)
    entry_cpf.place(x=200,y=70)
    # Endereço
    label = Label(janela_cad, text="Endereço: ")
    label.place(x=10,y=120)
    entry_end = Entry(janela_cad)
    entry_end.place(x=200,y=120)
    # Telefone
    label = Label(janela_cad, text="Telefone: ")
    label.place(x=10,y=170)
    entry_tel = Entry(janela_cad)
    entry_tel.place(x=200,y=170)

    # Genero 
    radio1 = Radiobutton(janela_cad,text = "Feminino", value = "Feminino", var = checargnr)
    radio1.place(x=10, y=220)

    radio1 = Radiobutton(janela_cad,text = "Masculino", value = "Masculino", var= checargnr)
    radio1.place(x=130, y=220)

    radio2 = Radiobutton(janela_cad,text = "Outro", value = "Outro", var = checargnr)
    radio2.place(x=190, y=290)
    
    def confirmar():
        nome = entry_nm.get()
        nome = nome.upper()
        cpf = entry_cpf.get()
        endereco = entry_end.get()
        endereco = endereco.upper()
        telefone = entry_tel.get()

        gravar = []
        arquivo = open("cadastro.txt", "a")
        gravar.append("\nDados\n")
        gravar.append("\nNome: " +  nome)
        gravar.append("\nCPF: " + cpf)
        gravar.append("\nEndereço: " +  endereco)
        gravar.append("\nTelefone: " + telefone)
        gravar.append("\nGenêro: "+ checargnr.get())
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
    botao.place(x=110,y=250)

def cad_area():
    if os.path.isfile("dadosarea.txt"):
        tkinter.messagebox.showinfo("Aviso","Cadastro já foi realizado!")
    else:
        janela_cad_area = Toplevel(janela)
        janela_cad_area.geometry("300x300")
        janela_cad_area.resizable(False,False)
        janela_cad_area.title("Cadastrar Área")

        # Nome da área
        label = Label(janela_cad_area, text="Nome da área: ")
        label.place(x=10,y=20)
        entry_nm_ar = Entry(janela_cad_area)
        entry_nm_ar.place(x=130,y=20)

        # Endereço da área
        label = Label(janela_cad_area, text="Endereço da área: ")
        label.place(x=10,y=70)
        entry_end_ar = Entry(janela_cad_area)
        entry_end_ar.place(x=130,y=70)

        # Valor da área
        label = Label(janela_cad_area, text="Valor da área R$: ")
        label.place(x=10,y=120)
        entry_valor = Entry(janela_cad_area)
        entry_valor.place(x=130,y=120)

        def confirmar():
            nome = entry_nm_ar.get()
            endereco = entry_end_ar.get()
            valor = entry_valor.get()

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
        botao.place(x=110,y=250)


def alugar():
    if os.path.isfile("cadastro.txt"):
        janela_alugar = Toplevel(janela)
        janela_alugar.geometry("500x390")
        janela_alugar.resizable(False,False)
        janela_alugar.title("Aluguel")
        checar_cadeira = StringVar()
        checar_cozinha = StringVar()
    
        # Deixar o calendario att
        data_atual = datetime.now()
        ano = data_atual.year
        mes = data_atual.month
        dia = data_atual.day

        # Listar Clientes
        listar_clientes = Listbox(janela_alugar, width= 30)
        listar_clientes.place(x=270,y=70)

        # Carregar nomes dos clientes
        arquivo = open("cadastro.txt", "r")
        for linha in arquivo:
            if "Nome:" in linha:
                nome = linha
                nome = nome[5:]
                listar_clientes.insert(END,nome)
        arquivo.close()

        # Busca
        label = Label(janela_alugar, text= "Pesquise:")
        label.place(x=270,y=10)

        busca = Entry(janela_alugar)
        busca.place(x=325,y=10) 

        # Horario do aluguel
        label_estado = Label(janela_alugar, text= "Horário: ")
        label_estado.place(x=20,y=260)

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
        combo_in.place(x=80,y=260)

        combo_fm = Combobox(janela_alugar, width= 5)
        combo_fm['values'] = (horarios)
        combo_fm.current(0)
        combo_fm.place(x=190,y=260)

        # Cadeiras
        check1 = Checkbutton(janela_alugar, text= "Cadeira", var= checar_cadeira , onvalue="Com cadeira", offvalue="Sem cadeira" )
        check1.place(x=20,y=290)
        check2 = Checkbutton(janela_alugar, text= "Cozinha", var= checar_cozinha , onvalue="Com cozinha", offvalue="Sem cozinha")
        check2.place(x=160,y=290)

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
        calendario.place(x=10,y=20)

        # carregar alugueis e deixar o calendario marcado 
        gravar = []
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
                gravar.append("\n| Aluguel |")
                gravar.append("\nCliente: " +  nome)
                gravar.append("\nData Alugada: " + calendario.get_date())
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
                gravar.append("\n-----------------------------------")
                arquivo.writelines(gravar)
                arquivo.close()
                tkinter.messagebox.showinfo("Aviso","Alugado com sucesso!")

        #Botões
        botao =Button(janela_alugar, text= "Alugar", command= alugar_ar)
        botao.place(x=270,y=40)

    else:
        tkinter.messagebox.showinfo("Aviso","Nenhum cadastro realizado criado!")


def relacao():
    if os.path.isfile("aluguel.txt"):
        janela_ex = Toplevel(janela)
        janela_ex.geometry("300x300")
        janela_ex.resizable(False,False)
        janela_ex.title("Exibir Dados da Área")

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
        
        label = Label(janela_ex, text= "Dados da Área", font= "Arial, 14")
        label.place(x=90,y=5)

        label = Label(janela_ex, text= dados[0])
        label.place(x=10,y=30)

        label = Label(janela_ex, text= dados[1])
        label.place(x=10,y=50)

        label = Label(janela_ex, text= dados[2])
        label.place(x=10,y=70)

        listar_clientes = Listbox(janela_ex, width= 46)
        listar_clientes.place(x=10,y=130)

        arquivo = open("aluguel.txt", "r")
        for linha in arquivo:
            if "Cliente:" in linha:
                listar_clientes.insert(END, "\n")
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
        label = Label(janela_ex, text= "Pesquise:")
        label.place(x=70,y=100)
        busca = Entry(janela_ex)
        busca.place(x=130,y=100)

        def pesquisar():
                pesquisa = busca.get()
                pesquisa = pesquisa.upper()
                arquivo = open("aluguel.txt", "r")
                achou = False
                # Limpa a listbox
                listar_clientes.delete(0, END)
                for linha in arquivo:
                    if pesquisa in linha and "Cliente:" in linha:
                        listar_clientes.insert(END, "\n")
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
                            listar_clientes.insert(END, "\n")
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
        
        def apagar():
            janela_ex = Toplevel(janela)
            janela_ex.geometry("300x300")
            janela_ex.resizable(False,False)
            janela_ex.title("Exibir Dados da Área")


        # Botões 
        botao =Button(janela_ex, text= "Apagar Cadastro Área", command= apagar)
        botao.place(x=260,y=40)

    else:
        tkinter.messagebox.showerror("Aviso","Nenhum aluguel realizado!")
    
def relatorio():
    if os.path.isfile("cadastro.txt"):
        janela_relat = Toplevel(janela)
        janela_relat.geometry("300x300")
        janela_relat.resizable(False,False)
        janela_relat.title("Relatorio")

        listar_clientes = Listbox(janela_relat, width= 46, height= 14)
        listar_clientes.place(x=10,y=40)

        # Carregar nomes dos clientes
        arquivo = open("cadastro.txt", "r")
        for linha in arquivo:
            if "Nome:" in linha:
                nome = linha
                nome = nome[5:]
                listar_clientes.insert(END,nome)
        arquivo.close()

        # Pesquisa
        label = Label(janela_relat, text= "Pesquise:")
        label.place(x=70,y=10)
        busca = Entry(janela_relat)
        busca.place(x=130,y=10)

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

            # Desing
            #canvas = Canvas(janela_relat, width=300, height=200)
            #canvas.create_rectangle(50, 50, 200, 150, fill="blue")
            #canvas.pack(fill = BOTH, expand = True)
        
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
        botao.place(x=110,y=272)

    else:
        tkinter.messagebox.showerror("Aviso","Nenhum cadastro realizado!")

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


janela.mainloop()