import random

name = input("Qual o seu nome? ")
print("Boa sorte, ", name)

words = ['chuva', 'computador', 'ciência', 'programação',
         'python', 'matematica', 'player', 'condição', 'reverso',
         'água', 'board', 'geeks']

word = random.choice(words)

print("Advinhe as letras.")

guesses = ''
turns = 12

while turns > 0:
  failed = 0
  
  for char in word:
    if char in guesses:
      print(char, end="")
    else:
      print("_")
      failed += 1
  
  if failed == 0:
    print("Você venceu!")
    print("A palavra é: ", word)
    break
  
  print()
  guess = input("Advinhe a letra: ")
  
  guesses += guess
  
  if guess not in word:
    turns -= 1
    print("Você tem ", + turns, "para advinhar")
    
    if turns == 0:
      print("Você perdeu!")