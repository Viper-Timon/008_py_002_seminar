# 4. Дополнительно:
# Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.
# Требуется определить: через сколько лет вклад составит не менее Y рублей.
#     Пример:
#     100
#     10
#     200
#     Вывод:
#     8

x = float(input('Сумма вклада = '))
p = float(input('Процент по вкладу = '))
y = float(input('Желаемая сумма = '))
if x > 0 and p > 0 and y > x:
    sum_vk= x 
    count = 0
    while sum_vk < y:
        sum_vk+=sum_vk*(p/100)
        sum_vk=int(sum_vk) # первая сумма также может иметь 
        # дробную часть, и если её округлять ранее - будет некорректно по логике вкладов 
        # т.е. не с нужной (меньшей) суммы начисление процентов =)
        count+=1
    print (count)
else: print('Введите другие значения')
