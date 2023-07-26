import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Crie uma janela principal
janela = tk.Tk()
janela.title("Exemplo de Imagem da Internet no Tkinter")

# URL da imagem que você deseja exibir
url_imagem = "https://cdn-icons-png.flaticon.com/128/6932/6932392.png"  # Substitua pela URL correta da imagem

# Faça o download da imagem da internet
response = requests.get(url_imagem)
imagem = Image.open(BytesIO(response.content))
imagem = imagem.resize((40, 40))  # Redimensione a imagem para exibição

# Converta a imagem para o formato compatível com o Tkinter
imagem_tk = ImageTk.PhotoImage(imagem)

# Crie um widget Label para exibir a imagem
label_imagem = tk.Label(janela, image=imagem_tk)
label_imagem.pack()

# Inicie o loop principal do Tkinter
janela.mainloop()
