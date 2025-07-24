import random
print("Привет!")
print("Сыграем в камень - ножницы - бумага! Это не отсылка на Влада А4 ")
player_choice = ''
while player_choice != 'Хватит!':
    print('Напиши "хватит", если захочешь закончить игру.\n')
    player_choice = input("Выбери камень, ножницы, бумагу: \n")
    comp_choice = random.choice(["камень","ножницы","бумага"])
    if player_choice == comp_choice:
        print('Мы оба выбрали', player_choice, ':)')
        print("Ничья!")
    elif player_choice == 'камень':
        print(f'Ты выбрал: {player_choice}, а я выбрал: {comp_choice}.')
        if comp_choice == 'ножницы':
            print('Ты выиграл')
        elif comp_choice == 'бумага':
            print('Ты проиграл')
    elif player_choice == 'ножницы':
        print(f'Ты выбрал: {player_choice}, а я выбрал: {comp_choice}.')
        if comp_choice == 'бумага':
            print('Ты выиграл')
        elif comp_choice == 'камень':
            print('Ты проиграл')
    elif player_choice == 'бумага':
        print(f'Ты выбрал: {player_choice}, а я выбрал: {comp_choice}.')
        if comp_choice == 'камень':
            print('Ты выиграл')
        elif comp_choice == 'ножницы':
            print('Ты проиграл')
    else:
        print('Я не понял что ты выбрал!')
print('Конец игры!До свидания!')
