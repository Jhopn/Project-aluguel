import tkinter as tk
from tkcalendar import Calendar, DateEntry

def selecionar_data():
    data_selecionada = cal.get_date()
    label_data.config(text="Data selecionada: " + data_selecionada)
    cal.configure(selectbackground='red', selectforeground='white')

root = tk.Tk()
root.title("Calendário")

cal = Calendar(root, selectmode='day')
cal.pack()

btn_selecionar = tk.Button(root, text="Selecionar Data", command=selecionar_data)
btn_selecionar.pack()

label_data = tk.Label(root, text="Data selecionada: ")
label_data.pack()

root.mainloop()
