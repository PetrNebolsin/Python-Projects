try:
    print ('Привет!\nДавай я расчитаю сколько тебе лет!')
    my_year = int(input('В каком году ты родился: '))
    current_year = int(input('Какой год сейчас: '))
    birthday = int(input('У тебя уже был день рождение в этом году? 1-да 2-нет: '))
    if birthday == 1:
        print('Тебе', current_year - my_year ,'лет!')
    if  birthday == 2:
        print('Тебе', current_year - my_year-1 ,'лет!')
except:
    print('Что-то т опошло не так')
