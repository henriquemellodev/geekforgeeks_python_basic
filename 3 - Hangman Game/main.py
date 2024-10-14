import tkinter as tk
import random

# Lista de palavras para advinhação
words = ['maça','banana','cereja','dia','uva']

# Escolha a palavra sorteada
word = random.choice(words)
guessed = ['_' for _ in word] # Lista para manter o controle das letras adivinhadas

def guess(letter):
  if letter in word:
    update_guessed(letter)
  update_display()
  
def update_guessed(letter):
  for index, char in enumerate(word):
    if char == letter:
      guessed[index] = letter
      
def update_display():
  label.config(text=' '.join(guessed))
  if '_' not in guessed:
    label.config(text='Você venceu!')
    
# Criar a janela principal
root = tk.Tk()
root.title("Jogo da Forca")

# Cria a label para mostrar a palavra para advinhação
label = tk.Label(root, text=' '.join(guessed), font=('Helvetica', 24))
label.pack(pady=20)

# Criar o frame para os botoes
frame = tk.Frame(root)
frame.pack()

# Cria botoes para cada letra
for ascii_code in range(97, 123): # Codigos ASCII para a-z
  letter = chr(ascii_code)
  btn = tk.Button(frame, text=letter.upper(), command=lambda l=letter: guess(l))
  btn.pack(side='left')
  
# Rodar a aplicação
root.mainloop()