import random

options = ('piedra', 'papel', 'tijera')
computer_wins = 0
user_wins = 0
rounds = 1

while True:
  print('*' * 40)
  print('                 ROUND', rounds)
  print('Computer => ', computer_wins, '            User => ', user_wins)
  print('*' * 40)
  user_option = input("piedra, papel o tijera => ")
  user_option = user_option.lower()

  if not user_option in options:
    print(user_option, "no es valida ")
    continue

  computer_option = random.choice(options)
  print("-" * 40)
  print("User option =>", user_option)
  print("Computer option =>", computer_option)
  print("-" * 40)

  if user_option == computer_option:
    print("Empate!")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("Piedra gana a tijera")
      print("user gano este ROUND")
      user_wins += 1

    else:
      print("Papel gana a piedra")
      print("computer gano este ROUND!")
      computer_wins += 1
  elif user_option == "papel":
    if computer_option == "piedra":
      print("Papel gana a piedra")
      print("user gano este ROUND")
      user_wins += 1
    else:
      print("tijera gana a papel")
      print("computer gano este ROUND!")
      computer_wins += 1
  elif user_option == "tijera":
    if computer_option == "papel":
      print("Tijera gana a papel")
      print("user gano este ROUND ")
      user_wins += 1
    else:
      print("Piedra gana a tijera")
      print("computer gano este ROUND!")
      computer_wins += 1
  if computer_wins == 3:
    print('*' * 40)
    print('      ¡¡La computadora ganó el juego¡¡', )
    print('*' * 40)
    break
  if user_wins == 3:
    print('*' * 40)
    print('      ¡¡El usuario ganó el juego¡¡')
    print('*' * 40)
    break

  rounds += 1