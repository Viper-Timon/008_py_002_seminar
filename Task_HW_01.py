# 1.  Напишите программу, которая принимает
# на вход вещественное число
# и показывает сумму его цифр.

#     Пример:

#     6782 -> 23
#     0,56 -> 11



def Find_Sum_Numbers(x):
    sum = 0
    x=str(x)
    for i in x:
        if i.isdigit() == 1:
            sum+=int(i)
    return sum


n = input()
print(Find_Sum_Numbers(n))
