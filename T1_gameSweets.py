# Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.
import random

def mansMove(candys)->int:
    tookCandys=int(input('Введите сколько конфет вы возьмете(!не больше 28):'))
    if candys<28:
        while tookCandys<0 or tookCandys>candys:
            print(f'Вы взяли конфет больше,чем осталось! Вы можете взять от 1 до {candys}!')
            tookCandys=int(input('Введите еще раз сколько конфет вы возьмете:'))
    else:
        while tookCandys<0 or tookCandys>28:
            print('Вы ввели неправильное число конфет!Должно быть от 1 до 28!')
            tookCandys=int(input('Введите еще раз сколько конфет вы возьмете:'))
    leftoverСandy=candys-tookCandys
    print(f'Осталось {leftoverСandy} конфет')
    return leftoverСandy

def botMove(candys)->int:
    if candys<29:
        tookCandys=random.randint(1,candys)
    else:
        tookCandys=random.randint(1,28)
    print(f'Компьютер взял {tookCandys} конфет')
    leftoverСandy=candys-tookCandys
    print(f'Осталось {leftoverСandy} конфет')
    return leftoverСandy

print('Есть 120 конфет за раз можно взять не больше 28 конфет.Выигрывает тот, кто оставил на столе 0 конфет')
sweets=120
while sweets!=0:
    sweets=mansMove(sweets)
    if sweets==0:
        print('Поздравляю!Вы победили компьютер!')
        break
    sweets=botMove(sweets)
    if sweets==0:
        print('Компьютер победил. Игра закончена.')
        break

