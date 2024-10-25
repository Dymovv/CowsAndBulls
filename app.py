import random

ex = [exnum for exnum in range(100,1000) if str(exnum).count('0') > 0] # добавление в спсисок чисел-исключений (в данном случае это числа от 100 до 999, имеющие 0 в составе)
compnumber = random.choice([num for num in range(100,10000) if len(set(str(num))) == len(str(num)) and num not in ex])  # число, загаданное компьютером (с ограничениями)

if compnumber < 1000:
  compnumber = '0'+str(compnumber)        # добавление 0 в начало 3-значных чисел


while True:
  player_move = int(input('Введите число: '))
  if player_move < 1000:
    player_move = '0'+str(player_move)        # добавление 0 в начало 3-значных чисел
  if (len(set(str((player_move)))) < len(str(player_move))) or (len(str(player_move)) != 4):        # проверка корректности ввода
    print('Некорректный формат ввода!')
    continue

  bulls = 0
  counter = 0
  for num in str(compnumber):                                     # проверка быков
    if str(player_move)[counter] == num:
      bulls += 1
    counter += 1

  counter = 0
  cows = 0
  for num in str(compnumber):                                               # проверка коров
    if str(player_move)[counter] != num and num in str(player_move):
      cows += 1
    counter += 1

  print('Коровы:', cows, 'Быки', bulls)
  print(compnumber)
  if player_move == compnumber:
    print('Вы победили!')
    break




