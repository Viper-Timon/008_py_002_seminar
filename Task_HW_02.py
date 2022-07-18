# 2. Напишите программу, которая принимает 
# на вход число N и выдает набор произведений 
# чисел от 1 до N. Факториал
#     5! = 120


def factorial_n(n):
    comp = 1
    i=1
    while i <=n:
        comp*=i
        i+=1
    return comp


num = int(input('введите N = '))
print(factorial_n(num))