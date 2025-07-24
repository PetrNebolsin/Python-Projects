YOAN = 0.091
DOLLAR= 0.013
EURO = 0.011
print('Здравствуйте!')
print('На какую валютум вы будете менять?')
print('Вы можете поменять на евро, доллар или на овшорный юань.')
print('Выберите: 1-доллар 2-евро 3-юань')
choise = input()
if choise > '3' :
    print('Ошибка')
elif choise < '1' :
    print('Ошибка')    
print(f'Спасибо за выбор!Вы выбрали {choise}!') 
print('Сколько у вас рублей?')
choise_1 = int(input())
if choise == '1' :
    result = choise_1 * DOLLAR
    print(f'Вы получаете {result} долларов')
elif choise == '2' :
    result = choise_1 * EURO
    print(f'Вы получаете {result} евро')
elif choise == '3' :
    result = choise_1 * YOAN
    print(f'Вы получаете {result} юаней')
frase = input()