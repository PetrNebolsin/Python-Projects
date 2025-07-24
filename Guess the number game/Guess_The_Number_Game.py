'''Игра "Угадай число"'''


import random # Библиотека для генирации случайного числа
number = random.randint(1,1000000) # Получаем случайное число
print('отгадайте число')
player = int(input())
while player != number: # Пока игрок не угадает число...
    try:
        if player < number:
            print('мое число больше')
            player = int(input())
        elif player > number:
            print('мое число меньше')
            player = int(input())
    except:
        print('попробуй еще раз')
        player = int(input())
print('ты угадал')
