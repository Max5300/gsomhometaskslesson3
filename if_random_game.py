import random
x = int(input("Введите число от 1 до 4: "))
y = random.randint(1, 4)
if x == y:
    print("Победа")
else:
    if x > y:
        print("Повторите еще раз! Введенное число больше загаданного")
    else:
        print("Повторите еще раз! Введенное число меньше загаданного")
