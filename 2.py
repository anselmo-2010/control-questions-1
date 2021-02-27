from random import randint

random_number = randint(1, 20)

i = 0
while i < 5:
    count = int(input("Введите число от 1 до 20 - "))
    if random_number == count:
        print("Класс! Вы угадали")
        print("Случайное число :", random_number)
        break
    elif random_number > count:
        print("Слишком мало")
    elif random_number < count:
        print("Слишком много")
    i+=1
if i == 5:
    print("Все вы не выиграли. Игра завершилась")          


