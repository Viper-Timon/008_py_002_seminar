# 2. Для натурального n создать словарь 
# индекс-значение, состоящий из элементов 
# последовательности 3n + 1.
    
# *Пример:*
    
#     - Для n = 6: 
# {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}



# number = {'Ivan':79543342356, 
#             'Segey':54654654333}
# print(number['Segey'])
# # print(list(number.items()))
# number[0]= 16
# print(number)

print('введите N')
n = int(input())
number={1:0}
for i in range(1,n+1):
    number[i]=3*i+1
print(number)

