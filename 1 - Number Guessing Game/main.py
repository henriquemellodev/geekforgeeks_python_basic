import random

print('Oi, bem vindo ao jogo. Este é um jogo de advinhação de números.\nVocê tem 7 chances de advinhar o número. Vamos começar o jogo!')

number_to_guess = random.randrange(100)

chances = 7

guess_counter = 0

while guess_counter < chances:
  guess_counter += 1
  my_guess = int(input('Por favor, digite seu palpite: '))
  
  if my_guess == number_to_guess:
    print(f"O número é {number_to_guess} e você acertou na tentativa {guess_counter}")
    break
  elif guess_counter >= chances and my_guess != number_to_guess:
    print(f"Ops, desculpe, o número é {number_to_guess}, boa soret na próxima vez!")
  
  elif my_guess > number_to_guess:
    print("Seu palpite está alto.")
  
  elif my_guess < number_to_guess:
    print("Seu palpite está muito baixo.") 